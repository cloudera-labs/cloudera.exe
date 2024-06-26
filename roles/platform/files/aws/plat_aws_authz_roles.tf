# ------- Cross Account Role -------
# First create the assume role policy document
data "aws_iam_policy_document" "cdp_xaccount_role_policy_doc" {
  version       = "2012-10-17"

  statement {
    actions = ["sts:AssumeRole"]
    effect  = "Allow"

    principals {
      type          = "AWS"
      identifiers   = ["arn:aws:iam::${var.xaccount_account_id}:root"]
    }

    condition {
      test     = "StringEquals"
      variable = "sts:ExternalId"

      values   = [var.xaccount_external_id]
    }
  }
}

# Create the IAM role that uses the above assume_role_policy document
resource "aws_iam_role" "cdp_xaccount_role" {
    name                = var.xaccount_role_name
    description         = "CDP Cross Account role for ${var.env_prefix}"

    assume_role_policy  = data.aws_iam_policy_document.cdp_xaccount_role_policy_doc.json

    tags                = merge(var.env_tags,{Name = var.xaccount_role_name})
}

# Attach AWS Cross Account Policy to Cross Account Role
resource "aws_iam_role_policy_attachment" "cdp_xaccount_role_attach" {
  role       = aws_iam_role.cdp_xaccount_role.name
  policy_arn = aws_iam_policy.cdp_xaccount_policy.arn
}

# ------- AWS Service Roles - CDP IDBroker -------
# First create the Assume role policy document
data "aws_iam_policy_document" "cdp_idbroker_role_policy_doc" {
  version       = "2012-10-17"

  statement {
    actions = ["sts:AssumeRole"]
    effect  = "Allow"

    principals {
      type          = "Service"
      identifiers   = ["ec2.amazonaws.com"]
    }
  }
}

# Create the IAM role that uses the above assume_role_policy document
resource "aws_iam_role" "cdp_idbroker_role" {
    name                = var.idbroker_role_name
    description         = "CDP IDBroker role for ${var.env_prefix}"

    assume_role_policy  = data.aws_iam_policy_document.cdp_idbroker_role_policy_doc.json

    tags                = merge(var.env_tags,{Name = var.idbroker_role_name})
}

# Create an instance profile for the iam_role
resource "aws_iam_instance_profile" "cdp_idbroker_role_instance_profile" {
  name = var.idbroker_role_name
  role = aws_iam_role.cdp_idbroker_role.name
}

# Attach CDP IDBroker Assume Policy to the Role
resource "aws_iam_role_policy_attachment" "cdp_idbroker_role_attach1" {
  role       = aws_iam_role.cdp_idbroker_role.name
  policy_arn = aws_iam_policy.cdp_idbroker_policy.arn
}

# Attach AWS Log Location Policy to the Role
resource "aws_iam_role_policy_attachment" "cdp_idbroker_role_attach2" {

  role       = aws_iam_role.cdp_idbroker_role.name
  policy_arn = aws_iam_policy.cdp_log_data_access_policy.arn
}


# ------- AWS Service Roles - CDP Log -------
# First create the Assume role policy document
data "aws_iam_policy_document" "cdp_log_role_policy_doc" {
  version       = "2012-10-17"

  statement {
    actions = ["sts:AssumeRole"]
    effect  = "Allow"

    principals {
      type          = "Service"
      identifiers   = ["ec2.amazonaws.com"]
    }
  }
}

# Create the IAM role that uses the above assume_role_policy document
resource "aws_iam_role" "cdp_log_role" {
    name                = var.log_role_name
    description         = "CDP Log role for ${var.env_prefix}"

    assume_role_policy  = data.aws_iam_policy_document.cdp_log_role_policy_doc.json

    tags                = merge(var.env_tags,{Name = var.log_role_name})
}

# Create an instance profile for the iam_role
resource "aws_iam_instance_profile" "cdp_log_role_instance_profile" {
  name = var.log_role_name
  role = aws_iam_role.cdp_log_role.name
}

