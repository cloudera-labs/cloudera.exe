# cm_repo_local

Set up a local HTTP-based package repository for Cloudera Manager.

This role downloads a Cloudera Manager tarball package and sets up a local HTTP repository using Apache (httpd). This is useful for air-gapped environments or when you want to serve Cloudera Manager packages from a local web server.

The role will:
- Install and configure Apache HTTP Server (httpd)
- Download the Cloudera Manager tarball package from a specified URL
- Extract the tarball to a local repository directory with proper permissions (755)
- Configure httpd to serve the repository on a custom port
- Create a YUM repository configuration pointing to the local repository
- Clean YUM metadata to ensure the new repository is recognized

# Requirements

- Internet access from the target host to the specified package repository URL.
- Appropriate system permissions to manage package repositories (e.g., root access or sudo privileges).

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cloudera_manager_version` | `str` | `False` | `7.11.3` | Version of Cloudera Manager (used for reference/documentation) |
| `cloudera_manager_tarball_url` | `str` | `True` | - | Full URL to the Cloudera Manager tarball package (e.g., `https://archive.cloudera.com/cm7/7.11.3/redhat8/yum/cloudera-manager-7.11.3-redhat8.tar.gz`) |
| `cloudera_manager_repo_username` | `str` | `False` | - | Username for authenticated tarball downloads (if required) |
| `cloudera_manager_repo_password` | `str` | `False` | - | Password for authenticated tarball downloads (if required) |
| `cm_local_repo_base_path` | `str` | `False` | `/var/www/html/cloudera-repos` | Base directory where the repository will be extracted |
| `cm_local_repo_httpd_port` | `int` | `False` | `3333` | Port on which httpd will serve the local repository |
| `cm_local_repo_httpd_conf` | `str` | `False` | `/etc/httpd/conf/httpd.conf` | Path to the httpd configuration file |
| `cm_local_repo_yum_conf` | `str` | `False` | `/etc/yum.repos.d/cloudera-manager.repo` | Path to the YUM repository configuration file |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Set up local repository with authentication
      ansible.builtin.import_role:
        name: cloudera.exe.cm_repo_local
      vars:
        cloudera_manager_version: 7.11.3
        cloudera_manager_tarball_url: "https://my-internal-repo.example/cm7/7.11.3/redhat8/yum/cloudera-manager-7.11.3.tar.gz"
        cloudera_manager_repo_username: "YOUR_UUID_HERE" # Replace with your actual UUID
        cloudera_manager_repo_password: "YOUR_PASSWORD_HERE" # Replace with your actual 

    - name: Set up local repository with custom paths and port
      ansible.builtin.import_role:
        name: cloudera.exe.cm_repo_local
      vars:
        cloudera_manager_tarball_url: "https://my-internal-repo.example/cm7/7.11.3/redhat8/yum/cloudera-manager-7.11.3.tar.gz"
        cm_local_repo_base_path: "/opt/repos/cloudera"
        cm_local_repo_httpd_port: 8080
        cloudera_manager_repo_username: "YOUR_UUID_HERE" # Replace with your actual UUID
        cloudera_manager_repo_password: "YOUR_PASSWORD_HERE" # Replace with your actual 
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
