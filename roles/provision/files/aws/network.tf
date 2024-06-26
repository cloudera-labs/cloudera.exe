variable "cluster_prefix" {
  type = string
  description = "Deployment cluster prefix"
  validation {
    condition     = length(var.cluster_prefix) < 9 && length(var.cluster_prefix) > 4
    error_message = "The deployment cluster prefix must be between 5-8 characters."
  }
}

variable "vpc_name" {
  type        = string
  description = "VPC name"
  default     = null
}

variable "vpc_cidr" {
  type        = string
  description = "VPC CIDR block"
  default     = "172.16.0.0/16"
}

variable "vpc_enable_dns_support" {
  type        = bool
  description = "VPC DNS Support"
  default     = true
}

variable "vpc_enable_dns_hostnames" {
  type        = bool
  description = "VPC DNS Hostnames"
  default     = true
}

variable "igw_name" {
  type        = string
  description = "Internet Gateway name"
  default     = null
}

variable "public_subnets" {
  type       = list(object({
    az          = string
    name        = optional(string)
    cidr        = optional(string)
    cidr_range  = optional(number, 4)
    tags        = optional(map(string), {})
  }))

  description = "List of public subnets"
  default    = []
}

variable "public_route_table_name" {
  type        = string
  description = "Public route table name"
  default     = null
}

variable "private_subnets" {
  type       = list(object({
    az          = string
    name        = optional(string)
    cidr        = optional(string)
    cidr_range  = optional(number, 4)
    tags        = optional(map(string), {})
  }))

  description = "List of private subnets"
  default    = []
}

variable "nat_gateway_name" {
  type        = string
  description = "NAT gateway name"
  default     = null
}

variable "private_route_table_name" {
  type        = string
  description = "Private route table name"
  default     = null
}

# Security Groups
variable "security_group_default_name" {
  type        = string
  description = "Default Security Group name"
  default     = null
}

variable "security_group_default_desc" {
  type        = string
  description = "Default Security Group description"
  default     = null
}

variable "security_group_rules_ingress" {
  type       = list(object({
    cidr       = list(string)
    from_port  = string
    to_port    = string
    protocol   = string
  }))

  description = "Ingress rules for default Security Group"
  default    = []
}

# ------- Virtual Network -------
resource "aws_vpc" "cluster" {
  cidr_block            = var.vpc_cidr
  tags                  = { Name = var.vpc_name != null ? var.vpc_name : var.cluster_prefix }
  instance_tenancy      = "default"
  enable_dns_support    = var.vpc_enable_dns_support
  enable_dns_hostnames  = var.vpc_enable_dns_hostnames
}

# ------- Public Network infrastructure -------
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.cluster.id
  tags   = { Name = var.igw_name != null ? var.igw_name : var.cluster_prefix }
}

locals {
  public_subnets = [
    for idx, subnet in var.public_subnets :
      merge(subnet, { name = subnet.name != null ? subnet.name : "${var.cluster_prefix}-public-${format("%02d", idx+1)}" })
  ]

  private_subnets = [
    for idx, subnet in var.private_subnets :
      merge(subnet, { name = subnet.name != null ? subnet.name : "${var.cluster_prefix}-private-${format("%02d", idx+1)}" })
  ]

  cidr_allocation = zipmap(
    [for subnet in concat(local.public_subnets, local.private_subnets) : subnet.name if subnet.cidr == null],
    cidrsubnets(var.vpc_cidr, [for subnet in concat(local.public_subnets, local.private_subnets) : subnet.cidr_range if subnet.cidr == null]...)
  )
}

resource "aws_subnet" "public_subnets" {
  for_each                = {for idx, subnet in local.public_subnets: idx => subnet}

  vpc_id                  = aws_vpc.cluster.id
  cidr_block              = each.value.cidr != null ? each.value.cidr : local.cidr_allocation[each.value.name]
  map_public_ip_on_launch = true
  availability_zone       = each.value.az
  tags                    = merge(each.value.tags, { Name = each.value.name })
}

resource "aws_default_route_table" "public_route_table" {
  default_route_table_id = aws_vpc.cluster.default_route_table_id

  route {
    cidr_block           = "0.0.0.0/0"
    gateway_id           = aws_internet_gateway.igw.id
  }

  tags                   = { Name = var.public_route_table_name != null ? var.public_route_table_name : "${var.cluster_prefix}-public" }
}

resource "aws_route_table_association" "public_subnets" {
  for_each        = aws_subnet.public_subnets

  subnet_id       = each.value.id
  route_table_id  = aws_vpc.cluster.default_route_table_id
}

# ------- Private Network infrastructure -------
resource "aws_subnet" "private_subnets" {
  for_each                = {for idx, subnet in local.private_subnets: idx => subnet}

  vpc_id                  = aws_vpc.cluster.id
  cidr_block              = each.value.cidr != null ? each.value.cidr : local.cidr_allocation[each.value.name]
  map_public_ip_on_launch = false
  availability_zone       = each.value.az
  tags                    = merge(each.value.tags, { Name = each.value.name })
}

resource "aws_eip" "nat_gateway_eip" {
  for_each  = aws_subnet.private_subnets

  vpc       = true
  tags      = merge(each.value.tags, { Name = "${var.cluster_prefix}-${each.value.tags_all["Name"]}-nat" })
}

resource "aws_nat_gateway" "private_subnets" {
  for_each          = aws_subnet.private_subnets

  subnet_id         = aws_subnet.public_subnets[each.key % length(aws_subnet.public_subnets)].id
  allocation_id     = aws_eip.nat_gateway_eip[each.key].id
  connectivity_type = "public"

  tags              = { Name = each.value.tags_all["Name"] != null ? each.value.tags_all["Name"] : "${var.cluster_prefix}-nat-${format("%02d", each.key+1)}" }
}

resource "aws_route_table" "private_route_table" {
  for_each          = aws_nat_gateway.private_subnets

  vpc_id            = aws_vpc.cluster.id

  route {
    cidr_block      = "0.0.0.0/0"
    nat_gateway_id  = each.value.id
  }

  tags = { Name = each.value.tags_all["Name"] }
}

resource "aws_route_table_association" "private_subnets" {
  for_each        = aws_subnet.private_subnets

  subnet_id       = each.value.id
  route_table_id  = aws_route_table.private_route_table[each.key].id
}

# ------- Security Groups -------
locals {
  default_sg_name = var.security_group_default_name != null ? var.security_group_default_name : "${var.cluster_prefix}-default"
}

resource "aws_security_group" "default_sg" {
  vpc_id       = aws_vpc.cluster.id
  name         = local.default_sg_name
  description  = var.security_group_default_desc != null ? var.security_group_default_desc : local.default_sg_name

  tags         = { Name = local.default_sg_name }

  # Intra-SG communication
  ingress {
      from_port = 0
      to_port   = 0
      protocol  = "all"
      self      = true
  }
  dynamic "ingress" {
    for_each = var.security_group_rules_ingress

    content {
      cidr_blocks = ingress.value.cidr
      from_port   = ingress.value.from_port
      to_port     = ingress.value.to_port
      protocol    = ingress.value.protocol
    }

  }

  egress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 0
    to_port     = 0
    protocol    = "all"
  }
}

output "vpc" {
  value = {
    cidr = aws_vpc.cluster.cidr_block
  }
}

output "subnets" {
  value = {
    public = ["TBD"]
    private = ["TBD"]
  }

  description = "Network infrastructure"
}
