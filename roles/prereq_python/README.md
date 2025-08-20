# prereq_python

Install Python and pip.

This role ensures that the correct versions of Python are installed on a host to meet the requirements of specified Cloudera Manager and Cloudera Runtime versions. It also handles the installation and update of the `pip` package manager. For environments that still require Python 2, the role provides a flag to control whether the installation is done via the system package manager or from source.

To validate the required Python version for a given Cloudera Manager and Runtime, the [Cloudera on premise documentation](https://docs.cloudera.com/cdp-private-cloud-base/latest/installation/topics/cdpdc-cm-install-python-3.8.html) and the support matrix variables defined in the `cloudera.exe.prereq_supported` role are used.

The role will:
- Determine the required Python versions based on `cloudera_manager_version` and `cloudera_runtime_version`.
- Install the necessary Python packages if a supported version is not already present and installations and upgrades are enabled.
- Install or update the `pip` package for Python.
- Ensure that the installed Python versions and `pip` are properly configured and updated.

# Requirements

- Root or `sudo` privileges are required on the target host to install system packages.
- Network access to package repositories (for system packages) and PyPI (for pip).

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cloudera_manager_version` | `str` | `True` | | The version of Cloudera Manager to use for determining Python version requirements. |
| `cloudera_runtime_version` | `str` | `True` | | The version of Cloudera Runtime to use for determining Python version requirements. |
| `python_packages` | `list[str]` | `False` | - | Optional names of the Python packages to install. This is only used when a supported version of Python is not found. If not specified, the role will use OS-specific default package names. |
| `python_pip_packages` | `list[str]` | `False` | `[ python-pip ]` | The names of the Python pip packages to be installed or updated. |
| `prereq_python_upgrade` | `bool` | `False` | `true` | Flag to enable Python installation or upgrade if a supported version is not present. If `true`, the latest supported version or the `python_packages` will be installed. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Install Python for Cloudera Manager 7.11.3 / Cloudera Runtime 7.1.9
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_python
      vars:
        cloudera_manager_version: 7.11.3
        cloudera_runtime_version: 7.1.9

    - name: Install Python with custom package names
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_python
      vars:
        cloudera_manager_version: 7.11.3
        cloudera_runtime_version: 7.1.9
        python_packages:
          - python39 # Example custom package name for Python 3.9
        python_pip_package:
          - python3-pip
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
