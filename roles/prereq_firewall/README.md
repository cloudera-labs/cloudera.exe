# prereq_firewall

Disable firewalls

This role ensures that firewalls on the target host are disabled. It can intelligently back up existing firewall rules (for both IPv4 and IPv6) before disabling the service. This allows for a straightforward restoration of the original firewall state if needed.

The role will:
- Check for and stop active firewall services, such as `firewalld` or `iptables`.
- Create a backup of the current `iptables` rules for both IPv4 and IPv6 in a timestamped format. The backup directory defaults to the Ansible user's home directory. Backup file naming is `iptables-rules-[ipv4|ipv6].TIMESTAMP`, where `TIMESTAMP` is UTC.
- Disable firewall services from starting on boot.
- Flush all existing `iptables` rules to ensure an open network.

# Requirements

- Root or `sudo` privileges are required on the target host to manage system services and firewall rules.
- The target host must have `iptables` installed for the backup functionality to work. The role will likely also handle services like `firewalld` but its core backup feature is tied to `iptables`.

# Dependencies

- community.general.iptables_state

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `firewall_backup_enabled` | `bool` | `False` | `true` | Flag to enable timestamped backups of `iptables` rules before they are flushed. |
| `firewall_backup_dir` | `path` | `False` | `ansible_user` home directory | Path to the directory where the firewall rule backup files will be saved. |
| `firewall_backup_format` | `str` | `False` | `%Y%m%dT%H%M%S` | Timestamp format string to be used in the backup file names. The format uses standard `strftime` directives. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Disable firewalls and back up iptables rules
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_firewall
      # Backups are enabled by default and saved to the ansible user's home directory.

    - name: Disable firewalls without backing up iptables rules
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_firewall
      vars:
        firewall_backup_enabled: false

    - name: Disable firewalls with custom backup directory and format
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_firewall
      vars:
        firewall_backup_enabled: true
        firewall_backup_dir: "/root/firewall_backups"
        firewall_backup_format: "%Y-%m-%d_%H-%M-%S_UTC"
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
