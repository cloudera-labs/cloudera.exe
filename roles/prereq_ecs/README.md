# prereq_ecs

Set up for ECS

This role prepares a host for Cloudera's ECS (Embedded Container Service) usage by creating the required local users and configuring the firewall and network settings. It ensures that the host's environment is properly configured to support ECS components and operations, including user permissions and network security rules.

The role will:
- Create the necessary system users and groups for ECS, based on a list provided by the `prereq_cloudera_manager` role.
- Configure firewall rules to allow traffic required by ECS components.
- Set up networking configurations to ensure proper communication within the ECS environment.

# Requirements

- Root or `sudo` privileges are required on the target host to manage system users, firewall rules, and network configurations.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| | | | | This role has no configurable parameters. |

# Example Playbook

```yaml
- hosts: ecs_nodes
  tasks:
    - name: Set up the host for ECS usage
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_ecs
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
