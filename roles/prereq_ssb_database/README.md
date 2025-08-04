# prereq_ssb_database

Set up database and user accounts for SQL Stream Builder

This role automates the setup of databases and their associated user accounts for SQL Stream Builder (SSB) and its Materialized View Engine (MVE). It supports various database types, including PostgreSQL, MySQL, and Oracle. The role creates two distinct databases and dedicated users with ownership privileges for each, using sensible defaults that can be easily overridden.

The role will:
- Connect to the specified database server using administrative credentials.
- For the SSB Admin service, it will:
    - Create a new database with the name specified by `ssb_admin_database`.
    - Create a new database user specified by `ssb_admin_username` with the password from `ssb_admin_password`.
    - Grant ownership and all necessary privileges to the `ssb_admin_username` for the new database.
- For the SSB Materialized View Engine, it will:
    - Create a new database with the name specified by `ssb_mve_database`.
    - Create a new database user specified by `ssb_mve_username` with the password from `ssb_mve_password`.
    - Grant ownership and all necessary privileges to the `ssb_mve_username` for the new database.

# Requirements

- A running and accessible database server of the specified `database_type`.
- The `database_admin_user` must have sufficient administrative privileges to create new databases and users.
- The machine running the Ansible playbook must have the necessary database client libraries installed to connect to the database (e.g., `psycopg2` for PostgreSQL, `mysql-connector-python` for MySQL).

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `database_type` | `str` | `True` | | Specifies the type of database to connect to. Valid choices are `postgresql`, `mysql`, and `oracle`. |
| `database_host` | `str` | `True` | | The hostname or IP address of the database server. |
| `database_admin_user` | `str` | `True` | | The username with administrative privileges used to manage the database. |
| `database_admin_password` | `str` | `True` | | The password for the database administrative user. This variable is marked with `no_log: true` and will not be displayed in Ansible logs. |
| `ssb_admin_username` | `str` | `False` | `ssb_admin` | The username for the SQL Stream Builder Admin database user and owner of the database. |
| `ssb_admin_password` | `str` | `False` | `ssb_admin` | The password for the SQL Stream Builder Admin database user. It is highly recommended to override this default in production. |
| `ssb_admin_database` | `str` | `False` | `ssb_admin` | The name of the database to be created for SQL Stream Builder Admin. |
| `ssb_mve_username` | `str` | `False` | `ssb_mve` | The username for the Materialized View Engine database user and owner of the database. |
| `ssb_mve_password` | `str` | `False` | `ssb_mve` | The password for the Materialized View Engine database user. It is highly recommended to override this default in production. |
| `ssb_mve_database` | `str` | `False` | `ssb_mve` | The name of the database to be created for the Materialized View Engine. |

# Example Playbook

```yaml
- hosts: localhost
  tasks:
    - name: Set up SSB databases and users on PostgreSQL
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_ssb_database
      vars:
        database_type: "postgresql"
        database_host: "db-server.example.com"
        database_admin_user: "postgres"
        database_admin_password: "my_postgres_admin_password" # Use Ansible Vault for this

    - name: Set up SSB databases with custom credentials on MySQL
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_ssb_database
      vars:
        database_type: "mysql"
        database_host: "mysql-db-server.example.com"
        database_admin_user: "root"
        database_admin_password: "my_mysql_root_password" # Use Ansible Vault for this
        ssb_admin_username: "my_ssb_admin_user"
        ssb_admin_password: "a_strong_ssb_admin_password"
        ssb_admin_database: "my_ssb_admin_db"
        ssb_mve_username: "my_mve_user"
        ssb_mve_password: "a_strong_mve_password"
        ssb_mve_database: "my_mve_db"
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
