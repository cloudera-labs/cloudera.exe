# ------- Global settings -------
variable "aws_profile" {
  type        = string
  description = "Profile for AWS cloud credentials"

  # Profile is default unless explicitly specified
  default = "default"
}

variable "region" {
  type        = string
  description = "Region which Cloud resources will be created"
}

variable "env_tags" {
  type        = map
  description = "Tags applied to provised resources"

  default     = {
      comment = "Created with Terraform by cloudera-deploy"
  }
}

# ------- Network Resources -------
variable "vpc_name" {
  type        = string
  description = "VPC name"
}

variable "vpc_cidr" {
  type        = string
  description = "VPC CIDR Block"
}

variable "igw_name" {
  type        = string
  description = "Internet Gateway"
}

# Public Network infrastructure
variable "public_subnets" {
  type       = list(object({
    name     = string
    cidr     = string
    az       = string
    tags     = map(string)
  }))
  
  description = "List of Public Subnets"
  default    = []
}

variable "public_route_table_name" {
  type        = string
  description = "Public Route Table Name"
}

# Private Network infrastructure
variable "private_subnets" {
  type       = list(object({
    name     = string
    cidr     = string
    az       = string
    tags     = map(string)
  }))

  description = "List of Private Subnets"
  default    = []
}

variable "nat_gateway_name" {
  type        = string
  
  description = "Nat Gateway"
  default     = "CDP_NAT_Gateway"
}

variable "private_route_table_name" {
  type        = string
  
  description = "Private Route Table"
  default     = "CDP_Private_RT"
}

# Security Groups
variable "security_group_default_name" {
  type        = string
  
  description = "Default Security Group for CDP environment"
}

variable "security_group_knox_name" {
  type        = string
  
  description = "Knox Security Group for CDP environment"
}

variable "security_group_rules_ingress" {
  type       = list(object({
    cidr       = list(string)
    from_port  = string
    to_port    = string
    protocol   = string
  }))
  
  description = "Ingress rules for Security Group"
  default    = []
}

# ------- Storage Resources -------
variable "storage_locations" {
  type       = list(object({
    bucket     = string
    object     = string
  }))

  description = "Storage locations for CDP environment"
}

variable "teardown_deletes_data" {
  type        = bool

  description = "Purge storage locations during teardown"
}

variable "utility_bucket" {
  type        = string

  description = "Utility bucket used as a mirror for downloaded PvC parcels"
}

# ------- Compute Resources -------
# Dynamic Inventory VMs
variable "dynamic_inventory_vms" {
  type       = list(object({
    name          = string
    instance_type = string
    ami           = string
    volume        = object({
      delete_on_termination = bool
      volume_size           = string
      volume_type           = string
    })
  }))

  description = "List of VMs to be created as part of dynamic inventory"

  default = []
}

variable "dynamic_inventory_tags" {
  type        = map
  description = "Tags applied to provisioned dynamic inventory resources"

  default     = {}
}

variable "dynamic_inventory_public_key_id" {
  type        = string
  
  description = "Name of the Public SSH key for the dynamic inventory VMs"
}

# Localised Utility VM
variable "utility_vms" {
  type       = list(object({
    name          = string
    instance_type = string
    ami           = string
    volume        = object({
      delete_on_termination = bool
      volume_size           = string
      volume_type           = string
    })
  }))

  description = "Utility VMs used for hosting parcel mirror"

  default = []
}

variable "utility_vm_tags" {
  type        = map
  description = "Tags applied to Utility VM"

  default     = {}
}

variable "utility_vm_public_key_id" {
  type        = string
  
  description = "Name of the Public SSH key for the Utility VM"

  default     = ""
}