# Attach AWS Log Location Policy to the Role
resource "aws_iam_role_policy_attachment" "cdp_log_role_attach1" {

  role       = aws_iam_role.cdp_log_role.name
  policy_arn = aws_iam_policy.cdp_log_data_access_policy.arn
}

# Attach AWS Bucket Access Policy to the Role
resource "aws_iam_role_policy_attachment" "cdp_log_role_attach2" {

  role       = aws_iam_role.cdp_log_role.name
  policy_arn = aws_iam_policy.cdp_bucket_data_access_policy.arn
}

# ------- AWS Data Access Roles - CDP Datalake Admin -------
# First create the Assume role policy document
data "aws_iam_policy_document" "cdp_datalake_admin_role_policy_doc" {
  version       = "2012-10-17"

  statement {
    actions = ["sts:AssumeRole"]
    effect  = "Allow"

    principals {
      type          = "AWS"
      identifiers   = ["arn:aws:iam::${var.caller_account_id}:role/${var.idbroker_role_name}"]
    }
  }
}

# Create the IAM role that uses the above assume_role_policy document
resource "aws_iam_role" "cdp_datalake_admin_role" {
    name                = var.datalake_admin_role_name
    description         = "CDP Datalake Admin role for ${var.env_prefix}"

    assume_role_policy  = data.aws_iam_policy_document.cdp_datalake_admin_role_policy_doc.json

    tags                = merge(var.env_tags,{Name = var.datalake_admin_role_name})
}

# Create an instance profile for the iam_role
resource "aws_iam_instance_profile" "cdp_datalake_admin_role_instance_profile" {
  name = var.datalake_admin_role_name
  role = aws_iam_role.cdp_datalake_admin_role.name
}

# Attach AWS Datalake Admin S3 Policy to the Role
resource "aws_iam_role_policy_attachment" "cdp_datalake_admin_role_attach1" {

  role       = aws_iam_role.cdp_datalake_admin_role.name
  policy_arn = aws_iam_policy.cdp_datalake_admin_s3_data_access_policy.arn
}

# Attach AWS Bucket Access Policy to the Role
resource "aws_iam_role_policy_attachment" "cdp_datalake_admin_role_attach2" {

  role       = aws_iam_role.cdp_datalake_admin_role.name
  policy_arn = aws_iam_policy.cdp_bucket_data_access_policy.arn
}

# ------- AWS Data Access Roles - CDP Ranger Audit -------
# First create the Assume role policy document
data "aws_iam_policy_document" "cdp_ranger_audit_role_policy_doc" {
  version       = "2012-10-17"

  statement {
    actions = ["sts:AssumeRole"]
    effect  = "Allow"

    principals {
      type          = "AWS"
      identifiers   = ["arn:aws:iam::${var.caller_account_id}:role/${var.idbroker_role_name}"]
    }
  }
}

# Create the IAM role that uses the above assume_role_policy document
resource "aws_iam_role" "cdp_ranger_audit_role" {
    name                = var.ranger_audit_role_name
    description         = "CDP Ranger Audit role for ${var.env_prefix}"

    assume_role_policy  = data.aws_iam_policy_document.cdp_ranger_audit_role_policy_doc.json

    tags                = merge(var.env_tags,{Name = var.ranger_audit_role_name})
}

# Create an instance profile for the iam_role
resource "aws_iam_instance_profile" "cdp_ranger_audit_role_instance_profile" {
  name = var.ranger_audit_role_name
  role = aws_iam_role.cdp_ranger_audit_role.name
}

# Attach AWS Ranger Audit S3 Policy to the Role
resource "aws_iam_role_policy_attachment" "cdp_ranger_audit_role_attach1" {

  role       = aws_iam_role.cdp_ranger_audit_role.name
  policy_arn = aws_iam_policy.cdp_ranger_audit_s3_data_access_policy.arn
}

# Attach AWS Bucket Access Policy to the Role
resource "aws_iam_role_policy_attachment" "cdp_ranger_audit_role_attach2" {

  role       = aws_iam_role.cdp_ranger_audit_role.name
  policy_arn = aws_iam_policy.cdp_bucket_data_access_policy.arn
}
