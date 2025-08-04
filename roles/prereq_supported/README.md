# prereq_supported

Verify configuration against support matrix

This role verifies various system and configuration settings on a target host against the official Cloudera on-premises support matrix, which is available at [supportmatrix.cloudera.com/](https://supportmatrix.cloudera.com). It is designed to be run early in a deployment pipeline to ensure that the environment meets all prerequisites before proceeding with the installation of Cloudera products. Additionally, the role defines and makes available a `support_matrix` variable that can be imported and utilized by other roles for their own specific verification needs.

The role will:
- Collect system facts about the target host (OS version, kernel, etc.).
- Compare these facts against the requirements defined in the internal `support_matrix` data structure for the specified versions of Cloudera Manager, Cloudera Runtime, and Data Services.
- Log any discrepancies or unsupported configurations.
- The `support_matrix` variable will be available for use in subsequent tasks or roles within the same playbook.

# Requirements

- This role is intended to be run on the target hosts to gather accurate system facts.
- It requires a well-defined `support_matrix` data structure in its internal variables that corresponds to the official Cloudera support matrix.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cloudera_manager_version` | `str` | `True` | | The version of Cloudera Manager to validate against. |
| `cloudera_runtime_version` | `str` | `True` | | The version of Cloudera Runtime to validate against. |
| `data_services_version` | `str` | `False` | | The version of Cloudera Data Services to validate against. This is an optional parameter. |

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
        data_services_version: "1.0.0" # Optional parameter

    - name: Use the support matrix variable in a subsequent task
      ansible.builtin.debug:
        msg: "The supported Python version is {{ support_matrix.python_version }}"
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
