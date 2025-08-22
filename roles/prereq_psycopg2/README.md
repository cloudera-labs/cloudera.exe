# prereq_psycopg2

Install psycopg2

This role installs the `psycopg2` Python package, which is the most popular PostgreSQL database adapter for the Python programming language. It is a critical component for many applications that need to interact with a PostgreSQL database. The role also provides an option to manage the state of PostgreSQL repositories on the host during the installation process.

The role will:
- Install the `psycopg2` Python package using `pip`.
- Optionally disable PostgreSQL-related package repositories before installation to prevent conflicts or unintended package updates, as controlled by `rdbms_repo_disable`.
- Ensure the package is installed and available for Python 3 applications.

# Requirements

- Python 3 and its package manager (`pip`) must be installed on the target host.
- Root or `sudo` privileges are required on the target host to install system-level packages and manage repositories, as `psycopg2` may have system library dependencies.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `rdbms_repo_disable` | `bool` | `False` | `true` | Flag to control whether PostgreSQL repositories are disabled before installing `psycopg2`. This is useful to prevent potential conflicts with existing repositories. If `false`, repositories will remain active. |

# Example Playbook

```yaml
- hosts: db_clients
  tasks:
    - name: Install psycopg2 and disable PSQL repos during installation
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_psycopg2
      # The rdbms_repo_disable flag will be true by default.

    - name: Install psycopg2 without disabling PSQL repos
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_psycopg2
      vars:
        rdbms_repo_disable: false
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
