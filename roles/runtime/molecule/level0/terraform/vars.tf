variable "name_prefix" {
  type = string
  description = "An unique identifer"
}

variable "region" {
  type = string
  description = "AWS region name"
}

variable "vpc_name" {
  type = string
  description = "AWS VPC name"
}

variable "sg_names" {
  type = object({
    knox = string
    default = string
  })
  description = "AWS Security Group names for Knox and Default"
}

variable "tags" {
  type = map(string)
  description = "Key-Value pairs of tags applied to AWS assets"
}

variable "extra_rules" {
  type = list(map(any))
  description = "A list of maps representing the additional rules added to the Knox and Default security groups"
  default = []
}

variable "s3_bucket_name" {
  type = string
  description = "AWS S3 bucket name for logs, audit, and data (all-in-one)"
}