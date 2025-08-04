# prereq_ntp

Manage NTP Services

This role manages NTP (Network Time Protocol) services on a host, with a focus on using Chrony as the preferred time synchronization service. It intelligently handles different states of NTP service installation and operation to ensure that a single, reliable time service is active.

The role will:
- Check for the presence of both the `chrony` and `ntp` services.
- If neither service is installed or running, it will install the `chrony` package.
- If both `chrony` and `ntp` services are found to be installed and running, it will stop and disable the `ntp` service to prevent conflicts and prioritize `chrony`.
- Ensure the selected time synchronization service (`chrony`) is running and enabled on system boot.

# Requirements

- Root or `sudo` privileges are required on the target host to install and manage system packages and services.
- Network access from the target host to configured NTP servers for time synchronization.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| | | | | This role has no configurable parameters. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Manage NTP services to prioritize Chrony
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_ntp
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
