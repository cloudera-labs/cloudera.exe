# prereq_nifi

Set up for NiFi

This role prepares a host for Apache NiFi usage by creating a dedicated system user and group named `nifi`. This user is essential for running NiFi processes with appropriate permissions and isolation. The role can also optionally set up Access Control Lists (ACLs) on TLS entities if required for secure NiFi communication.

The role will:
- Create the `nifi` system user and group.
- Configure home directories and other necessary local paths for the `nifi` user, if required.
- Ensure appropriate permissions are set for files and directories related to NiFi.
- Configure TLS ACLs to secure NiFi communication, if needed.

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
- hosts: nifi_nodes
  tasks:
    - name: Set up the nifi user and environment
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_nifi
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
