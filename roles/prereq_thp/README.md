# prereq_thp

Disable Transparent Huge Pages

This role disables Transparent Huge Pages (THP) on a host, which is a common practice for environments running big data, databases, and other performance-sensitive applications. THP can sometimes lead to performance degradation due to memory allocation overhead. The role also includes an optional step to rebuild the GRUB bootloader to ensure the THP setting persists across reboots.

The role will:
- Modify kernel parameters to disable THP at runtime.
- Create or update a shared Cloudera profile, `/etc/tuned/cldr/tuned.conf`, if the `tuned` service is enabled.
- Modify the GRUB configuration file to add a kernel boot parameter that disables THP.
- Rebuild the GRUB bootloader configuration to apply the change permanently.
- Ensure the changes are persistent across system restarts.

# Requirements

- Root or `sudo` privileges are required on the target host to modify kernel parameters and GRUB configuration.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| | | | | This role has no configurable parameters. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Disable Transparent Huge Pages and rebuild GRUB
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_thp
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
