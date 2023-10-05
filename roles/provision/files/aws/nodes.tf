variable "nodes" {
  type                      = list(object({
    name                    = string
    ami_filters             = optional(map(list(string)), {
      name                  = [ "RHEL-8.6*" ]
      architecture          = [ "x86_64" ]
    })
    ami_owners              = optional(list(string),[ 309956199498 ])
    ami_user                = optional(string, "ec2-user")
    instance_type           = optional(string, "m5.xlarge")
    subnet_index            = optional(number, 0)
    elastic_ip              = optional(bool, false)
    private_ip              = optional(string, null)
    tags                    = optional(map(string))
    root_volume             = optional(object({
      delete_on_termination = optional(bool, true)
      volume_size           = optional(number, 30)
      volume_type           = optional(string, "gp2")
    }), {})
    volumes                 = optional(list(object({
      device_name           = string
      mount                 = string
      volume_size           = optional(number, 100)
      volume_type           = optional(string, "gp2")
      tags                  = optional(map(string), {})
    })), [])
  }))
  
  description = "List of infrastructure nodes"
  default     = []
}

# ------- Inventory Nodes -------
data "aws_ami" "images" {
  for_each = { for idx, node in var.nodes : idx => node }

  most_recent = true

  owners = each.value.ami_owners
  dynamic filter {
    for_each = each.value.ami_filters

    content {
      name   = filter.key
      values = filter.value
    }
  }
}

locals {
  existing_subnets = concat(values(aws_subnet.public_subnets), values(aws_subnet.private_subnets))

  volumes = flatten([
    for idx, node in var.nodes:
    [ 
      for node_vol in node.volumes:
        {
          node_index    = idx
          name          = node.name
          device        = node_vol.device_name
          mount         = node_vol.mount
          size          = node_vol.volume_size
          type          = node_vol.volume_type
          subnet_index  = node.subnet_index
        }
    ] 
  ])
}

resource "aws_instance" "inventory" {
  for_each                = {for idx, node in var.nodes: idx => node}

  # TODO Find security group(s) by name
  vpc_security_group_ids  = [aws_security_group.default_sg.id]
  key_name                = aws_key_pair.deployment_keypair.key_name
  instance_type           = each.value.instance_type
  ami                     = data.aws_ami.images[each.key].id
  ebs_optimized           = true

  # TODO Alternatively, render by looking up the subnet name
  subnet_id               = local.existing_subnets[each.value.subnet_index].id
  private_ip              = each.value.private_ip  

  root_block_device {
    delete_on_termination = each.value.root_volume.delete_on_termination
    volume_size           = each.value.root_volume.volume_size
    volume_type           = each.value.root_volume.volume_type
  }

  associate_public_ip_address = local.existing_subnets[each.value.subnet_index].map_public_ip_on_launch

  tags                     = merge(each.value.tags, { Name = each.value.name }) 

  lifecycle {
    precondition {
      condition     = length(var.public_subnets) > 0 || length(var.private_subnets) > 0
      error_message = "Unable to provision, no subnets available. You must define at least one subnet, public or private."
    } 
  }
}

resource "aws_eip" "inventory" {
  for_each = {for idx, node in var.nodes: idx => node if node.elastic_ip}

  instance = aws_instance.inventory[each.key].id
  vpc      = true
  tags     = {
    Name     = each.value.name
  }

  depends_on = [
    aws_internet_gateway.igw
  ]
}

resource "aws_ebs_volume" "inventory" {
  for_each    = {for idx, volume in local.volumes: idx => volume}

  availability_zone = local.existing_subnets[each.value.subnet_index].availability_zone
  size              = each.value.size
  type              = each.value.type
  tags              = {
    Name        = "${each.value.name}: ${each.value.device}"
    mount       = each.value.mount
  }
  #encrypted ...
}

resource "aws_volume_attachment" "inventory" {
  for_each    = {for idx, volume in local.volumes: idx => volume}

  device_name = each.value.device
  volume_id   = aws_ebs_volume.inventory[index(local.volumes, each.value)].id
  instance_id = aws_instance.inventory[each.value.node_index].id
}

# ------- Construct outputs for details of node and storage volumes -------
locals {
  # Details for all attached volumes
  attached_volumes = [
      for idx, volume in local.volumes: 
        {
            "vol_name" = aws_ebs_volume.inventory[index(local.volumes, volume)].tags["Name"]
            "vol_id"   = aws_volume_attachment.inventory[index(local.volumes, volume)].volume_id
            "instance" = aws_volume_attachment.inventory[index(local.volumes, volume)].instance_id
            "device"   = aws_volume_attachment.inventory[index(local.volumes, volume)].device_name
            "mount"    = aws_ebs_volume.inventory[index(local.volumes, volume)].tags["mount"]
        }
        if length(aws_ebs_volume.inventory) > 0
    ]
  
  # Attached volume details grouped by instance
  attached_volumes_by_instance = {
    for vol in local.attached_volumes :
      vol.instance => 
      {
        vol_name = vol.vol_name
        vol_id   = vol.vol_id
        device   = vol.device
        mount    = vol.mount
      }...
  }
}

output "nodes" {
  value = [
    for idx, v in aws_instance.inventory : 
      {
        # The top-level keys are used by 'add_host' within the provision role; 
        # use the nested 'metadata' tags within a 'module_defaults' declaration 
        # to add additional, ad-hoc 'add_host' variables
        "id"  = v.id
        "label" = v.tags["Name"]
        "hostname" = v.tags["hostname"]
        "instance_user" = var.nodes[idx].ami_user
        "ipv4" = lookup(aws_eip.inventory, idx, "") != "" ? aws_eip.inventory[idx].public_ip : v.public_ip != "" ? v.public_ip : v.private_ip
        "groups" = [ for g in coalesce(split(",", v.tags["groups"]), []) : trimspace(g) ]
        "metadata" = { for m, t in v.tags_all : m => t if !contains(["groups", "Name", "hostname"], m) }
        "storage_volumes" = lookup(local.attached_volumes_by_instance, v.id, [])
      }
  ]

  description = "Details of the provisioned inventory nodes."
}