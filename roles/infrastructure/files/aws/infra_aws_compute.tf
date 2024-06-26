# ------- Dynamic Inventory VMs -------
resource "aws_instance" "cdp_dynamic_inventory_vm" {

  for_each      = {for idx, vm in var.dynamic_inventory_vms: idx => vm}

  vpc_security_group_ids      = [aws_security_group.cdp_default_sg.id]
  key_name                    = var.dynamic_inventory_public_key_id
  instance_type               = each.value.instance_type
  ami                         = each.value.ami
  ebs_optimized               = true

  # Volume / root_block_device
  root_block_device {
    delete_on_termination  = each.value.volume.delete_on_termination
    volume_size            = each.value.volume.volume_size
    volume_type            = each.value.volume.volume_type
  }

  # TODO: Review settng subnet_id to first public subnet (believe Ansible approach does this)
  subnet_id                   = aws_subnet.cdp_public_subnets[0].id

  associate_public_ip_address = true

  tags                        = merge(var.dynamic_inventory_tags,{Name = each.value.name})
}

# ------- Localised Utility VM Instance -------
resource "aws_instance" "cdp_utility_vms" {

  for_each                    = {for idx, vm in var.utility_vms: idx => vm}

  vpc_security_group_ids      = [aws_security_group.cdp_default_sg.id]
  key_name                    = var.utility_vm_public_key_id
  instance_type               = each.value.instance_type
  ami                         = each.value.ami
  ebs_optimized               = true

  subnet_id                   = aws_subnet.cdp_public_subnets[0].id

  # Volume / root_block_device
  root_block_device {
    # Need to cast from string (yes) to bool
    delete_on_termination  = each.value.volume.delete_on_termination
    volume_size            = each.value.volume.volume_size
    volume_type            = each.value.volume.volume_type
  }


  associate_public_ip_address = true

  tags                        = merge(var.utility_vm_tags,{Name = each.value.name})
}
