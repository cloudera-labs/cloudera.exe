# prereq_python

Install Python

This role ensures that the correct versions of Python are installed on a host to meet the requirements of specified Cloudera Manager and Cloudera Runtime versions. It also handles the installation and update of the `pip` package manager for Python 3. For environments that still require Python 2, the role provides a flag to control whether the installation is done via the system package manager or from source.

To validate the required Python version for a given Cloudera Manager and Runtime, the [Cloudera on premise documentation](https://docs.cloudera.com/cdp-private-cloud-base/latest/installation/topics/cdpdc-cm-install-python-3.8.html) and the support matrix variables defined in the `cloudera.exe.prereq_supported` role are used.

The role will:
- Determine the required Python versions based on `cloudera_manager_version` and `cloudera_runtime_version`.
- Install the necessary Python 3 packages if a supported version is not already present.
- Install or update the `pip` package for Python 3.
- If Python 2 is required, install it either via the system's package manager (`python2_package_install: true`) or from source (`python2_package_install: false`).
- Ensure that the installed Python versions and `pip` are properly configured and accessible.

# Requirements

- Root or `sudo` privileges are required on the target host to install system packages.
- Network access to package repositories (for system packages) and PyPI (for pip).
- If installing Python 2 from source, the host will require build tools (e.g., `gcc`, `make`, development headers).

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cloudera_manager_version` | `str` | `False` | `7.11.3` | The version of Cloudera Manager to use for determining Python version requirements. |
| `cloudera_runtime_version` | `str` | `False` | `7.1.9` | The version of Cloudera Runtime to use for determining Python version requirements. |
| `python3_package` | `str` | `False` | - | An optional name of the Python 3 package to install. This is only used when a supported version of Python 3 is not found. If not specified, the role will use OS-specific default package names. |
| `python3_pip_package` | `str` | `False` | `python-pip` | The name of the Python 3 Pip package to be installed or updated. |
| `python2_package_install` | `bool` | `False` | `true` | Flag to specify if Python 2 should be installed via the system package manager. If `false`, the role will attempt to install Python 2 from source. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Install Python for Cloudera Manager 7.11.3 / Cloudera Runtime 7.1.9
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_python
      # All variables will use their defaults, installing Python 3 with pip and Python 2 via package manager.

    - name: Install Python for a different version of Cloudera Runtime
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_python
      vars:
        cloudera_runtime_version: "7.1.8"
        # The role will adjust Python version requirements accordingly.

    - name: Install Python with custom package names and install Python 2 from source
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_python
      vars:
        python3_package: "python39" # Example custom package name for Python 3.9
        python3_pip_package: "python3-pip"
        python2_package_install: false # Install Python 2 from source
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
