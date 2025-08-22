# prereq_rngd

Install the Random Number Generator package

This role installs and configures the Random Number Generator Daemon (`rngd`) package on a host. The daemon is essential for ensuring that the system has a sufficient amount of entropy available for cryptographic operations, which is crucial for secure communications and services.

**NOTE** This role should only be used when run on virtual machine (VM); guard role execution by using the conditional `ansible_virtualization_role == 'guest'`.

The role will:
- Install the `rngd` package using the system's package manager.
- Ensure the `rngd` service is enabled and started, so that it can continuously feed entropy from a hardware random number generator to the kernel's entropy pool.

# Requirements

- Root or `sudo` privileges are required on the target host to install and manage system packages and services.

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
    - name: Install and configure the Random Number Generator daemon
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_rngd

    - name: Install and configure with the virtualization conditional
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_rngd
      when: ansible_virtualization_role == 'guest'
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
