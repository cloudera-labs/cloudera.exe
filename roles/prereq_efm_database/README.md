# prereq_efm_database

Set up database and user accounts for Edge Flow Manager

This role automates the setup of a database and its associated user accounts specifically for Apache Edge Flow Manager services. The role creates the database and a dedicated user with ownership privileges, using sensible defaults that can be easily overridden.

The role will:
- Connect to the specified database server using administrative credentials.
- Create a new database with the name specified by `efm_database`.
- Create a new database user specified by `efm_username` with the password from `efm_password`.
- Grant ownership and all necessary privileges to the `efm_username` for the new database.
- Ensure the database is configured correctly for efm operations.

# Requirements

- A running and accessible database server of the specified `database_type`.
- The `database_admin_user` must have sufficient administrative privileges to create new databases and users.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `database_type` | `str` | `True` | | Specifies the type of database to connect to. |
| `database_host` | `str` | `True` | | The hostname or IP address of the database server. |
| `database_admin_user` | `str` | `True` | | The username with administrative privileges used to manage the database. |
| `database_admin_password` | `str` | `True` | | The password for the database administrative user. This variable is marked with `no_log: true` and will not be displayed in Ansible logs. |
| `efm_username` | `str` | `False` | `efm` | The username for the efm database user. This user will also be the owner of the database. |
| `efm_password` | `str` | `False` | `efm` | The password for the efm database user. It is highly recommended to override this default in production. |
| `efm_database` | `str` | `False` | `efm` | The name of the database to be created for efm. |

# Example Playbook

```yaml
- hosts: localhost
  tasks:
    - name: Set up efm database and user on PostgreSQL
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_efm_database
      vars:
        database_type: "postgresql"
        database_host: "db-server.example.com"
        database_admin_user: "postgres"
        database_admin_password: "my_postgres_admin_password"
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
