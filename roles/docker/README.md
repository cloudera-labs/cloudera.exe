# docker

Install Docker

This role installs Docker Community Edition (CE) and related packages, and then adds specified users to the `docker` group, allowing them to manage Docker containers without `sudo`. It supports configuring the Docker repository for both RedHat-based and Ubuntu-based operating systems.

The role will:
- Configure the appropriate Docker package repository for the detected operating system.
- Import the necessary GPG key for the Docker repository.
- Install the specified Docker packages (`docker-ce`, `docker-ce-cli`, `containerd.io`, etc.).
- Ensure the Docker service is running and enabled.
- Create the `docker` group if it does not exist.
- Add specified users to the `docker` group, granting them Docker management privileges.

# Requirements

- Target host must have internet access to download Docker packages and repository keys.
- Root or `sudo` privileges are required to manage packages and system services.
- For adding users to the `docker` group, the users must already exist on the system.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `docker_repo` | `str` | `False` | - | The string identifying the Docker repository. For RedHat-based OS distributions, this is the URL for the YUM/DNF repository. For Ubuntu-based OS distributions, this is the deb package string for the APT repository. If not specified, the value is taken from the role's default variables. |
| `docker_repo_key` | `str` | `False` | - | URL for the GPG key used to validate the Docker repository. If not specified, the value is taken from the role's default variables. |
| `docker_packages` | `list` of `str` | `False` | `["docker-ce", "docker-ce-cli", "docker-ce-rootless-extras", "containerd.io", "docker-buildx-plugin"]` | List of Docker packages to install. This allows customization of installed components. |
| `docker_users` | `list` of `str` | `False` | `[]` | List of usernames that should be added to the `docker` system group. These users will then be able to run Docker commands without `sudo`. |

# Example Playbook

```yaml
- hosts: docker_hosts
  tasks:
    - name: Install Docker with default packages and add admin user
      ansible.builtin.import_role:
        name: cloudera.exe.docker
      vars:
        docker_users:
          - adminuser
          - devops

    - name: Install Docker with specific packages and repo for Ubuntu
      ansible.builtin.import_role:
        name: cloudera.exe.docker
      vars:
        docker_repo: "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
        docker_repo_key: "https://download.docker.com/linux/ubuntu/gpg"
        docker_packages:
          - "docker-ce"
          - "docker-ce-cli"
          - "containerd.io"
        docker_users:
          - jenkins_user

## License

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
