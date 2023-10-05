terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

variable "region" {
  type        = string
  description = "AWS Region"
}

variable "env_tags" {
  type        = map(string)
  description = "Tags applied to provisioned resources"

  default     = {
    comment = "Created with Terraform via cloudera.exe.provision"
  }
}

provider "aws" {
  region = var.region
  default_tags {
    tags = var.env_tags
  }
}
