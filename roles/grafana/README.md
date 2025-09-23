
# grafana

Automates the installation and configuration of a Grafana server, with Prometheus integration for monitoring and observability.

## Features

- Installs Grafana using OS-specific package management for major Linux distributions (Ubuntu, CentOS, RedHat, Rocky).
- Configures core Grafana server settings, including protocol (HTTP/HTTPS), port, domain, and root URL.
- Optionally enables HTTPS/TLS for secure access, with configurable certificate and key paths.
- Allows setting a custom admin password for the Grafana web interface.
- Provisions Prometheus as a data source, with the ability to specify a custom Prometheus endpoint.
- Configures dashboard providers and ensures dashboards are available at startup.
- Supports custom locations for data source and dashboard configuration files.
- Ensures idempotent and secure configuration changes, with sensitive values (like admin password) protected in logs.
- Designed for flexibility and easy extension to other monitoring backends or dashboard sources.

## How it works

1. Installs Grafana using the appropriate package manager for the detected OS.
2. Configures server and security settings in `grafana.ini`, including TLS and admin credentials if specified.
3. Provisions Prometheus as a data source and sets up dashboard providers using Jinja2 templates.
4. Ensures the dashboards directory exists and copies a default dashboard for immediate use.
5. Restarts or reloads the Grafana service as needed to apply configuration changes.

## Requirements

- A running Prometheus server accessible from the Grafana host.

## Dependencies

None.

## Role Variables (Argument Specification)

| Parameter                        | Type | Default Value                                   | Description                                                               |
|----------------------------------|------|-------------------------------------------------|---------------------------------------------------------------------------|
| `grafana_datasource_directory`   | `str` | `/etc/grafana/provisioning/datasources/automatic.yml` | Location of the Grafana data sources configuration file.                 |
| `grafana_providers_configuration`| `str` | `/etc/grafana/provisioning/dashboards/providers.yml`  | Location of the Grafana dashboard provider configurations file.          |
| `grafana_dashboard_directory`    | `str` | `/var/lib/grafana/dashboards`                        | Location of the Grafana dashboard configurations directory.              |
| `prometheus_url`                 | `str` | `http://localhost:9090`                              | URL (host:port) to the Prometheus server that Grafana will connect to.   |
| `prometheus_hostname`            | `str` | `localhost`                                          | Hostname of the Prometheus server for TLS server name verification.      |
| `grafana_tls_enabled`                    | `bool`| `false`                                              | Enable or disable TLS/SSL for Grafana (HTTPS support).                   |
| `grafana_tls_cert_path`          | `str` | `/etc/pki/tls/certs/grafana.crt`                     | Path to the TLS certificate file for Grafana.                            |
| `grafana_tls_key_path`           | `str` | `/etc/pki/tls/private/grafana.key`                   | Path to the TLS private key file for Grafana.                            |
| `grafana_domain`                 | `str` | `localhost`                                          | Domain name for the Grafana server (used in server configuration).       |
| `grafana_root_url`               | `str` | `http://localhost:3000`                              | The root URL for accessing Grafana (used in server configuration).       |
| `grafana_config_file`            | `str` | `/etc/grafana/grafana.ini`                           | Path to the main Grafana configuration file.                             |
| `grafana_http_port`              | `int` | `3000`                                               | HTTP port for Grafana to listen on.                                      |
| `grafana_security_admin_password`| `str` | `admin`                                              | Admin password for Grafana web interface.                                 |


## TLS/HTTPS Support

If `grafana_tls_enabled` is set to `true`, the role will configure Grafana to use HTTPS. You must provide valid certificate and key files at the specified paths (`grafana_tls_cert_path` and `grafana_tls_key_path`).

## Examples

Basic installation connecting to a local Prometheus server:

```yaml
- name: Set up Grafana server with local Prometheus
  ansible.builtin.import_role:
    name: grafana_server
- name: Set up Grafana server for a specific Prometheus endpoint
  ansible.builtin.import_role:
    name: grafana_server
  vars:
    prometheus_url: "http://my-prometheus-server.example.com:9090"

- name: Set up Grafana with custom provisioning directories
  ansible.builtin.import_role:
    name: grafana_server
  vars:
    grafana_datasource_directory: "/opt/grafana/configs/datasources.yml"
    grafana_providers_configuration: "/opt/grafana/configs/providers.yml"
    grafana_dashboard_directory: "/opt/grafana/dashboards_custom"
    prometheus_url: "http://monitoring-cluster.internal:9090"

- name: Set up Grafana server with TLS/HTTPS enabled
  ansible.builtin.import_role:
    name: grafana_server
  vars:
    grafana_tls_enabled: true
    grafana_security_admin_password: secretpassword
    grafana_domain: "grafana.1.1.1.1.pvc.labs.com"
    grafana_root_url: "https://grafana.1.1.1.1.pvc.labs.com:3000"
    grafana_tls_cert_path: "/etc/grafana/certs/grafana.crt"
    grafana_tls_key_path: "/etc/grafana/private/grafana.key"
    prometheus_url: "https://prometheus.example.com:9090"

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
