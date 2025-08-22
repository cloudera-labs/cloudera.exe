# cm_repo

Manage the package repository for Cloudera Manager.

This role manages the configuration of the package repository used for downloading and installing Cloudera Manager binaries. It provides flexible options to configure access to various repository types, including Cloudera's trial archives, enterprise archives requiring authentication, and custom private repositories.

The role will:
- Add or configure the appropriate package repository (e.g., YUM/APT) for Cloudera Manager.
- Handle authentication for enterprise or custom repositories using provided username and password.
- Optionally configure GPG key validation for repository contents.
- Enable the repository for package installation.

# Requirements

- Internet access from the target host to the specified package repository URL.
- Appropriate system permissions to manage package repositories (e.g., root access or sudo privileges).

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cloudera_manager_version` | `str` | `False` | `7.11.3` | Version of Cloudera Manager for which the repository is being configured. If not defined and `cloudera_manager_repo_username` is not set, it will typically default to a trial version like `7.4.4`, if compatible with the OS distribution and if the `cloudera_manager_repo_url` is not explicitly set to an enterprise archive. |
| `cloudera_manager_repo_url` | `str` | `False` | - | Base URL for the package repository. If not defined and `cloudera_manager_repo_username` is set, it will default to the Cloudera enterprise archive URL for the specified version. Otherwise, it defaults to the Cloudera trial archive URL. |
| `cloudera_manager_repo_username` | `str` | `False` | | Username for authenticating to the package repository. For Cloudera enterprise licenses, this corresponds to the `uuid` value provided by Cloudera. |
| `cloudera_manager_repo_password` | `str` | `False` | | Password for authenticating to the package repository. For Cloudera enterprise licenses, this corresponds to the derived `password` value associated with your `uuid`. |
| `cloudera_manager_repo_key` | `str` | `False` | | URL to the package repository's GPG public key for content validation. |
| `cloudera_manager_repo_gpgcheck` | `bool` | `False` | - | Flag to manage validation checks (GPG checks) of the repository contents. Set to `true` to enable GPG signature verification during package installation. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Configure Cloudera Manager trial repository (default version)
      ansible.builtin.import_role:
        name: cloudera.exe.cm_repo
      vars:
        # cloudera_manager_version and cloudera_manager_repo_url will use their implicit defaults for trial.
        # No username/password needed.

    - name: Configure Cloudera Manager enterprise repository for a specific version
      ansible.builtin.import_role:
        name: cloudera.exe.cm_repo
      vars:
        cloudera_manager_version: 7.11.3
        cloudera_manager_repo_username: "YOUR_UUID_HERE" # Replace with your actual UUID
        cloudera_manager_repo_password: "YOUR_PASSWORD_HERE" # Replace with your actual password
        # cloudera_manager_repo_url will default to the enterprise archive for 7.11.3

    - name: Configure a custom Cloudera Manager repository
      ansible.builtin.import_role:
        name: cloudera.exe.cm_repo
      vars:
        cloudera_manager_version: 7.11.1 # Example specific version
        cloudera_manager_repo_url: "http://my-internal-repo.example.com/cm/7.11.1/"
        cloudera_manager_repo_username: "internal_user"
        cloudera_manager_repo_password: "internal_password"
        cloudera_manager_repo_key: "http://my-internal-repo.example.com/gpg/repo.key"
        cloudera_manager_repo_gpgcheck: true
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
