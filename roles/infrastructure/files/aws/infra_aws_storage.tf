# ------- S3 Buckets -------
# NOTE: Variables cannot be used with the prevent_destroy lifecycle policy
#       To overcome this limitation and still support infra__teardown_deletes_data = False
#       we create two similar resource using a conditional on the for_each.
#       Resource cdp_storage_delete_data is created when teardown_deletes_data = True
#       Resource cdp_storage_retain_data is created when teardown_deletes_data = False
#       References:
#        * https://github.com/hashicorp/terraform/issues/22544#issuecomment-981575058
#        * https://discuss.hashicorp.com/t/conditionally-create-resources-when-a-for-each-loop-is-involved/20841/9

resource "aws_s3_bucket" "cdp_storage_delete_data" {
  for_each          = var.teardown_deletes_data ? toset(var.storage_locations[*].bucket) : []

  bucket            = each.value
  tags              = merge(var.env_tags,{Name = each.value})

  # Purge storage locations during teardown?
  force_destroy     = true
  lifecycle {
    # A Terraform destroy of this resource will result in an error message.
    prevent_destroy = false
  }
}
resource "aws_s3_bucket" "cdp_storage_retain_data" {
  for_each         = var.teardown_deletes_data ? [] : toset(var.storage_locations[*].bucket)

  bucket            = each.value
  tags              = merge(var.env_tags,{Name = each.value})

  # Purge storage locations during teardown?
  force_destroy     = false
  lifecycle {
    # A Terraform destroy of this resource will result in an error message.
    prevent_destroy = true
  }
}

# Separate bucket acl resource definition
resource "aws_s3_bucket_acl" "cdp_storage_acl" {
  for_each = var.teardown_deletes_data ? aws_s3_bucket.cdp_storage_delete_data : aws_s3_bucket.cdp_storage_retain_data

  bucket   = each.value.id
  acl      = "private"
}

# ------- AWS Buckets directory structures -------
resource "aws_s3_object" "cdp_storage_object" {

    for_each      = {for idx, object in var.storage_locations: idx => object}
    
    # Bucket is either from 'cdp_storage_delete_data' or 'cdp_storage_retain_data' resource depending on teardown_deletes_data'
    bucket        = var.teardown_deletes_data ? aws_s3_bucket.cdp_storage_delete_data[each.value.bucket].id : aws_s3_bucket.cdp_storage_retain_data[each.value.bucket].id

    key           = each.value.object    
    content_type  = "application/x-directory"
}

# ------- Download Mirror Bucket -------
# TODO: Don't fail if Mirror Bucket already exists from non-Terraform code.
# resource "aws_s3_bucket" "cdp_utility_bucket" {
#   bucket        = var.utility_bucket
#   acl           = "private"
#   force_destroy = true

#   tags          = merge(var.env_tags,{Name = var.utility_bucket})
# }
