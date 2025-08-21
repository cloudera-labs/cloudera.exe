# prereq_cloudera_manager

Set up for Cloudera Manager

This role prepares a host for Cloudera Manager usage by performing several foundational setup tasks. It creates the dedicated `cloudera-scm` system user and group, configures the user's home directory and permissions, and can optionally install LDAP client packages for Kerberos support.

The role will:
- Create the `cloudera-scm` system user and group.
- Configure permissions for the `cloudera-scm` user's home directory (`/var/lib/cloudera-scm`).
- Set up TLS ACLs (Access Control Lists) on the host, if needed by the Cloudera Manager service.
- Optionally install a list of specified LDAP packages, which are often required for Kerberos authentication integration.
- Ensure the Kerberos configuration file (`/etc/krb5.conf`) is properly configured for the Cloudera Manager service.

# Requirements

- Root or `sudo` privileges are required on the target host to manage system users, groups, and packages.
- The Kerberos configuration file at `kerberos_config_path` must exist on the target host or be managed by another role.

# Dependencies

- `cloudera.exe.prereq_cloudera_users`

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `kerberos_config_path` | `path` | `False` | `/etc/krb5.conf` | Path to the Kerberos configuration file on the target host. |
| `cloudera_manager_ldap_packages` | `list` of `str` | `False` | | List of LDAP packages to install for enabling Kerberos support. If not defined, the role will use default packages based on the OS distribution. |

# Example Playbook

```yaml
- hosts: cm_nodes
  tasks:
    - name: Perform default Cloudera Manager setup
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_cloudera_manager
      # This will create the cloudera-scm user and use the default krb5.conf path.

    - name: Perform Cloudera Manager setup with custom Kerberos and LDAP packages
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_cloudera_manager
      vars:
        kerberos_config_path: "/etc/my-custom-krb5.conf"
        cloudera_manager_ldap_packages:
          - "openldap-clients"
          - "nss-pam-ldapd"
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
