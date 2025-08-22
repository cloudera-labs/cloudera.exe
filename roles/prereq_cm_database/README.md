# prereq_cm_database

Database and user for Cloudera Manager

This role creates the necessary database and a dedicated user account for Cloudera Manager to store its metadata. While primarily intended for PostgreSQL as specified in the description, it is designed to be flexible enough to work with other database types such as MySQL and Oracle. The role connects to an existing database server using administrative credentials to perform the setup.

The role will:
- Connect to the specified database server using the provided `database_admin_user` and `database_admin_password`.
- Create a new database with the name defined by `cloudera_manager_database_name`.
- Create a new database user specified by `cloudera_manager_database_user`.
- Grant ownership and all necessary privileges on the new database to the new user.

# Requirements

- A running and accessible database server of the specified `cloudera_manager_database_type`.
- The `database_admin_user` must have sufficient administrative privileges to create new databases and users.
- The machine running the Ansible playbook must have the necessary database client libraries installed to connect to the database (e.g., `psycopg2` for PostgreSQL, `mysql-connector-python` for MySQL).

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cloudera_manager_database_user` | `str` | `False` | `scm` | The username for the Cloudera Manager database account. This user will be created and granted ownership of the database. |
| `cloudera_manager_database_type` | `str` | `True` | | The type of database to connect to. Valid choices are `postgresql`, `mysql`, and `oracle`. |
| `cloudera_manager_database_password` | `str` | `True` | | The password for the Cloudera Manager database user. This password will be used by Cloudera Manager to connect to its database. |
| `cloudera_manager_database_name` | `str` | `False` | `scm` | The name of the database to be created for Cloudera Manager. |
| `database_admin_user` | `str` | `True` | | The username with administrative privileges used to manage the database. |
| `database_admin_password` | `str` | `True` | | The password for the database administrative user. This variable is marked with `no_log: true` and will not be displayed in Ansible logs. |
| `database_host` | `str` | `True` | | The hostname or IP address of the database server. |
| `database_port` | `int` | `False` | - | The port for connecting to the database server. If not specified, the role will use the default port for the specified database type. |

# Example Playbook

```yaml
- hosts: localhost
  tasks:
    - name: Create database and user for Cloudera Manager on PostgreSQL
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_cm_database
      vars:
        cloudera_manager_database_type: "postgresql"
        cloudera_manager_database_password: "scm_strong_password" # Use Ansible Vault for this
        database_admin_user: "postgres"
        database_admin_password: "postgres_admin_password" # Use Ansible Vault for this
        database_host: "db-server.example.com"
        database_port: 5432 # Explicitly set port for clarity

    - name: Create database and user for Cloudera Manager on MySQL
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_cm_database
      vars:
        cloudera_manager_database_type: "mysql"
        cloudera_manager_database_user: "cm_mysql_user"
        cloudera_manager_database_password: "mysql_strong_password" # Use Ansible Vault for this
        cloudera_manager_database_name: "cm_metadata"
        database_admin_user: "root"
        database_admin_password: "mysql_root_password" # Use Ansible Vault for this
        database_host: "mysql-server.example.com"
        database_port: 3306
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
