# prereq_kernel

Update kernel parameters

This role updates and applies specified kernel parameters using `sysctl`. It is designed to configure a host for performance-critical applications by tuning memory management settings like `swappiness` and `overcommit_memory`, and by disabling IPv6 functionality for all network interfaces by default. The changes are applied both for the current running system and for future reboots.

The role will:
- Modify kernel parameters via `sysctl`.
- Ensure the changes are made persistent by writing them to a configuration file (e.g., in `/etc/sysctl.d/`).
- By default, it will configure memory management settings and disable IPv6.

# Requirements

- Root or `sudo` privileges are required on the target host to update kernel parameters.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `prereq_kernel__kernel_flags` | `dict` | `False` | `{"vm.swappiness": 1, "vm.overcommit_memory": 1, "net.ipv6.conf.all.disable_ipv6": 1, "net.ipv6.conf.default.disable_ipv6": 1, "net.ipv6.conf.lo.disable_ipv6": 1}` | A dictionary of kernel parameters and their values to configure with `sysctl`. The role will apply the default values unless overridden. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Update kernel parameters with default values
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_kernel
      # This will set vm.swappiness, overcommit_memory, and disable IPv6 as per the default values.

    - name: Override default swappiness and enable IPv6 on the loopback interface
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_kernel
      vars:
        prereq_kernel__kernel_flags:
          vm.swappiness: 10
          net.ipv6.conf.lo.disable_ipv6: 0 # Enable IPv6 on loopback
```

# License

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
