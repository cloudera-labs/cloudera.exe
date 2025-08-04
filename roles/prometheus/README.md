# prometheus

Install Prometheus.

This role automates the installation of the Prometheus monitoring system from its official distribution archive. It sets up the necessary directories for configuration and the time-series database (TSDB), creates a dedicated system user and group for the service, and installs a basic Prometheus configuration to get started.

The role will:
- Create a dedicated system user and group (`prometheus`).
- Create necessary directories for Prometheus configuration (`/etc/prometheus`) and TSDB storage (`/var/lib/prometheus`).
- Download the Prometheus distribution tarball.
- Extract the Prometheus binary and related files to the installation directory.
- Install a basic `prometheus.yml` configuration file.
- Set up a `systemd` service for Prometheus.
- Enable and start the Prometheus service, ensuring it runs on system boot.

# Requirements

- Target host must have `systemd` for service management.
- Internet access on the target host to download the Prometheus tarball.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `prometheus_tarball_url` | `str` | `False` | `https://github.com/prometheus/prometheus/releases/download/v2.48.1/prometheus-2.48.1.linux-amd64.tar.gz` | URL to the Prometheus distribution archive file. |
| `prometheus_directory` | `path` | `False` | `/etc/prometheus` | Prometheus configuration directory. |
| `prometheus_tsdb_directory` | `path` | `False` | `/var/lib/prometheus` | Prometheus TSDB directory. |
| `prometheus_tarball_file` | `str` | `False` | `prometheus.tar.gz` | Intermediate archive file name for the downloaded tarball. |
| `prometheus_user` | `str` | `False` | `prometheus` | Prometheus service user. |
| `prometheus_group` | `str` | `False` | `prometheus` | Prometheus service group. |
| `prometheus_service_directory` | `path` | `False` | `/etc/systemd/system/prometheus.service` | Prometheus Systemd service directory (full path to the service file). |

# Example Playbook

```yaml
- hosts: monitoring_servers
  tasks:
    - name: Install Prometheus server with custom settings
      ansible.builtin.import_role:
        name: prometheus
      vars:
        prometheus_tarball_url: "[https://github.com/prometheus/prometheus/releases/download/v2.49.0/prometheus-2.49.0.linux-amd64.tar.gz](https://github.com/prometheus/prometheus/releases/download/v2.49.0/prometheus-2.49.0.linux-amd64.tar.gz)"
        prometheus_directory: "/opt/prometheus/config"
        prometheus_tsdb_directory: "/data/prometheus_tsdb"
        prometheus_user: "prom_admin"
        prometheus_group: "prom_admin"
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
