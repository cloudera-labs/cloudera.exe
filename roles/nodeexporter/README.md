# node_exporter

Install Node Exporter.

This role handles the download, installation, and configuration of the Prometheus Node Exporter on a Linux host. It ensures the Node Exporter is set up as a systemd service, running under a dedicated user and group, making it ready to expose host-level metrics for Prometheus scraping.

The role will:
- Create a dedicated system user and group for the Node Exporter service.
- Download the specified Node Exporter tarball from the provided URL.
- Extract the Node Exporter binary to the configured directory.
- Set up a systemd service file for Node Exporter.
- Enable and start the Node Exporter service, ensuring it runs on system boot.

## Requirements

- Target host must have `systemd` for service management.
- Internet access on the target host to download the Node Exporter tarball.

## Dependencies

None.

## Role Variables

| Parameter                        | Type | Default Value                                                                      | Required | Description                                     |
|----------------------------------|------|------------------------------------------------------------------------------------|----------|-------------------------------------------------|
| `node_exporter_directory`        | `path`| `/etc/node_exporter`                                                               | `false`  | The directory where Node Exporter will be installed. |
| `node_exporter_tarball_url`      | `str`| `https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz`| `false`  | URL to the Node Exporter installation package (tarball). |
| `node_exporter_tarball_file`     | `str`| `node_exporter.tar.gz`                                                             | `false`  | The intermediate filename to use for the downloaded tarball. |
| `node_exporter_service_directory`| `path`| `/etc/systemd/system/node_exporter.service`                                        | `false`  | Full path to the systemd service file for Node Exporter. |
| `node_exporter_user`             | `str`| `node_exporter`                                                                    | `false`  | The system username under which the Node Exporter service will run. |
| `node_exporter_group`            | `str`| `node_exporter`                                                                    | `false`  | The system group under which the Node Exporter service will run. |

## Examples

```yaml
- name: Install Node Exporter with default configuration
  ansible.builtin.import_role:
    name: node_exporter
  # No variables needed here as defaults will be used

- name: Install Node Exporter v1.8.0
  ansible.builtin.import_role:
    name: node_exporter
  vars:
    node_exporter_tarball_url: "https://github.com/prometheus/node_exporter/releases/download/v1.8.0/node_exporter-1.8.0.linux-amd64.tar.gz"
    node_exporter_tarball_file: "node_exporter-1.8.0.tar.gz" # Update filename for clarity

- name: Install Node Exporter with custom paths and user
  ansible.builtin.import_role:
    name: node_exporter
  vars:
    node_exporter_directory: "/opt/monitoring/node_exporter"
    node_exporter_service_directory: "/usr/lib/systemd/system/node_exporter.service" # Common location on some distros
    node_exporter_user: "prometheus_exporter"
    node_exporter_group: "prometheus_exporter"
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
