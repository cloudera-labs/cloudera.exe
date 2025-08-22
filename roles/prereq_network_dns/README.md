# prereq_network_dns

Set up hostname and DNS networking

This role automates the configuration of a host's networking settings, including its hostname and DNS. It is designed to work with various system-level network configuration tools like `cloud-init`, `NetworkManager`, `Netplan`, and `dhclient`. The role is crucial for ensuring proper name resolution and consistent IP address configuration within a cluster or managed environment.

The role will:
- Set the hostname of the target host.
- Configure DNS settings, including the search domain (`network_dns_domain`).
- Configure a list of DNS forwarders for name resolution (`network_dns_forwarders`).
- Apply these configurations to the appropriate network management system (`cloud-init`, `dhclient`, `netplan`, etc.) on the host.
- Set a static IP address or ensure a specific IP is used as the default for the host.

# Requirements

- Root or `sudo` privileges are required on the target host to modify system and network configuration files.
- This role assumes the presence of one of the targeted network configuration systems on the host (e.g., `NetworkManager` on Red Hat-based systems or `Netplan` on Ubuntu).

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `network_cloud_init_path` | `path` | `False` | `/etc/cloud/cloud.cfg` | Path to the `cloud-init` configuration file. The role will manage this file if it exists. |
| `network_dhclient_path` | `path` | `False` | `/etc/dhcp/dhclient.conf` | Path to the DHCP client configuration file. |
| `network_netplan_dir` | `path` | `False` | `/etc/netplan` | Path to the Netplan configuration directory. |
| `network_dns_domain` | `str` | `True` | | The DNS search domain for the host (e.g., `example.internal`). |
| `network_dns_forwarders` | `list` of `str` | `True` | | A prioritized list of DNS name server IP addresses to be used for name resolution. |
| `network_ip_address` | `str` | `True` | | The IP address of the host that the role should configure as the default. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Set up network for a cluster node
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_network_dns
      vars:
        network_dns_domain: "example.internal"
        network_dns_forwarders:
          - "10.0.0.10"
          - "8.8.8.8"
        network_ip_address: "10.0.1.100"
        # The other optional path variables will use their defaults and will be managed if those files exist.
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
