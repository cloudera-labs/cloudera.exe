# Edge Flow Manager

This role streamlines the deployment and configuration of Cloudera Edge Flow Manager (EFM) on designeted host. It covers the full installation workflow, from fetching the EFM package to setting up the service and applying configuration templates.

## What this role does

- Retrieves the EFM tarball from a user-defined or default source
- Installs EFM into a configurable directory
- Sets up the required system user and group for EFM
- Applies configuration using a Jinja2 template for `efm.properties`
- Installs and manages the EFM systemd service unit
- Adjusts permissions for all relevant files and directories
- Supports authentication for protected download sources

# Requirements

- Network access from the target host to the URL specified in `efm_tarball_url`.

## Variables

| Name                            | Purpose                                                      | Default (see `defaults/main.yml`)           |
|----------------------------------|--------------------------------------------------------------|---------------------------------------------|
| `efm_tarball_url`                | Download link for the EFM tarball                            | (default provided in role)                  |
| `efm_directory`                  | Installation directory for EFM                               | `/opt/cloudera/cem`                         |
| `efm_properties_directory`       | Path to the EFM properties file                              | `/opt/cloudera/cem/efm/conf/efm.properties` |
| `efm_service_directory`          | Location for the systemd service file                        | `/etc/systemd/system/efm.service`           |
| `efm_user`                       | System user for EFM                                          | `efm`                                       |
| `efm_group`                      | System group for EFM                                         | `efm`                                       |
| `cloudera_manager_repo_username` | Username for protected repositories (optional)               |                                             |
| `cloudera_manager_repo_password` | Password for protected repositories (optional)               |                                             |

## Example usage

```yaml
- hosts: efm_nodes
  become: true
  roles:
    - role: efm
      vars:
        efm_tarball_url: "https://archive.cloudera.com/p/CEM/redhat9/2.x/updates/2.2.0.0/tars/efm/efm-2.2.0.0-1-bin.tar.gz"
        cloudera_manager_repo_username: "repo_user"
        cloudera_manager_repo_password: "repo_pass"
        efm_encryption_password: "pass"
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

