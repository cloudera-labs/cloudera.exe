# ------- VPC -------
# Create the VPC's
resource "aws_vpc" "cdp_vpc" {
  cidr_block           = var.vpc_cidr
  tags = merge(var.env_tags,{Name = var.vpc_name})

  instance_tenancy     = "default"
  enable_dns_support   = true
  enable_dns_hostnames = true
}

# ------- AWS Public Network infrastructure -------
# Internet Gateway
resource "aws_internet_gateway" "cdp_igw" {
  vpc_id = aws_vpc.cdp_vpc.id
  tags   = merge(var.env_tags,{Name = var.igw_name})
}

# AWS VPC Public Subnets
resource "aws_subnet" "cdp_public_subnets" {
    for_each                = {for idx, subnet in var.public_subnets: idx => subnet}

    vpc_id                  = aws_vpc.cdp_vpc.id
    cidr_block              = each.value.cidr
    map_public_ip_on_launch = true
    availability_zone       = each.value.az
    tags                    = merge(var.env_tags,each.value.tags)
}

# Public Route Table
resource "aws_default_route_table" "cdp_public_route_table" {
  default_route_table_id = aws_vpc.cdp_vpc.default_route_table_id

  route {
    cidr_block           = "0.0.0.0/0"
    gateway_id           = aws_internet_gateway.cdp_igw.id
  }

  tags                   = merge(var.env_tags,{Name = var.public_route_table_name})

}

# Associate the Public Route Table with the Public Subnets
resource "aws_route_table_association" "cdp_public_subnets" {

  for_each        = aws_subnet.cdp_public_subnets

  subnet_id       = each.value.id
  route_table_id  = aws_vpc.cdp_vpc.default_route_table_id
}

# ------- AWS Private Networking infrastructure -------

# AWS VPC Private Subnets
resource "aws_subnet" "cdp_private_subnets" {
    for_each                = {for idx, subnet in var.private_subnets: idx => subnet}

    vpc_id                  = aws_vpc.cdp_vpc.id
    cidr_block              = each.value.cidr
    map_public_ip_on_launch = false
    availability_zone       = each.value.az
    tags                    = merge(var.env_tags,each.value.tags)
}

# Private Route Table for the AWS VPC
#  - Not implemeted in Terraform because of "when: no" in Ansible

# Elastic IP for each NAT gateway
resource "aws_eip" "cdp_nat_gateway_eip" {

  for_each  =  {for idx, subnet in var.public_subnets: idx => subnet}

  vpc       = true
  tags      = merge(var.env_tags,{Name = format("%s-%s-%02d", var.nat_gateway_name, "eip", index(var.public_subnets, each.value)+1)})
}

#  Network Gateways (NAT)
resource "aws_nat_gateway" "cdp_nat_gateway" {

  # for_each          = { for s in aws_subnet.cdp_public_subnets : s.id => s }
  count             = length(aws_subnet.cdp_public_subnets)

  subnet_id         = aws_subnet.cdp_public_subnets[count.index].id
  allocation_id     = aws_eip.cdp_nat_gateway_eip[count.index].id
  connectivity_type = "public"

  tags              = merge(var.env_tags,{Name = format("%s-%02d", var.nat_gateway_name, count.index)})
  # tags               = merge(var.env_tags,{Name = format("%s-%s-%02d", var.nat_gateway_name, "eip", index(aws_subnet.cdp_public_subnets, each.value)+1)})
}


# Private Route Tables
resource "aws_route_table" "cdp_private_route_table" {
  for_each = {for idx, subnet in var.private_subnets: idx => subnet}

  vpc_id = aws_vpc.cdp_vpc.id

  tags   = merge(var.env_tags,{Name = format("%s-%02d", var.private_route_table_name, index(var.private_subnets, each.value))})

  route {
    cidr_block     = "0.0.0.0/0"
    #nat_gateway_id = aws_nat_gateway.cdp_nat_gateway[0].id

    nat_gateway_id = aws_nat_gateway.cdp_nat_gateway[(index(var.private_subnets, each.value) % length(aws_nat_gateway.cdp_nat_gateway))].id

  }
}

# Associate the Private Route Tables with the Private Subnets
resource "aws_route_table_association" "cdp_private_subnets" {

  count = length(aws_subnet.cdp_private_subnets)

  subnet_id       = aws_subnet.cdp_private_subnets[count.index].id
  route_table_id = aws_route_table.cdp_private_route_table[count.index].id
}

# ------- Security Groups -------
# Default SG
resource "aws_security_group" "cdp_default_sg" {
  vpc_id       = aws_vpc.cdp_vpc.id
  name         = var.security_group_default_name
  description  = var.security_group_default_name

  tags         = merge(var.env_tags,{Name = var.security_group_default_name})

  # Create self reference ingress rule to allow
  # communication among resources in the security group.
  ingress {
      from_port = 0
      to_port   = 0
      protocol  = "all"
      self      = true
  }

  # Dynamic Block to create security group rule from var.sg_ingress
  dynamic "ingress" {
    for_each = var.security_group_rules_ingress

    content {
      cidr_blocks = ingress.value.cidr
      from_port  = ingress.value.from_port
      to_port    = ingress.value.to_port
      protocol   = ingress.value.protocol
    }

  }

  # Terraform removes the default ALLOW ALL egress. Let's recreate this
  egress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 0
    to_port     = 0
    protocol    = "all"
  }
}

# Knox SG
resource "aws_security_group" "cdp_knox_sg" {
  vpc_id       = aws_vpc.cdp_vpc.id
  name         = var.security_group_knox_name
  description  = var.security_group_knox_name

  tags         = merge(var.env_tags,{Name = var.security_group_knox_name})

  # Create self reference ingress rule to allow
  # communication among resources in the security group.
  ingress {
      from_port = 0
      to_port   = 0
      protocol  = "all"
      self      = true
  }

  # Dynamic Block to create security group rule from var.sg_ingress
  dynamic "ingress" {
    for_each = var.security_group_rules_ingress

    content {
      cidr_blocks = ingress.value.cidr
      from_port  = ingress.value.from_port
      to_port    = ingress.value.to_port
      protocol   = ingress.value.protocol
    }

  }

  # Terraform removes the default ALLOW ALL egress. Let's recreate this
  egress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 0
    to_port     = 0
    protocol    = "all"
  }
}
