# mount

Create, format, and mount a storage volume.

This role automates the process of creating, formatting, and mounting a logical volume management (LVM) partition on a specified device. It handles the installation of the `LVM2` operating system package if it's not already present.

The role will:
- Install the `lvm2` package.
- Identify the specified block device(s).
- Create a Physical Volume (PV) on the device.
- Create a Volume Group (VG) on the PV.
- Create a Logical Volume (LV) within the VG.
- Format the Logical Volume with the specified or default filesystem type (`xfs` by default).
- Mount the Logical Volume to the specified mount path.
- Configure `fstab` for persistent mounting across reboots.
- Optionally, for `aws` provider, it will handle NVMe device name mapping (e.g., `/dev/nvme0n1` to `/dev/xvda`).

## Requirements

- Target host must have unpartitioned, unformatted block devices available.
- For `aws` provider, instances must have EBS volumes attached.

## Dependencies

None.

## Role Variables

| Parameter           | Type             | Default Value | Required | Description                                                                                                                              |
|---------------------|------------------|---------------|----------|------------------------------------------------------------------------------------------------------------------------------------------|
| `mount_volumes`     | `list` of `dict` | -             | `true`   | A list of dictionaries, where each dictionary defines a storage volume to be created, formatted, and mounted.                            |
| `device` | `str`            | -             | `true`   | The identifier of the block device (e.g., `/dev/sdb`, `/dev/nvme1n1`).                                                                   |
| `mount`  | `path`           | -             | `true`   | The absolute path on the host where the volume should be mounted (e.g., `/mnt/data`, `/opt/app`).                                      |
| `fstype` | `str`            | `mount_fstype`| `false`  | The filesystem type to format the partition with (e.g., `xfs`, `ext4`). If not specified, the value of `mount_fstype` will be used.   |
| `mount_fstype`      | `str`            | `xfs`         | `false`  | The default filesystem type to format partitions with if not specified per volume in `mount_volumes`.                                    |
| `mount_provider`    | `str`            | -             | `false`  | The infrastructure provider where the volume is being provisioned. If set to `aws`, EBS NVMe volume attachments will be mapped correctly. *Choices*: `aws` |

## Examples

Basic usage to create and mount a single volume using the default `xfs` filesystem:

```yaml
- name: Create and mount a data volume with default filesystem
  ansible.builtin.import_role:
    name: cloudera.exe.mount
  vars:
    mount_volumes:
      - device: "/dev/sdb"
        mount: "/mnt/data"
    # mount_fstype will default to 'xfs'

- name: Provision multiple storage volumes with a custom default filesystem
  ansible.builtin.import_role:
    name: cloudera.exe.mount
  vars:
    mount_fstype: "ext4" # All volumes will be formatted with ext4 unless overridden
    mount_volumes:
      - device: "/dev/sdb"
        mount: "/mnt/data1"
      - device: "/dev/sdc"
        mount: "/var/lib/app_data"

- name: Provision volumes with mixed filesystem types
  ansible.builtin.import_role:
    name: cloudera.exe.mount
  vars:
    mount_fstype: "xfs" # Global default, but can be overridden
    mount_volumes:
      - device: "/dev/sdb"
        mount: "/mnt/data_xfs"
        fstype: "xfs" # Explicitly xfs, matches default
      - device: "/dev/sdc"
        mount: "/mnt/data_ext4"
        fstype: "ext4" # Explicitly ext4, overrides global default

- name: Create and mount volumes on an AWS instance with specific filesystems
  ansible.builtin.import_role:
    name: cloudera.exe.mount
  vars:
    mount_provider: "aws"
    mount_volumes:
      - device: "/dev/nvme0n1" # Role will map this to the correct /dev/xvd*
        mount: "/mnt/ebs_volume_1"
        fstype: "xfs"
      - device: "/dev/nvme1n1"
        mount: "/var/log/application"
        fstype: "ext4"
```

## License

```
Copyright 2025 Cloudera, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
