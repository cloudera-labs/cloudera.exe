# MiNiFi C++ Agent

This role streamlines the deployment and configuration of Cloudera MiNiFi C++ Agent on designated hosts.

The role will:
- Retrieves the MiNiFi C++ tarball from a user-defined or default source
- Installs MiNiFi C++ into a configurable directory
- Applies configuration using a Jinja2 template for `minifi.properties`
- Configures C2 protocol for communication with EFM server
- Supports TLS/SSL configuration for secure communication
- Installs and starts the MiNiFi C++ agent service
- Supports authentication for protected download sources

## Requirements

- Network access from the target host to the URL specified in `minifi_cpp_tarball_url`
- Access to EFM server for C2 communication (specified in `efm_host_url`)
- For TLS configuration: Valid certificates and private keys on target host

## Variables

| Name                            | Purpose                                                      | Default (see `defaults/main.yml`)           |
|----------------------------------|--------------------------------------------------------------|---------------------------------------------|
| `minifi_cpp_tarball_url`        | Download link for the MiNiFi C++ tarball                    | (default provided in role)                  |
| `minifi_cpp_directory`          | Installation directory for MiNiFi C++                       | `/opt/cloudera/cem/minifi-cpp`              |
| `minifi_cpp_properties_path`    | Path to the MiNiFi C++ properties file                      | `/opt/cloudera/cem/minifi-cpp/conf/minifi.properties` |
| `minifi_cpp_agent_class_name`   | Agent class name for MiNiFi C++ agent                       | `minifi-agent-cpp`                          |
| `efm_host_url`                  | URL for the EFM server for C2 communication                 | `http://localhost:10090`                    |
| `minifi_cpp_repo_username` | Username for protected repositories (optional)               |                                             |
| `minifi_cpp_repo_password` | Password for protected repositories (optional)               |                                             |
| `minifi_tls_enabled`            | Enable/disable TLS for MiNiFi C++ agent                     | `false`                                     |
| `minifi_tls_client_certificate` | Path to client certificate file for TLS authentication      | `/etc/pki/tls/certs/host.crt`              |
| `minifi_tls_client_private_key` | Path to client private key file for TLS authentication      | `/etc/pki/tls/private/host.key`            |
| `minifi_tls_client_ca_certificate` | Path to CA certificate file for TLS authentication       | `/etc/ipa/ca.crt`                          |

## Example usage

```yaml
# Basic MiNiFi C++ installation
- hosts: minifi_nodes
  become: true
  tasks:
    - name: Install MiNiFi C++ with basic configuration
      ansible.builtin.import_role:
        name: cloudera.exe.minifi_agent_cpp
      vars:
        minifi_cpp_repo_username: "repo_user"
        minifi_cpp_repo_password: "repo_pass"
        efm_host_url: "http://efm-server:10090"
        minifi_cpp_agent_class_name: "production-agents"

    - name: Install MiNiFi C++ with TLS enabled
      ansible.builtin.import_role:
        name: cloudera.exe.minifi_agent_cpp
      vars:
        efm_host_url: "https://efm-server:10090"
        minifi_cpp_agent_class_name: "secure-agents"
        # TLS Configuration
        minifi_tls_enabled: true
        minifi_tls_client_certificate: "/etc/pki/tls/certs/minifi.crt"
        minifi_tls_client_private_key: "/etc/pki/tls/private/minifi.key"
        minifi_tls_client_ca_certificate: "/etc/ipa/ca.crt"
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
