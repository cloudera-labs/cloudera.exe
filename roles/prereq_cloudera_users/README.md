# prereq_cloudera_users

Set up for Local User Accounts required by Cloudera services

This role prepares a host for Cloudera Manager usage by performing several foundational setup tasks. It creates the dedicated `cloudera-scm` system user and group and configures the user's home directory and permissions.

The role will:
- Create the `cloudera-scm` system user and group.
- Configure permissions for the `cloudera-scm` user's home directory (`/var/lib/cloudera-scm`).
- Set up TLS ACLs (Access Control Lists) on the host, if needed by the Cloudera Manager service.

# Requirements

- Root or `sudo` privileges are required on the target host to manage system users, groups, and packages.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| | | | | This role has no configurable parameters. |

# Example Playbook

```yaml
- hosts: cm_nodes
  tasks:
    - name: Perform default Cloudera User Setup
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_cloudera_users
      # This will create the cloudera-scm user

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
