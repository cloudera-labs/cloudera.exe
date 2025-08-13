# freeipa_server_users

Create superusers in FreeIPA.

This role creates superuser accounts in a FreeIPA environment. It's used to establish administrative accounts that are then added to a specified group, typically the **admins** group, to ensure they have the necessary permissions. The role is highly configurable, allowing you to define one or more superusers with their personal details and passwords.

## Requirements

- A running and accessible **FreeIPA server**.
- The `ipaadmin_principal` must have permissions to create users and manage groups within the FreeIPA environment.
- Network connectivity from the Ansible controller (or the execution host) to the FreeIPA server.

## Dependencies

None.

## Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `superuser_accounts` | `list` of `dict` | `False` | `[{'user': 'superuser', 'given_name': 'Cloudera', 'surname': 'Labs', 'password': 'superuser', 'display_name': 'Cloudera Labs Superuser'}]` | A list of superuser accounts to create. Each dictionary requires `user`, `given_name`, `surname`, and `password`. `display_name` is optional. |
| `superuser_group` | `str` | `False` | `admins` | The group to which the new superuser accounts will be added. |
| `ipaadmin_password` | `str` | `True` | | The password for the **FreeIPA** admin principal. This should be stored securely, for example, using Ansible Vault. |
| `ipaadmin_principal` | `str` | `False` | `admin` | The principal (username) for authenticating to the **FreeIPA** server. |
| `ipaserver_host` | `str` | `False` | `inventory_hostname` | The hostname or IP address of the **FreeIPA** server. |

## Example Playbook

```yaml
- hosts: ipaserver_host
  tasks:
    - name: Create default superuser
      ansible.builtin.import_role:
        name: cloudera.exe.freeipa_server_users
      vars:
        ipaadmin_password: "MySuperSecretAdminPassword" # Use Ansible Vault
        # All other values will use their defaults.

    - name: Create multiple superusers and add to a custom group
      ansible.builtin.import_role:
        name: cloudera.exe.freeipa_server_users
      vars:
        ipaadmin_password: "MySuperSecretAdminPassword" # Use Ansible Vault
        superuser_group: "power_users"
        superuser_accounts:
          - user: "ops_admin"
            given_name: "Operations"
            surname: "Admin"
            password: "OpsAdminPassword123"
          - user: "dev_admin"
            given_name: "Development"
            surname: "Admin"
            password: "DevAdminPassword456"
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
