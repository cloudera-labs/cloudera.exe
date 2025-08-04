# grafana_server

Set up Grafana server, connected to a Prometheus server.

The role will:
- Install the Grafana server package(s).
- Configure Grafana data sources, primarily for Prometheus, based on the provided `prometheus_url`.
- Configure Grafana dashboard providers.
- Provision a default dashboard.

## Requirements

- A running Prometheus server accessible from the Grafana host.

## Dependencies

None.

## Role Variables (Argument Specification)

| Parameter                        | Type | Default Value                                   | Description                                                               |
|----------------------------------|------|-------------------------------------------------|---------------------------------------------------------------------------|
| `grafana_datasource_directory`   | `str`| `/etc/grafana/provisioning/datasources/automatic.yml`| Location of the Grafana data sources configuration file.                 |
| `grafana_providers_configuration`| `str`| `/etc/grafana/provisioning/dashboards/providers.yml` | Location of the Grafana dashboard provider configurations file.          |
| `grafana_dashboard_directory`    | `str`| `/var/lib/grafana/dashboards`                   | Location of the Grafana dashboard configurations directory.              |
| `prometheus_url`                 | `str`| `localhost:9090`                                | URL (host:port) to the Prometheus server that Grafana will connect to.   |

## Examples

Basic installation connecting to a local Prometheus server:

```yaml
- name: Set up Grafana server with local Prometheus
  ansible.builtin.import_role:
    name: grafana_server
  # No variables needed here as defaults will be used for local Prometheus

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
