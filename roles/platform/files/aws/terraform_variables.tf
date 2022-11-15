# ------- Global settings -------
variable "aws_profile" {
  type        = string
  description = "Profile for AWS cloud credentials"

  # Profile is default unless explicitly specified
  default = "default"
}

# Region
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

variable "env_prefix" {
  type        = string
  description = "Shorthand name for the environment. Used in resource descriptions"
}

variable "caller_account_id" {
  type        = string
  description = "ID of the Cloud Service Provider Account"
}

# ------- Policies -------
# Cross Account Policy (name and document)
variable "xaccount_policy_name" {
  type        = string
  description = "Cross Account Policy name"

}

variable "xaccount_account_policy_doc" {
  type        = string
  description = "Location of cross acount policy document"

}
# CDP IDBroker Assume Role policy
variable "idbroker_policy_name" {
  type        = string
  description = "IDBroker Policy name"

}

# CDP Data Access Policies - Log
variable "log_data_access_policy_name" {
  type        = string
  description = "Log Data Access Policy Name"

}

variable "log_data_access_policy_doc" {
  type        = string
  description = "Location of Log Data Access Policy"

}

# CDP Data Access Policies - ranger_audit_s3
variable "ranger_audit_s3_policy_name" {
  type        = string
  description = "Ranger S3 Audit Data Access Policy Name"

}

variable "ranger_audit_s3_policy_doc" {
  type        = string
  description = "Location of Ranger S3 Audit Data Access Policy"

}

# CDP Data Access Policies - datalake_admin_s3 
variable "datalake_admin_s3_policy_name" {
  type        = string
  description = "Datalake Admin S3 Data Access Policy Name"

}

variable "datalake_admin_s3_policy_doc" {
  type        = string
  description = "Location of Datalake Admin S3 Data Access Policy"

}

# CDP Data Access Policies - bucket_access
variable "bucket_access_policy_name" {
  type        = string
  description = "Bucket Access Data Access Policy Name"

}

variable "bucket_access_policy_doc" {
  type        = string
  description = "Bucket Access Data Access Policy"

}

# ------- Policies -------
# Cross Account Role (name and id)
variable "xaccount_role_name" {
  type        = string
  description = "Cross account Assume role Name"
}

variable "xaccount_account_id" {
  type        = string
  description = "Account ID of the cross account"
}

variable "xaccount_external_id" {
  type        = string
  description = "External ID of the cross account"
}

# IDBroker service role
variable "idbroker_role_name" {
  type        = string
  description = "IDBroker service role Name"
}

# Log service role
variable "log_role_name" {
  type        = string
  description = "Log service role Name"
}

# CDP Datalake Admin role
variable "datalake_admin_role_name" {
  type        = string
  description = "Datalake Admin role Name"
}

# CDP Ranger Audit role
variable "ranger_audit_role_name" {
  type        = string
  description = "Ranger Audit role Name"
}
