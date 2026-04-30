

# prereq_freeipa_client

Install prerequisites for FreeIPA client

This role prepares a host for FreeIPA client installation by installing necessary system packages and Python packages. It automatically detects the operating system distribution and installs the appropriate dependencies required for the FreeIPA client functionality.

The role will:
- Detect the target host's operating system (RedHat, etc.).
- Install OS-specific system packages required for FreeIPA client (krb5-devel, gcc, libffi-devel, openssl-devel).
- Detect the Python version installed on the target host.
- Install Python packages needed for FreeIPA client functionality (ipaclient, packaging) using the appropriate pip version.

# Requirements

- Root or `sudo` privileges are required on the target host to install system and Python packages.
- Python and pip must be available on the target host.
- Network access to package repositories (yum/dnf for system packages, PyPI for Python packages).

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `system_packages` | `list` | `False` | OS-specific defaults | List of system packages to install for FreeIPA client. If not provided, OS-specific defaults will be used (krb5-devel, gcc, libffi-devel, openssl-devel for RedHat-based systems). |
| `python_packages` | `list` | `False` | `['ipaclient', 'packaging']` | List of Python packages to install for FreeIPA client functionality. If not provided, defaults to ipaclient and packaging. |

# Example Playbook

```yaml
- hosts: freeipa_clients
  tasks:
    - name: Install FreeIPA client prerequisites
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_freeipa_client
      # Uses default system packages for the detected OS

    - name: Install FreeIPA client prerequisites with custom packages
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_freeipa_client
      vars:
        system_packages:
          - krb5-devel
          - gcc
          - libffi-devel
          - openssl-devel
          - python3-devel
        python_packages:
          - ipaclient
          - packaging
          - python-freeipa
```

# License

```
Copyright 2026 Cloudera, Inc.

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
