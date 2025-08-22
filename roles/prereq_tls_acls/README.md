# prereq_tls_acls

Set up local user ACLs for TLS

This role is designed to manage and validate file system ACLs for TLS-related entities, including keystores, private keys, and key password files. It operates in two distinct modes: a `main` mode to set the ACLs and a `validate` mode to check that the ACLs are correctly applied. The role's behavior is driven by a list of users and a set of flags that define which TLS entities each user should have access to.

Typically, TLS entity variables are set as `hostvars`.

The role will:
- **`main` mode**:
    - Iterate through the `acl_user_accounts` list.
    - For each specified user, it will apply `read` file ACLs for the users' `group` to the TLS keystore, encrypted private key, unencrypted private key, and password file, as directed by the corresponding Boolean flags (`keystore_acl`, `key_acl`, etc.).
    - It uses the specified TLS path variables to locate the files to which ACLs should be applied.
- **`validate` mode**:
    - Iterate through the `acl_user_accounts` list.
    - For each user and TLS entity, it will assert that the ACLs have been correctly set.
    - This mode is useful for verification in CI/CD pipelines or after an initial deployment.

# Requirements

- Root or `sudo` privileges are required on the target host to set file system ACLs.
- The users listed in `acl_user_accounts` must already exist on the target host.
- The TLS files (keystore, keys, password file) must exist on the target host at the specified paths.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `acl_user_accounts` | `list` of `dict` | `False` | `[]` | A list of user accounts to which ACLs will be applied or validated. Each item is a dictionary with the following keys. |
| &nbsp;&nbsp;&nbsp;&nbsp;`user` | `str` | `True` | | The name of the user account. |
| &nbsp;&nbsp;&nbsp;&nbsp;`keystore_acl` | `bool` | `False` | `false` | If `true`, sets an ACL for the user on the TLS keystore. |
| &nbsp;&nbsp;&nbsp;&nbsp;`key_acl` | `bool` | `False` | `false` | If `true`, sets an ACL for the user on the encrypted TLS private key. |
| &nbsp;&nbsp;&nbsp;&nbsp;`key_password_acl` | `bool` | `False` | `false` | If `true`, sets an ACL for the user on the TLS private key password file. |
| &nbsp;&nbsp;&nbsp;&nbsp;`unencrypted_key_acl` | `bool` | `False` | `false` | If `true`, sets an ACL for the user on the unencrypted TLS private key. |
| `tls_keystore_path` | `path` | `False` | | Path to the TLS keystore file. |
| `tls_keystore_path_generic` | `path` | `False` | | Path to a hardlink that points to the TLS keystore. |
| `tls_key_path` | `path` | `False` | | Path to the encrypted TLS private key file. |
| `tls_key_path_generic` | `path` | `False` | | Path to a hardlink that points to the encrypted TLS private key. |
| `tls_key_password_file` | `path` | `False` | | Path to the TLS private key password file. |
| `tls_key_path_plaintext` | `path` | `False` | | Path to the unencrypted TLS private key file. |
| `tls_key_path_plaintext_generic` | `path` | `False` | | Path to a hardlink that points to the unencrypted TLS private key. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Set ACLs for Impala and Solr TLS files
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_tls_acls
      vars:
        acl_user_accounts:
          - user: "impala"
            keystore_acl: true
            key_acl: true
            key_password_acl: true
          - user: "solr"
            keystore_acl: true
        tls_keystore_path: "/opt/tls/keystore.jks"
        tls_key_path: "/opt/tls/private.key"
        tls_key_password_file: "/opt/tls/password.txt"

    - name: Validate TLS ACLs for Impala
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_tls_acls
        tasks_from: validate # Use the 'validate' mode
      vars:
        acl_user_accounts:
          - user: "impala"
            keystore_acl: true
            key_acl: true
            key_password_acl: true
        tls_keystore_path: "/opt/tls/keystore.jks"
        tls_key_path: "/opt/tls/private.key"
        tls_key_password_file: "/opt/tls/password.txt"
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
