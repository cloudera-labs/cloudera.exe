# prereq_supported

Verify configuration against support matrix

This role verifies various system and configuration settings on a target host against the official Cloudera on-premises support matrix, which is available at [supportmatrix.cloudera.com/](https://supportmatrix.cloudera.com). It is designed to be run early in a deployment pipeline to ensure that the environment meets all prerequisites before proceeding with the installation of Cloudera products.

The role will:
- Collect system facts about the target host (OS version, kernel, etc.).
- Compare these facts against the requirements defined by the support matrix at [supportmatrix.cloudera.com/](https://supportmatrix.cloudera.com) for the specified versions of Cloudera Manager, Cloudera Runtime, and Data Services.
- Log any discrepancies or unsupported configurations.

# Requirements

- This role is intended to be run on the target hosts to gather accurate system facts.
- Access to the [supportmatrix.cloudera.com/](https://supportmatrix.cloudera.com) site.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cloudera_manager_version` | `str` | `True` | | The version of Cloudera Manager to validate against. |
| `cloudera_runtime_version` | `str` | `True` | | The version of Cloudera Runtime to validate against. |
| `cloudera_data_services_version` | `str` | `False` | | The version of Cloudera Data Services to validate against. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Verify host configuration against support matrix
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_supported
      vars:
        cloudera_manager_version: "7.11.3"
        cloudera_runtime_version: "7.1.9"
        cloudera_data_services_version: "1.0.0" # Optional parameter
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
