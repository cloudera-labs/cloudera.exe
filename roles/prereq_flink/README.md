# prereq_flink

Set up for Flink

This role prepares a host for Apache Flink usage by creating a dedicated system user and group named `flink`. This user is essential for running Flink processes with appropriate permissions and isolation. The role can also optionally set up Access Control Lists (ACLs) on TLS entities if required for secure Flink communication.

The role will:
- Create the `flink` system user and group.
- Configure home directories and other necessary local paths for the `flink` user, if required.
- Ensure appropriate permissions are set for files and directories related to Flink.
- Configure TLS ACLs to secure Flink communication, if needed.

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
- hosts: flink_nodes
  tasks:
    - name: Set up the flink user and environment
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_flink
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
