# MiNiFi Java Agent

This role streamlines the deployment and configuration of Cloudera MiNiFi Java Agent on designated hosts.

The role will:
- Retrieve the MiNiFi Java tarball from a user-defined or default source
- Install MiNiFi Java into a configurable directory
- Apply configuration using a Jinja2 template for `minifi.properties`
- Configure C2 protocol for communication with EFM server
- Support TLS/SSL configuration for secure communication
- Install and start the MiNiFi Java agent service
- Support authentication for protected download sources

## Requirements

- Network access from the target host to the URL specified in `minifi_java_tarball_url`
- Access to EFM server for C2 communication (specified in `efm_host_url`)
- For TLS configuration: Valid certificates and private keys on target host

## Variables

| Name                            | Purpose                                                      | Default (see `defaults/main.yml`)           |
|----------------------------------|--------------------------------------------------------------|---------------------------------------------|
| `minifi_java_tarball_url`        | Download link for the MiNiFi Java tarball                   | (default provided in role)                  |
| `minifi_java_directory`          | Installation directory for MiNiFi Java                      | `/opt/cloudera/cem/minifi-java`              |
| `minifi_java_properties_path`    | Path to the MiNiFi Java properties file                     | `/opt/cloudera/cem/minifi-java/conf/minifi.properties` |
| `minifi_java_agent_class_name`   | Agent class name for MiNiFi Java agent                      | `minifi-agent-java`                          |
| `efm_host_url`                  | URL for the EFM server for C2 communication                 | `http://localhost:10090`                    |
| `minifi_java_repo_username` | Username for protected repositories (optional)               |                                             |
| `minifi_java_repo_password` | Password for protected repositories (optional)               |                                             |
| `minifi_tls_enabled`            | Enable/disable TLS for MiNiFi Java agent                    | `false`                                     |
| `minifi_tls_client_certificate` | Path to client certificate file for TLS authentication      | `/etc/pki/tls/certs/host.crt`              |
| `minifi_tls_client_private_key` | Path to client private key file for TLS authentication      | `/etc/pki/tls/private/host.key`            |
| `minifi_tls_client_ca_certificate` | Path to CA certificate file for TLS authentication       | `/etc/ipa/ca.crt`                          |
| `minifi_java_service_path`       | Path to the systemd service file for MiNiFi Java.          | `/etc/systemd/system/minifi-java.service` |
| `minifi_tls_keystore_path`       | Path to the keystore file for TLS configuration.           |                                             |
| `minifi_tls_keystore_type`       | Type of the keystore (e.g., JKS, PKCS12).                  |                                             |
| `minifi_tls_keystore_password`   | Password for the keystore file.                            |                                             |
| `minifi_tls_key_password`        | Password for the private key in the keystore.              |                                             |
| `minifi_tls_truststore_path`     | Path to the truststore file for TLS configuration.         |                                             |
| `minifi_tls_truststore_type`     | Type of the truststore (e.g., JKS, PKCS12).                |                                             |
| `minifi_tls_truststore_password` | Password for the truststore file.                          |                                             |
| `minifi_tls_ssl_protocol`        | SSL protocol to use for TLS communication (e.g., TLSv1.2). |                                             |

## Example usage

```yaml
# Basic MiNiFi Java installation
- hosts: minifi_nodes
  become: true
  tasks:
    - name: Install MiNiFi Java with basic configuration
      ansible.builtin.import_role:
        name: cloudera.exe.minifi_agent_java
      vars:
        minifi_java_repo_username: "repo_user"
        minifi_java_repo_password: "repo_pass"
        efm_host_url: "http://efm-server:10090"
        minifi_java_agent_class_name: "java-agent"
# MiNiFi Java installation with TLS configuration
- hosts: minifi_nodes
  become: true
  tasks:
    - name: Install MiNiFi Java with TLS enabled
      ansible.builtin.import_role:
        name: cloudera.exe.minifi_agent_java
      vars:
        efm_host_url: "https://efm-server:10090"
        minifi_tls_enabled: true
        minifi_tls_keystore_path: "/etc/pki/tls/keystore.jks"
        minifi_tls_keystore_password: "keystore_password"
        minifi_tls_truststore_path: "/etc/pki/tls/truststore.jks"
        minifi_tls_truststore_password: "truststore_password"
        minifi_tls_ssl_protocol: "TLSv1.2"
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
