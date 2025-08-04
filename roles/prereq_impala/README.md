# prereq_impala

Set up for Impala

This role prepares a host for Apache Impala usage by creating a dedicated system user and group named `impala`. This user is essential for running Impala processes with appropriate permissions and isolation. The role can also optionally configure TLS for Impala communication, including managing keystore, private key, and password files, and setting up file system permissions for these entities.

The role will:
- Create the `impala` system user and group.
- Configure home directories and other necessary local paths for the `impala` user, if required.
- Ensure appropriate permissions are set for files and directories related to Impala.
- If TLS is enabled via the provided parameters, the role will:
    - Set up Access Control Lists (ACLs) on TLS-related files.
    - Manage hardlinks for TLS files as needed for generic paths.
    - Ensure TLS key password files are securely configured.

# Requirements

- Root or `sudo` privileges are required on the target host to create system users and groups, and to configure file system permissions and ACLs.
- If any TLS path parameters are specified, the corresponding certificate, key, and password files must exist on the target host or be managed by another role.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `tls_keystore_path` | `path` | `False` | | Path to the TLS keystore file. |
| `tls_keystore_path_generic` | `path` | `False` | | Path to a hardlink that points to the TLS keystore. Used to provide a consistent, generic path. |
| `tls_key_path` | `path` | `False` | | Path to the encrypted TLS private key file. |
| `tls_key_path_generic` | `path` | `False` | | Path to a hardlink that points to the encrypted TLS private key. |
| `tls_key_password_file` | `path` | `False` | | Path to the file containing the password for the TLS private key. |
| `tls_key_path_plaintext` | `path` | `False` | | Path to the unencrypted TLS private key file. |
| `tls_key_path_plaintext_generic` | `path` | `False` | | Path to a hardlink that points to the unencrypted TLS private key. |

# Example Playbook

```yaml
- hosts: impala_nodes
  tasks:
    - name: Set up the impala user and environment without TLS
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_impala

    - name: Set up impala with TLS configuration
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_impala
      vars:
        tls_keystore_path: "/opt/certs/impala/keystore.jks"
        tls_key_path: "/opt/certs/impala/impala.key"
        tls_key_password_file: "/opt/certs/impala/password.txt"
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
