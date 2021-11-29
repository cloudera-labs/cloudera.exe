terraform {
  required_version = ">= 0.13"
  required_providers {
    aws = "~> 3.0"
  }
}

provider "aws" {
  region         = var.region
  default_tags {
    tags         = var.tags
  }
  ignore_tags {
    keys         = ["kubernetes.io/role/internal-elb", "kubernetes.io/role/elb"]
    key_prefixes = ["kubernetes.io/cluster/"]
  }
}

data "aws_availability_zones" "available" {
  state = "available"
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.2.0"

  tags = var.tags

  name = var.vpc_name
  cidr = "10.10.0.0/16"
  
  enable_nat_gateway = true
  igw_tags           = var.tags
  nat_eip_tags       = var.tags
  nat_gateway_tags   = var.tags

  enable_dns_hostnames = true

  # azs                      = [ "us-east-2a", "us-east-2b", "us-east-2c"]
  azs                      = data.aws_availability_zones.available.names
  public_subnets           = [ "10.10.0.0/19", "10.10.32.0/19", "10.10.64.0/19" ]
  public_subnet_tags       = merge({ "kubernetes.io/role/elb" = "1" }, var.tags)
  public_route_table_tags  = var.tags
  private_subnets          = [ "10.10.96.0/19", "10.10.128.0/19", "10.10.160.0/19" ]
  private_subnet_tags      = merge({ "kubernetes.io/role/internal-elb" = "1" }, var.tags)
  private_route_table_tags = var.tags
}

module "default_sg" {
  source = "terraform-aws-modules/security-group/aws"

  name            = var.sg_names.default
  use_name_prefix = false
  description     = "Default for Molecule integration test. Namespace: ${var.name_prefix}"
  vpc_id          = module.vpc.vpc_id

  ingress_cidr_blocks      = [ module.vpc.vpc_cidr_block ]
  ingress_rules            = [ "all-all" ]
  ingress_with_cidr_blocks = concat(local.cdp_controlplane_rules, var.extra_rules)
  ingress_with_self        = [ { rule = "all-all" } ]

  egress_cidr_blocks = [ "0.0.0.0/0" ]
  egress_rules       = [ "all-all" ]
}

module "knox_sg" {
  source = "terraform-aws-modules/security-group/aws"

  name            = var.sg_names.knox
  use_name_prefix = false
  description     = "Knox for Molecule integration test. Namespace: ${var.name_prefix}"
  vpc_id          = module.vpc.vpc_id

  ingress_cidr_blocks      = [ module.vpc.vpc_cidr_block ]
  ingress_rules            = [ "all-all" ]
  ingress_with_cidr_blocks = concat(local.cdp_controlplane_rules, var.extra_rules)
  ingress_with_self        = [ { rule = "all-all" } ]

  egress_cidr_blocks = [ "0.0.0.0/0" ]
  egress_rules       = [ "all-all" ]
}

# These are only necessary if not tunneling, i.e. Level0
locals {
  cdp_controlplane_rules = [
    {
      rule        = "https-443-tcp"
      cidr_blocks = "52.36.110.208/32,52.40.165.49/32,35.166.86.177/32"
    },
    {
      from_port   = 9443
      to_port     = 9443
      protocol    = "tcp"
      cidr_blocks = "52.36.110.208/32,52.40.165.49/32,35.166.86.177/32"
    }
  ]
}