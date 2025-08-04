# postgresql_client

Client installation and configuration for PostgreSQL database

This role focuses on setting up client-side components for interacting with a PostgreSQL database. Primarily, it handles the installation of the PostgreSQL JDBC (Java Database Connectivity) Driver. Optionally, it can also install the `psycopg2` Python package, which is a PostgreSQL adapter for Python.

The role will:
- Download the specified PostgreSQL JDBC connector JAR file.
- Verify the integrity of the downloaded JDBC connector using a provided checksum.
- Install the JDBC connector JAR to the designated installation directory on the target host.
- Manage the download method for the JDBC connector, either via the Ansible controller for efficiency or directly on each target host.
- Optionally, install the `psycopg2` Python package using `pip` for Python-based applications needing PostgreSQL connectivity.

# Requirements

- **For JDBC Connector**:
    - A Java Runtime Environment (JRE) or Java Development Kit (JDK) is typically required on the target host for applications that will use the JDBC driver. This role does not install Java.
    - Write permissions for the Ansible user in the `postgresql_connector_install_dir`.
    - Network access from the download location (controller or target host) to the `postgresql_connector_url`.
- **For `psycopg2` (if `install_py3_psycopg2` is `true`)**:
    - Python 3 and its package manager (`pip`) must be installed on the target host. This role does not install Python or pip.
    - Network access from the target host to Python package repositories (e.g., PyPI).
    - Build tools may be required on the target host for `psycopg2` if pre-compiled binary wheels are not available for the operating system.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `postgresql_connector_url` | `str` | `False` | `https://jdbc.postgresql.org/download/postgresql-42.7.2.jar` | URL from which to download the PostgreSQL JDBC connector JAR file. |
| `postgresql_connector_checksum` | `str` | `False` | `md5:bb897217989c97a463d8f571069d158a` | Checksum of the downloaded PostgreSQL connector JAR file for integrity verification (e.g., `md5:<checksum_value>`). |
| `postgresql_connector_install_dir` | `str` | `False` | `/usr/share/java` | The absolute path on the target host where the PostgreSQL JDBC connector JAR will be installed. |
| `download_connector_to_controller` | `bool` | `False` | `true` | Flag to specify if the PostgreSQL connector should be downloaded via the Ansible controller host. If `true`, the download is performed once on the controller and then copied to each target host. If `false`, the download is performed directly on each target host. |
| `install_py3_psycopg2` | `bool` | `False` | `false` | Flag to specify if the `psycopg2` Python package (PostgreSQL adapter for Python 3) should be installed using `pip`. |

# Example Playbook

```yaml
- hosts: database_clients
  tasks:
    - name: Configure PostgreSQL client with default JDBC connector
      ansible.builtin.import_role:
        name: cloudera.exe.postgresql_client
      # Uses all default values for JDBC connector and does not install psycopg2.

    - name: Configure PostgreSQL client with specific JDBC version and install psycopg2
      ansible.builtin.import_role:
        name: cloudera.exe.postgresql_client
      vars:
        postgresql_connector_url: "https://jdbc.postgresql.org/download/postgresql-42.8.0.jar"
        postgresql_connector_checksum: "sha256:abcd1234efgh5678ijkl9012mnopqrstuv" # Replace with actual checksum
        postgresql_connector_install_dir: "/opt/custom/jdbc"
        download_connector_to_controller: false # Download on each target host
        install_py3_psycopg2: true # Install psycopg2 Python package
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
