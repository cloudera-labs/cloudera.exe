# prereq_jdk

Set up JDK

This role automates the setup of a Java Development Kit (JDK) on a host. It can optionally install the JDK packages from various providers (OpenJDK, Oracle, Azul), handle version management, and perform post-installation configuration. For older JDK versions (9 and below), it can also enable the Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy to support stronger encryption.

This role also verifies the JDK on target host against the official Cloudera on-premises support matrix, which is available at [supportmatrix.cloudera.com/](https://supportmatrix.cloudera.com). It is designed to be run early in a deployment pipeline to ensure that the environment meets the JDK prerequisites before proceeding with the installation of Cloudera products.

The role will:
- Install the specified JDK packages if `jdk_install_packages` is `true`.
- For JDK versions 8 and below, it will apply the JCE Unlimited Strength Jurisdiction Policy if needed, by modifying `java.security` files.
- If multiple `java.security` files are found during JCE configuration, it will either proceed or halt based on the `jdk_security_paths_override` flag.
- For JDKs installed from Cloudera's repository, the role will ensure that any missing symbolic links are created to support a consistent JDK installation path.
- Compare JDK against the support matrix at [supportmatrix.cloudera.com/](https://supportmatrix.cloudera.com) for the specified versions of Cloudera Manager and Cloudera Runtime.

# Requirements

- Root or `sudo` privileges are required to install packages and modify system-wide configuration files.
- Network access to the package repositories for the chosen JDK provider.
- Access to the [supportmatrix.cloudera.com/](https://supportmatrix.cloudera.com) site.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `jdk_provider` | `str` | `False` | `openjdk` | The JDK vendor or provider to use for installation. Valid choices are `openjdk`, `oracle`, and `azul`. |
| `jdk_install_packages` | `bool` | `False` | `True` | Flag to enable or disable the installation of JDK packages. If `false`, the role will assume a JDK is already installed and will only perform configuration tasks. |
| `jdk_packages` | `list` of `str` | `False` | - | A list of OS packages to install if `jdk_install_packages` is `true`. If not specified, the role will use default package names based on `jdk_provider` and `jdk_version`. |
| `jdk_version` | `int` | `False` | `17` | The supported JDK version to install. Valid choices are `8`, `11`, and `17`. |
| `jdk_security_paths` | `list` of `path` | `False` | - | A list of paths to search for `java.security` files. The role will only apply JCE changes to files in these locations. |
| `jdk_security_paths_override` | `bool` | `False` | `False` | Flag to control behavior when multiple `java.security` files are found in the specified paths. If `true`, the role will continue with JCE changes even if multiple files are found. If `false`, the role will fail, requiring a more specific path list. |
| `cloudera_manager_version` | `str` | `True` | | The version of Cloudera Manager to validate against. |
| `cloudera_runtime_version` | `str` | `True` | | The version of Cloudera Runtime to validate against. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Set up default OpenJDK 17 installation
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_jdk
      vars:
        cloudera_manager_version: "7.11.3"
        cloudera_runtime_version: "7.1.9"
      # All variables will use their defaults, installing OpenJDK 17.

    - name: Set up Oracle JDK 11 without installing packages
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_jdk
      vars:
        jdk_provider: oracle
        jdk_version: 11
        jdk_install_packages: false # Assume JDK 11 is already installed
        cloudera_manager_version: "7.11.3"
        cloudera_runtime_version: "7.1.9"

    - name: Set up OpenJDK 8 with JCE policy
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_jdk
      vars:
        jdk_version: 8
        # Since version 8 is used, JCE enablement will be attempted.
        jdk_security_paths:
          - /etc/java/security/
        jdk_security_paths_override: false
        cloudera_manager_version: "7.11.3"
        cloudera_runtime_version: "7.1.9"
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
