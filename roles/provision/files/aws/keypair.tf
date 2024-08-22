variable "ssh_keypair_name" {
  type = string
  description = "AWS SSH key pair name"
  validation {
    condition     = length(var.ssh_keypair_name) > 4
    error_message = "The SSH key pair name must be greater than 4 characters."
  }
}

variable "ssh_keypair_public_key_text" {
  type = string
  description = "AWS SSH key pair public key text"
  validation {
    condition     = length(var.ssh_keypair_public_key_text) > 0
    error_message = "The SSH key pair public key text must not be empty."
  }
}

resource "aws_key_pair" "deployment_keypair" {
  key_name   = var.ssh_keypair_name
  public_key = var.ssh_keypair_public_key_text
}

output "ssh_keypair" {
  value = {
    name = aws_key_pair.deployment_keypair.key_name
    public_key = var.ssh_keypair_public_key_text
    fingerprint = aws_key_pair.deployment_keypair.fingerprint
  }
  description = "Deployment SSH keypair"
}
