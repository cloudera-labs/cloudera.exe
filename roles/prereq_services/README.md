# prereq_services

Manage operating system services

This role is designed to manage operating system services to meet the specific requirements of a Cloudera on-premises deployment. It takes a proactive approach by disabling services that are typically unnecessary in a cluster environment and ensuring that essential services, such as the Name Service Cache Daemon (NSCD), are installed, configured, and running.

The role will:
- Install the `nscd` package and ensure the corresponding service is enabled and started.
- Iterate through a list of unnecessary services, stopping and disabling each one to reduce system overhead and potential security risks.
- Ensure all services are in the correct state (either running and enabled, or stopped and disabled) to match the desired configuration.

# Requirements

- Root or `sudo` privileges are required on the target host to manage system packages and services.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `prereq_services_unnecessary_services` | `list` of `str` | `False` | `["bluetooth", "cups", "postfix"]` | A list of OS service names that will be stopped and disabled. |
| `prereq_services_nscd_package` | `str` | `False` | `nscd` | The name of the package for the Name Service Cache Daemon (NSCD) to install. This may vary between OS distributions. |
| `prereq_services_nscd_service` | `str` | `False` | `nscd` | The name of the NSCD service to enable and start. This may vary between OS distributions. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Manage default OS services for Cloudera
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_services
      # This will install nscd and disable bluetooth, cups, and postfix.

    - name: Manage OS services with a custom list of unnecessary services
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_services
      vars:
        prereq_services__unnecessary_services:
          - avahi-daemon
          - auditd
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
