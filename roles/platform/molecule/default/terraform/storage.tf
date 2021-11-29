module "s3_bucket" {
  source = "terraform-aws-modules/s3-bucket/aws"

  bucket        = var.s3_bucket_name
  acl           = "private"
  force_destroy = true
}

resource "aws_s3_bucket_object" "cml" {
  bucket       = module.s3_bucket.s3_bucket_id
  key          = "datasci/"
  content_type = "application/x-directory"
}

resource "aws_s3_bucket_object" "cde" {
  bucket       = module.s3_bucket.s3_bucket_id
  key          = "dataeng/"
  content_type = "application/x-directory"
}

resource "aws_s3_bucket_object" "log" {
  bucket       = module.s3_bucket.s3_bucket_id
  key          = "logs/"
  content_type = "application/x-directory"
}

resource "aws_s3_bucket_object" "data" {
  bucket       = module.s3_bucket.s3_bucket_id
  key          = "data/"
  content_type = "application/x-directory"
}

resource "aws_s3_bucket_object" "audit" {
  bucket       = module.s3_bucket.s3_bucket_id
  key          = "ranger/audit/"
  content_type = "application/x-directory"
}
