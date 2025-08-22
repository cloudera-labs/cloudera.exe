# prereq_database

Create and manage databases and users

This role configures databases and their associated users in the specified database system. It connects to the database server using administrative credentials and then creates a list of user accounts and databases, granting the correct ownership and permissions. This role is highly flexible and can manage multiple databases and users in a single execution.

The role will:
- Connect to the specified database server using the provided `database_admin_user` and `database_admin_password`.
- Iterate through the `database_accounts` list to perform the following for each entry:
    - Create a new database with the specified name.
    - Create a new user account with the specified username and password.
    - Grant ownership of the new database to the specified owner (defaults to the created user).
- Ensure that all privileges are correctly assigned for the new users and databases.

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
| `database_admin_user` | `str` | `True` | | The username for the database admin login. |
| `database_admin_password` | `str` | `True` | | The password for the database admin login. This variable is marked with `no_log: true` and will not be displayed in Ansible logs. |
| `database_host` | `str` | `True` | | The hostname or IP address of the database server. |
| `database_port` | `int` | `False` | - | The port for connecting to the database server. If not specified, the role will use the default port for the specified database type. |
| `database_accounts` | `list` of `dict` | `True` | | A list of database accounts to create and manage. Each item in the list is a dictionary with the following keys. |
| &nbsp;&nbsp;&nbsp;&nbsp;`db` | `str` | `True` | | The name of the database to create. |
| &nbsp;&nbsp;&nbsp;&nbsp;`user` | `str` | `True` | | The name of the database user. |
| &nbsp;&nbsp;&nbsp;&nbsp;`password` | `str` | `True` | | The password for the database user. This variable is marked with `no_log: true` and will not be displayed in Ansible logs. |
| &nbsp;&nbsp;&nbsp;&nbsp;`owner` | `str` | `False` | `user` | The name of the database user who should own the database. If not specified, the `user` will be set as the owner. |

# Example Playbook

```yaml
- hosts: localhost
  tasks:
    - name: Manage databases and users on a PostgreSQL server
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_database
      vars:
        database_type: "postgresql"
        database_host: "db-server.example.com"
        database_admin_user: "postgres"
        database_admin_password: "my_postgres_admin_password" # Use Ansible Vault for this
        database_port: 5432
        database_accounts:
          - db: "scm"
            user: "scm_user"
            password: "scm_password_here" # Use Ansible Vault for this
          - db: "ranger"
            user: "ranger_user"
            password: "ranger_password_here"
            owner: "ranger_user" # Explicitly setting owner
          - db: "hive"
            user: "hive_user"
            password: "hive_password_here"
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
