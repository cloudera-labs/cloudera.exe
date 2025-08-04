# prereq_selinux

Manage SELinux policy enforcement

This role is designed to manage the enforcement state and policy of SELinux on a host. It can set SELinux to `enforcing`, `permissive`, or `disabled` mode. The role ensures that the necessary packages for SELinux management are installed, but it assumes that SELinux itself is already part of the system's kernel.

The role will:
- Install packages required for SELinux administration (e.g., `selinux-policy`, `libselinux-python`).
- Configure the SELinux state (`selinux_state`) to `disabled`, `enforcing`, or `permissive`.
- Set the SELinux policy (`selinux_policy`), with OS-specific defaults if not specified.
- Apply the changes to the system to take effect immediately and persist across reboots.

# Requirements

- Root or `sudo` privileges are required on the target host to manage SELinux.
- The system kernel must have SELinux support compiled in and enabled for the role to have its full effect.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `selinux_state` | `str` | `False` | `permissive` | The desired enforcement mode for SELinux. `disabled` completely turns off SELinux, `permissive` logs but does not enforce policy, and `enforcing` enforces policy and logs denials. Valid choices are `disabled`, `enforcing`, `permissive`. |
| `selinux_policy` | `str` | `False` | - | The policy to adopt for SELinux. On Red Hat-based distributions, the default is `targeted`. On Ubuntu-based distributions, the default is `default`. This variable should be set to match the desired policy file name. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Set SELinux to permissive mode
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_selinux
      # This will install SELinux management tools and set the state to permissive by default.

    - name: Set SELinux to enforcing mode with the targeted policy
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_selinux
      vars:
        selinux_state: enforcing
        selinux_policy: targeted

    - name: Disable SELinux entirely
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_selinux
      vars:
        selinux_state: disabled
```

# License

```
Copyright 2024 Cloudera, Inc.

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
