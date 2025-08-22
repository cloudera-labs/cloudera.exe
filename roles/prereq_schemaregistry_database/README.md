# prereq_schemaregistry_database

Set up database and user accounts for Schema Registry

This role automates the setup of a database and its associated user accounts specifically for Schema Registry services. It supports various database types, including PostgreSQL, MySQL, and Oracle. The role creates the database and a dedicated user with ownership privileges, using sensible defaults that can be easily overridden.

The role will:
- Connect to the specified database server using administrative credentials.
- Create a new database with the name specified by `schemaregistry_database`.
- Create a new database user specified by `schemaregistry_username` with the password from `schemaregistry_password`.
- Grant ownership and all necessary privileges to the `schemaregistry_username` for the new database.
- Ensure the database is configured correctly for Schema Registry operations.

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
| `database_admin_user` | `str` | `True` | | The username with administrative privileges used to manage the database. |
| `database_admin_password` | `str` | `True` | | The password for the database administrative user. This variable is marked with `no_log: true` and will not be displayed in Ansible logs. |
| `database_host` | `str` | `True` | | The hostname or IP address of the database server. |
| `database_port` | `int` | `False` | - | The port for connecting to the database server. If not specified, the role will use the default port for the specified database type. |
| `schemaregistry_username` | `str` | `False` | `registry` | The username for the Schema Registry database user. This user will also be the owner of the database. |
| `schemaregistry_password` | `str` | `False` | `registry` | The password for the Schema Registry database user. It is highly recommended to override this default in production. |
| `schemaregistry_database` | `str` | `False` | `registry` | The name of the database to be created for Schema Registry. |

# Example Playbook

```yaml
- hosts: localhost
  tasks:
    - name: Set up Schema Registry database and user on PostgreSQL
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_schemaregistry_database
      vars:
        database_type: "postgresql"
        database_host: "db-server.example.com"
        database_admin_user: "postgres"
        database_admin_password: "my_postgres_admin_password" # Use Ansible Vault for this

    - name: Set up Schema Registry database with custom credentials on MySQL
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_schemaregistry_database
      vars:
        database_type: "mysql"
        database_host: "mysql-db-server.example.com"
        database_admin_user: "root"
        database_admin_password: "my_mysql_root_password" # Use Ansible Vault for this
        schemaregistry_username: "my_sr_user"
        schemaregistry_password: "a_strong_sr_password"
        schemaregistry_database: "my_sr_db"
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
