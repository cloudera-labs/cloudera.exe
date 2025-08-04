# prereq_kafka

Set up for Kafka

This role prepares a host for Apache Kafka usage by creating dedicated system users and groups for both `kafka` and `cruisecontrol`. These users are essential for running their respective services with appropriate permissions and isolation.

The role will:
- Create the `kafka` system user and group.
- Create the `cruisecontrol` system user and group.
- Configure home directories and other necessary local paths for these users, if required.
- Ensure appropriate permissions are set for files and directories related to Kafka and Cruise Control.

# Requirements

- Root or `sudo` privileges are required on the target host to create system users and groups.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| | | | | This role has no configurable parameters. |

# Example Playbook

```yaml
- hosts: kafka_nodes
  tasks:
    - name: Set up the kafka and cruisecontrol users and environment
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_kafka
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
