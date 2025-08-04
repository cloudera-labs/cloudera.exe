# prereq_ranger

Set up for Ranger

This role prepares a host for Apache Ranger usage by creating a set of dedicated system users and a group. It specifically creates the `ranger`, `rangerraz`, and `rangertagsync` users and the `ranger` group. These users and groups are essential for running Ranger services with appropriate permissions and isolation. The role can also optionally set up Access Control Lists (ACLs) on TLS entities if required for secure Ranger communication.

The role will:
- Create the `ranger` system group.
- Create the `ranger`, `rangerraz`, and `rangertagsync` system users, assigning them to the `ranger` group.
- Configure home directories and other necessary local paths for these users, if required.
- Ensure appropriate permissions are set for files and directories related to Ranger.
- Configure TLS ACLs to secure Ranger communication, if needed.

# Requirements

- Root or `sudo` privileges are required on the target host to create system users and groups, and to configure file system permissions and ACLs.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| | | | | This role has no configurable parameters. |

# Example Playbook

```yaml
- hosts: ranger_nodes
  tasks:
    - name: Set up the ranger users and environment
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_ranger
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
