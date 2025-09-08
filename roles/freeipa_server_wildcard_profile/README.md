# freeipa_server_ecs

Install a wildcard certificate profile for FreeIPA

This role creates a certificate profile in FreeIPA specifically for issuing wildcard certificates. It configures a new profile to include a wildcard Subject Alternative Name (SAN), making it easy to generate certificates that secure multiple subdomains. This role is designed to be run directly on a FreeIPA server and will not modify an existing profile if one with the same name is already present.

## Requirements
- The `ipaadmin_principal` must have permissions to manage certificate profiles in FreeIPA.
- The role assumes it's being run on the FreeIPA server itself.

## Dependencies

None.

## Parameters
| Variable| Type | Required |	Default	| Description |
| --- | --- | --- | --- | --- |
| `ipaadmin_principal` | `str` | `False` | `admin` | FreeIPA admin principal for authentication. |
| `ipaadmin_password`	| `str`	| `True`| | FreeIPA admin password for authentication. This should be stored securely, e.g., using Ansible Vault. |
| `ipaserver_domain` | `str` | `True`	| | Domain name to use as the root zone for references within the profile (e.g., example.internal). |
| `ipaserver_realm`	| `str`	| `True` | | Realm name to use for references within the profile (e.g., EXAMPLE.INTERNAL). |
| `freeipa_wildcard_profile_name` |	`str` |	`False`	| `wildcard` | The name of the wildcard certificate profile to create in FreeIPA. |

## Example Playbook

```yaml
- hosts: ipaserver_host
  tasks:
    - name: Create the default wildcard certificate profile in FreeIPA
      ansible.builtin.import_role:
        name: cloudera.exe.freeipa_server_wildcard_profile
      vars:
        ipaadmin_password: "MySuperSecretAdminPassword" # Use Ansible Vault
        ipaserver_domain: "example.internal"
        ipaserver_realm: "EXAMPLE.INTERNAL"

    - name: Create a custom named wildcard certificate profile
      ansible.builtin.import_role:
        name: cloudera.exe.freeipa_server_wildcard_profile
      vars:
        ipaadmin_password: "MySuperSecretAdminPassword"
        ipaserver_domain: "apps.example.internal"
        ipaserver_realm: "EXAMPLE.INTERNAL"
        freeipa_wildcard_profile_name: "custom_profile"
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
