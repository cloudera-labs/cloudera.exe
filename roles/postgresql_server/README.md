# postgresql_server

Install PostgreSQL server for Cloudera Manager

This role installs and configures a PostgreSQL server, primarily for use as a backend database for Cloudera Manager. It sets up the necessary packages, manages the PostgreSQL repository, configures essential database settings (e.g., `postgresql.conf`), and defines host-based authentication rules (`pg_hba.conf`). The role can also optionally create a database superuser and enable TLS for secure connections. It will also ensure the `psycopg2` (or `psycopg3`) Python client library is available.

The role will:
- Optionally enable or disable the PostgreSQL package repository setup.
- Install PostgreSQL server packages, including client libraries and utilities.
- Ensure the `psycopg2` (or `psycopg3`) Python package is installed, which is often required for Ansible's PostgreSQL modules.
- Create a dedicated database superuser account if `create_database_admin_user` is `true`.
- Configure global PostgreSQL server settings by managing the `postgresql.conf` file.
- Configure host-based authentication (HBA) rules by managing the `pg_hba.conf` file, controlling client access.
- Optionally, enable and configure TLS for secure client-server connections, utilizing specified certificate, key, and CA files.
- Start and enable the PostgreSQL service.

# Requirements

- Target host must have internet access to download PostgreSQL packages and repository data.
- Root or `sudo` privileges are required to manage packages, services, and system configuration files.
- If `postgresql_tls_enabled` is `true`, ensure that the certificate, key, and CA files specified (`postgresql_tls_cert_path`, `postgresql_tls_key_path`, `postgresql_tls_ca_path`) are present on the target host prior to execution.

# Dependencies

- `community.general`
- `community.postgresql`

In addition, the following role(s) are required:

- `geerlingguy.postgres`


# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `create_database_admin_user` | `bool` | `False` | `false` | Flag to specify if a database superuser should be created by this role. If `true`, `database_admin_user` and `database_admin_password` must be provided. |
| `database_admin_user` | `str` | `True` if `create_database_admin_user` is `true` | | Username for the database superuser account to be created. |
| `database_admin_password` | `str` | `True` if `create_database_admin_user` is `true` | | Password for the database superuser account to be created. |
| `postgresql_version` | `int` | `False` | `14` | PostgreSQL version to install (e.g., 12, 14, 16). |
| `postgresql_packages` | `list` of `str` | `False` | `[defaults based on OS]` | List of packages to install for the PostgreSQL server. If not defined, the role will use default package names specific to the OS distribution and PostgreSQL version. |
| `postgresql_repo_enabled` | `bool` | `False` | `true` | Flag enabling the setup and teardown of the PostgreSQL package repository. If `false`, the role will assume existing repositories are configured and will not modify them. |
| `postgresql_tls_enabled` | `bool` | `False` | `false` | Flag enabling TLS connections for the PostgreSQL server. |
| `postgresql_tls_cert_path` | `path` | `False` | `$PGDATA/server.crt` | Path to the TLS certificate file on the PostgreSQL server. If not specified, PostgreSQL typically uses a default path (e.g., `$PGDATA/server.crt`). |
| `postgresql_tls_key_path` | `path` | `False` | `$PGDATA/server.key` | Path to the TLS private key file on the PostgreSQL server. If not specified, PostgreSQL typically uses a default path (e.g., `$PGDATA/server.key`). |
| `postgresql_tls_ca_path` | `path` | `False` | `None` | Path to the TLS Certificate Authority (CA) file on the PostgreSQL server. If not specified, PostgreSQL will typically not use a CA file, impacting client certificate validation. |
| `postgresql_config_options` | `list` of `dict` | `False` | `[]` | List of global configuration entries for the `postgresql.conf` file. Each dictionary requires an `option` (parameter name) and a `value`. |
| &nbsp;&nbsp;&nbsp;&nbsp;`option` | `str` | `True` | | Name of the PostgreSQL configuration parameter (e.g., `listen_addresses`). |
| &nbsp;&nbsp;&nbsp;&nbsp;`value` | `str` | `True` | | Value of the PostgreSQL configuration parameter (e.g., `'*'`). |
| `postgresql_access_entries` | `list` of `dict` | `False` | `[]` | List of host-based authentication (HBA) entries for the `pg_hba.conf` file. Each dictionary requires `type`, `database`, `user`, and `auth_method`. `address` is optional. |
| &nbsp;&nbsp;&nbsp;&nbsp;`type` | `str` | `True` | | Authentication scope type (e.g., `host`, `local`). |
| &nbsp;&nbsp;&nbsp;&nbsp;`database` | `str` | `True` | | Database target for the HBA rule (e.g., `all`, `scm`). |
| &nbsp;&nbsp;&nbsp;&nbsp;`user` | `str` | `True` | | User or user type for the HBA rule (e.g., `all`, `scm_user`). |
| &nbsp;&nbsp;&nbsp;&nbsp;`address` | `str` | `False` | | Networking scope (e.g., `10.0.0.0/24`, `::1/128`). Required for `host` type. |
| &nbsp;&nbsp;&nbsp;&nbsp;`auth_method` | `str` | `True` | | Authentication method (e.g., `md5`, `scram-sha-256`, `trust`). |

# Example Playbook

```yaml
- hosts: db_servers
  tasks:
    - name: Install PostgreSQL server with default settings
      ansible.builtin.import_role:
        name: cloudera.exe.postgresql_server
      # Uses PostgreSQL 14, default packages, no admin user, no TLS, default configs.

    - name: Install PostgreSQL 16 with custom admin user and basic HBA
      ansible.builtin.import_role:
        name: cloudera.exe.postgresql_server
      vars:
        postgresql_version: 16
        create_database_admin_user: true
        database_admin_user: "cm_admin"
        database_admin_password: "MySuperSecurePassword"
        postgresql_access_entries:
          - type: host
            database: all
            user: all
            address: 0.0.0.0/0
            auth_method: md5
          - type: host
            database: all
            user: all
            address: ::/0
            auth_method: md5

    - name: Install PostgreSQL with TLS enabled and custom configs
      ansible.builtin.import_role:
        name: cloudera.exe.postgresql_server
      vars:
        postgresql_version: 14
        postgresql_tls_enabled: true
        postgresql_tls_cert_path: "/etc/pki/tls/certs/server.crt"
        postgresql_tls_key_path: "/etc/pki/tls/private/server.key"
        postgresql_tls_ca_path: "/etc/pki/tls/certs/ca.crt"
        postgresql_config_options:
          - option: ssl
            value: on
          - option: ssl_cert_file
            value: "/etc/pki/tls/certs/server.crt"
          - option: ssl_key_file
            value: "/etc/pki/tls/private/server.key"
          - option: ssl_ca_file
            value: "/etc/pki/tls/certs/ca.crt"
          - option: listen_addresses
            value: "'*'"
        postgresql_access_entries:
          - type: hostssl # Enforce SSL for this rule
            database: all
            user: all
            address: 0.0.0.0/0
            auth_method: scram-sha-256
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
