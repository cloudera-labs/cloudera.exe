# prereq_local_account

Set up local user accounts

This role automates the creation and management of local user accounts on a host. It can create multiple user accounts with specified home directories, UID, shell, comments, and group memberships. The role ensures that the user's home directory is created with the correct permissions.

The role will:
- Iterate through the list of `local_accounts` provided.
- For each account, create the system user and their primary group.
- Create the user's home directory with the specified permissions.
- Set the user's UID, shell, and comment if provided.
- Add the user to any specified `extra_groups`.

# Requirements

- Root or `sudo` privileges are required on the target host to manage system users and groups.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `local_accounts` | `list` of `dict` | `False` | `[]` | A list of user accounts to create. Each item in the list is a dictionary with the following keys. |
| &nbsp;&nbsp;&nbsp;&nbsp;`user` | `str` | `True` | | User account name. |
| &nbsp;&nbsp;&nbsp;&nbsp;`home` | `path` | `True` | | User account home directory. The role will create this directory. |
| &nbsp;&nbsp;&nbsp;&nbsp;`uid` | `int` | `False` | | User account UID (User ID). |
| &nbsp;&nbsp;&nbsp;&nbsp;`shell` | `str` | `False` | `/sbin/nologin` | User account shell. |
| &nbsp;&nbsp;&nbsp;&nbsp;`comment` | `str` | `False` | | Comments for the user account entry. |
| &nbsp;&nbsp;&nbsp;&nbsp;`extra_groups` | `list` of `str` | `False` | `[]` | Additional groups to assign (append) to the user account. |
| &nbsp;&nbsp;&nbsp;&nbsp;`mode` | `str` | `False` | `0755` | Permissions for the user account's home directory. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Create various local user accounts
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_local_account
      vars:
        local_accounts:
          - user: "appuser"
            home: "/home/appuser"
          - user: "jenkins"
            home: "/var/lib/jenkins"
            uid: 1001
            shell: "/bin/bash"
            comment: "CI/CD User"
            extra_groups:
              - "sudo"
              - "docker"
          - user: "monitoring"
            home: "/home/monitoring"
            mode: "0700"
            shell: "/bin/false"
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
