# Copyright 2024 Cloudera, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.70.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.6.3"
    }
  }
}

locals {
  resource_name = "molecule-${random_string.molecule.id}"
}

provider "aws" {
  default_tags {
    tags = {
      Name             = "${local.resource_name}"
      project          = "Molecule testing"
      terraform-run-id = "${random_string.molecule.id}"
    }
  }
}

resource "random_string" "molecule" {
  length  = 6
  special = false
  numeric = false
  upper   = false
}

resource "aws_vpc" "molecule" {
  enable_dns_support = true
  cidr_block         = "10.0.0.0/24"
}

resource "aws_internet_gateway" "molecule" {
  vpc_id = aws_vpc.molecule.id
}

resource "aws_default_route_table" "molecule" {
  default_route_table_id = aws_vpc.molecule.default_route_table_id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.molecule.id
  }
}

resource "aws_subnet" "molecule" {
  vpc_id = aws_vpc.molecule.id

  cidr_block              = "10.0.0.0/28"
  map_public_ip_on_launch = true
}

resource "aws_route_table_association" "molecule" {
  subnet_id      = aws_subnet.molecule.id
  route_table_id = aws_vpc.molecule.default_route_table_id
}

resource "aws_security_group" "molecule" {
  name        = local.resource_name
  description = "Allow all traffic within security group"
  vpc_id      = aws_vpc.molecule.id
}

resource "aws_vpc_security_group_ingress_rule" "allow_ssh" {
  security_group_id = aws_security_group.molecule.id
  description       = "Allow inbound SSH traffic"
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
  tags = {
    Name             = "${local.resource_name}"
    project          = "Molecule testing"
    terraform-run-id = "${random_string.molecule.id}"
  }

}

resource "aws_vpc_security_group_ingress_rule" "allow_intra" {
  security_group_id            = aws_security_group.molecule.id
  description                  = "Allow all intra-security group traffic"
  referenced_security_group_id = aws_security_group.molecule.id
  ip_protocol                  = -1
  tags = {
    Name             = "${local.resource_name}"
    project          = "Molecule testing"
    terraform-run-id = "${random_string.molecule.id}"
  }
}

resource "aws_vpc_security_group_egress_rule" "allow_all_traffic_ipv4" {
  security_group_id = aws_security_group.molecule.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1" # semantically equivalent to all ports
  tags = {
    Name             = "${local.resource_name}"
    project          = "Molecule testing"
    terraform-run-id = "${random_string.molecule.id}"
  }
}
