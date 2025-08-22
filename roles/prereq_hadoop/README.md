# prereq_hadoop

Set up for Hadoop

This role prepares a host for Apache Hadoop usage by creating a dedicated system group named `hadoop`. This group is essential for managing file system permissions and user access within a Hadoop environment.

The role will:
- Create the `hadoop` system group.
- Ensure appropriate permissions are set for files and directories that will be used by the Hadoop services and belong to the `hadoop` group.

# Requirements

- Root or `sudo` privileges are required on the target host to create system groups.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| | | | | This role has no configurable parameters. |

# Example Playbook

```yaml
- hosts: hadoop_nodes
  tasks:
    - name: Set up the hadoop group and environment
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_hadoop
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
