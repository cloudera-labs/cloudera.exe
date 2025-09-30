# pgadmin

Install pgAdmin

This role installs and configures pgAdmin 4, running it as a Docker container. It sets up automatic access to a list of specified PostgreSQL databases, enabling quick management through the pgAdmin web UI. A systemd service file is created to manage the pgAdmin container's lifecycle (start/stop).

The role will:
- Pull the official pgAdmin 4 Docker image.
- Create necessary directories for pgAdmin configuration and data persistence.
- Generate and configure the `.pgpass` file within the container for seamless database authentication.
- Create a configuration file to preload specified database connections into pgAdmin upon its first launch.
- Define and configure the pgAdmin web UI access details (email and password).
- Create a systemd service unit file to manage the pgAdmin Docker container.
- Start and enable the pgAdmin service to run on system boot.

# Requirements

- **Docker**: The `docker` service must be installed and running on the target host. Consider using the `docker_install` role as a prerequisite.
- **Systemd**: The target host must use `systemd` for service management.
- **Network Access**: The target host where pgAdmin is installed must have network access to the PostgreSQL database server(s).
- **Database Credentials**: The provided `database_admin_user` and `database_admin_password` must have sufficient privileges to access the specified databases.

# Dependencies

- `docker_install` (Recommended for Docker installation)

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `database_admin_user` | `str` | `True` | | Username for the database superuser account that pgAdmin will use to connect to databases. |
| `database_admin_password` | `str` | `True` | | Password for the database superuser account. |
| `database_host` | `str` | `True` | | The hostname or IP address of the primary PostgreSQL database server that pgAdmin will connect to. |
| `database_port` | `int` | `False` | `5432` | The port for connecting to the primary database server. |
| `pgadmin_db_servers` | `list` of `dict` | `False` | `[{Name: "CE Postgres", Group: "Servers", Port: "{{ database_port }}", Username: "{{ database_admin_user }}", PassFile: /pgpass, Host: "{{ database_host }}", SSLMode: prefer, MaintenanceDB: postgres}]` | A list of dictionaries, where each dictionary defines a database connection to be pre-loaded into pgAdmin at its first launch. Uses Jinja2 templating to derive values from `database_host`, `database_port`, and `database_admin_user` by default. |
| `pgadmin_pgpass` | `list` of `str` | `False` | `["{{ database_host }}:{{ database_port }}:*:{{ database_admin_user }}:{{ database_admin_password }}"]` | Contents for the `.pgpass` file within the pgAdmin container. Each element is a line in the format `hostname:port:database:username:password`. Uses Jinja2 templating by default to include the primary database's credentials. |
| `pgadmin_port` | `int` | `False` | `5050` | The port on the host where the pgAdmin web UI service will be listening. |
| `pgadmin_default_email` | `str` | `False` | `pgadmin@cloudera-labs.com` | Email account for the default user to access the pgAdmin web UI. This user is created on first launch of the container. |
| `pgadmin_default_password` | `str` | `False` | `pgadmin` | Password for the default user to access the pgAdmin web UI. **It is highly recommended to change this default password for production environments.** |
| `pgadmin_docker_exe` | `str` | `False` | `/usr/bin/docker` | The full path to the Docker executable on the target host. |
| `pgadmin_docker_network_subnet_cidr` | `str` | `False` | `172.21.0.0/16` | Subnet CIDR for the Docker bridge network used by pgadmin. |
| `pgadmin_docker_network_subnet_gateway` | `str` | `False` | `172.21.0.1` | Gateway for the Docker bridge network subnet used by pgadmin. |

# Example Playbook

```yaml
- hosts: pgadmin_host
  tasks:
    - name: Ensure Docker is installed (if not already)
      ansible.builtin.import_role:
        name: cloudera.exe.docker # Prerequisite role
      # You might pass variables to docker_install here if needed.

    - name: Install and configure pgAdmin for a single database
      ansible.builtin.import_role:
        name: cloudera.exe.pgadmin
      vars:
        database_admin_user: "postgres_superuser"
        database_admin_password: "my_secure_db_password"
        database_host: "my-db-server.example.com"
        database_port: 5432 # Explicitly define if not default

    - name: Install pgAdmin with custom web UI port and multiple database connections
      ansible.builtin.import_role:
        name: cloudera.exe.pgadmin
      vars:
        database_admin_user: "dbuser"
        database_admin_password: "another_secure_password"
        database_host: "main-db.example.com"
        pgadmin_port: 8080 # Custom port for web UI
        pgadmin_default_email: "admin@mycompany.com"
        pgadmin_default_password: "new_strong_password"
        pgadmin_db_servers:
          - Name: "Primary DB"
            Group: "Production"
            Port: 5432
            Username: "{{ database_admin_user }}"
            PassFile: /pgpass
            Host: "{{ database_host }}"
            SSLMode: prefer
            MaintenanceDB: postgres
          - Name: "Analytics DB"
            Group: "Data Warehousing"
            Port: 5432
            Username: "analytics_user"
            PassFile: /pgpass
            Host: "analytics-db.example.com"
            SSLMode: require
            MaintenanceDB: analytics_db
        pgadmin_pgpass:
          - "{{ database_host }}:{{ database_port }}:*:{{ database_admin_user }}:{{ database_admin_password }}"
          - "analytics-db.example.com:5432:*:analytics_user:analytics_password_secret" # Add credentials for analytics DB
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
