# prereq_smm

Set up for Streams Messaging Manager

This role prepares a host for Streams Messaging Manager (SMM) usage by creating dedicated system users and groups for SMM and Streams Replication Manager. It specifically creates the `streamsmsgmgr` and `streamsrepmgr` users. Additionally, it creates a symbolic link for the `streamsmsgmgr` user's home directory, which is a required step for the Custom Service Descriptor (CSD) installation.

The role will:
- Create the `streamsmsgmgr` and `streamsrepmgr` system users and groups.
- Configure home directories and other necessary local paths for these users.
- Ensure appropriate permissions are set for files and directories.
- Create a symbolic link for the `streamsmsgmgr` user's home directory to fulfill CSD installation requirements.

# Requirements

- Root or `sudo` privileges are required on the target host to create system users, groups, and symbolic links.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| | | | | This role has no configurable parameters. |

# Example Playbook

```yaml
- hosts: smm_nodes
  tasks:
    - name: Set up the SMM users and environment
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_smm
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
