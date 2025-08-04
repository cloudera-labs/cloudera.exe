# prereq_hue

Set up for Hue

This role prepares a host for Hue usage by creating a dedicated system user and group named `hue`. This user is essential for running Hue processes with appropriate permissions and isolation. The role also handles configuration for Hue's Kerberos and TLS requirements, including setting up ACLs on TLS entities and updating Kerberos encryption types.

The role will:
- Create the `hue` system user and group.
- Configure home directories and other necessary local paths for the `hue` user, if required.
- Ensure appropriate permissions are set for files and directories related to Hue.
- Optionally, set up TLS ACLs to secure Hue communication, if needed.
- Optionally, update Kerberos encryption types as required for Hue's secure operations.

# Requirements

- Root or `sudo` privileges are required on the target host to create system users and groups, and to configure file system permissions and system files.
- The Kerberos configuration file at `kerberos_config_path` must exist on the target host or be managed by another role.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `kerberos_config_path` | `path` | `False` | `/etc/krb5.conf` | Path to the Kerberos configuration file on the target host. This file will be configured for Hue's Kerberos settings. |

# Example Playbook

```yaml
- hosts: hue_nodes
  tasks:
    - name: Set up the hue user and default Kerberos configuration
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_hue

    - name: Set up the hue user with a custom Kerberos configuration path
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_hue
      vars:
        kerberos_config_path: "/etc/custom/krb5.conf"
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
