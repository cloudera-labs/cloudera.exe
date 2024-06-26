# ------- AWS Cross Account Policy -------
# The policy here is a dict variable so we'll use the variable
# directly in the aws_iam_policy resource.
resource "aws_iam_policy" "cdp_xaccount_policy" {
    name        = var.xaccount_policy_name
    description = "CDP Cross Account policy for ${var.env_prefix}"

    tags        = merge(var.env_tags,{Name = var.xaccount_policy_name})

    policy      = var.xaccount_account_policy_doc
}

# ------- CDP IDBroker Assume Role policy -------
# First create the assume role policy document
data "aws_iam_policy_document" "cdp_idbroker_policy_doc" {
  version       = "2012-10-17"

  statement {
    sid         = "VisualEditor0"
    actions     = ["sts:AssumeRole"]
    effect      = "Allow"
    resources   = ["*"]
  }
}

# Then create the policy using the document
resource "aws_iam_policy" "cdp_idbroker_policy" {
    name        = var.idbroker_policy_name
    description = "CDP IDBroker Assume Role policy for ${var.env_prefix}"

    tags        = merge(var.env_tags,{Name = var.idbroker_policy_name})

    policy      = data.aws_iam_policy_document.cdp_idbroker_policy_doc.json
}

# ------- CDP Data Access Policies - Log -------
resource "aws_iam_policy" "cdp_log_data_access_policy" {
    name        = var.log_data_access_policy_name
    description = "CDP Log Location Access policy for ${var.env_prefix}"

    tags        = merge(var.env_tags,{Name = var.log_data_access_policy_name})

    policy      = file(var.log_data_access_policy_doc)
}

# ------- CDP Data Access Policies - ranger_audit_s3 -------
resource "aws_iam_policy" "cdp_ranger_audit_s3_data_access_policy" {
    name        = var.ranger_audit_s3_policy_name
    description = "CDP Ranger Audit S3 Access policy for ${var.env_prefix}"

    tags        = merge(var.env_tags,{Name = var.ranger_audit_s3_policy_name})

    policy      = file(var.ranger_audit_s3_policy_doc)
}

# ------- CDP Data Access Policies - datalake_admin_s3 -------
resource "aws_iam_policy" "cdp_datalake_admin_s3_data_access_policy" {
    name        = var.datalake_admin_s3_policy_name
    description = "CDP Datalake Admin S3 Access policy for ${var.env_prefix}"

    tags        = merge(var.env_tags,{Name = var.datalake_admin_s3_policy_name})

    policy      = file(var.datalake_admin_s3_policy_doc)
}

# ------- CDP Data Access Policies - bucket_access -------
resource "aws_iam_policy" "cdp_bucket_data_access_policy" {
    name        = var.bucket_access_policy_name
    description = "CDP Bucket S3 Access policy for ${var.env_prefix}"

    tags        = merge(var.env_tags,{Name = var.bucket_access_policy_name})

    policy      = file(var.bucket_access_policy_doc)
}
