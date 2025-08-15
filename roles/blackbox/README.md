# blackbox_exporter

Install Blackbox Exporter

This role handles the download, installation, and configuration of the Prometheus Blackbox Exporter on a Linux host. The Blackbox Exporter is used to probe endpoints over various protocols, and this role ensures it is set up as a systemd service, running under a dedicated user and group, ready for configuration and use with Prometheus.

The role will:
- Create a dedicated system user and group (`blackbox`) for the service.
- Download the specified Blackbox Exporter tarball from the provided URL.
- Extract the Blackbox Exporter binary to the configured binary directory (`/usr/local/bin` by default).
- Set up a systemd service file for Blackbox Exporter.
- Ensure the Blackbox Exporter service is running and enabled on system boot.

# Requirements

- A running `systemd` instance for service management.
- Internet access on the target host to download the Blackbox Exporter tarball.
- Root or `sudo` privileges are required to manage packages, users, and system services.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `blackbox_tarball_url` | `str` | `False` | `https://github.com/prometheus/blackbox_exporter/releases/download/v0.24.0/blackbox_exporter-0.24.0.linux-amd64.tar.gz` | URL to the Blackbox Exporter distribution archive file. |
| `blackbox_directory` | `path` | `False` | `/etc/blackbox` | The directory for Blackbox Exporter configuration files. |
| `blackbox_bin_directory` | `path` | `False` | `/usr/local/bin` | The directory where the Blackbox Exporter binary will be placed. |
| `blackbox_tarball_file` | `str` | `False` | `blackbox.tar.gz` | The intermediate filename to use for the downloaded tarball. |
| `blackbox_user` | `str` | `False` | `blackbox` | The system username under which the Blackbox Exporter service will run. |
| `blackbox_group` | `str` | `False` | `blackbox` | The system group under which the Blackbox Exporter service will run. |
| `blackbox_service_directory` | `path` | `False` | `/etc/systemd/system/blackbox.service` | Full path to the systemd service file for Blackbox Exporter. |

# Example Playbook

```yaml
- hosts: monitoring_targets
  tasks:
    - name: Install Blackbox Exporter with default settings
      ansible.builtin.import_role:
        name: cloudera.exe.blackbox_exporter
      # All variables will use their defaults.

    - name: Install a custom version of Blackbox Exporter
      ansible.builtin.import_role:
        name: cloudera.exe.blackbox_exporter
      vars:
        blackbox_tarball_url: "[https://github.com/prometheus/blackbox_exporter/releases/download/v0.25.0/blackbox_exporter-0.25.0.linux-amd64.tar.gz](https://github.com/prometheus/blackbox_exporter/releases/download/v0.25.0/blackbox_exporter-0.25.0.linux-amd64.tar.gz)"
        blackbox_tarball_file: "blackbox-0.25.0.tar.gz"
        blackbox_user: "prom_exporter"
        blackbox_group: "prom_exporter"
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
