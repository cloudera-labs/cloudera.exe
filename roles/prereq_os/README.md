# prereq_os

Update general OS requirements.

This role updates general operating system requirements to prepare a host for a Cloudera deployment. It sets the system's timezone and addresses specific file permission requirements for the global `/tmp` directory on certain operating systems.

The role will:
- Set the host's timezone using the `os_timezone` variable.
- Ensure that the global `/tmp` directory has correct permissions to allow access for Cloudera Manager services.
- Specifically on Ubuntu 20.04, it will adjust root permissions on the global `/tmp` directory to comply with operational requirements.

# Requirements

- Root or `sudo` privileges are required on the target host to update the system timezone and modify directory permissions.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `os_timezone` | `str` | `False` | `UTC` | The timezone to set on the host. This should be a valid timezone string (e.g., `America/New_York`, `Europe/London`). |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Update OS requirements with default UTC timezone
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_os

    - name: Update OS requirements with a specific timezone
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_os
      vars:
        os_timezone: "America/Denver"
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
