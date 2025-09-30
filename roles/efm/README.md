# Edge Flow Manager

This role streamlines the deployment and configuration of Cloudera Edge Flow Manager (EFM) on designeted host. It covers the full installation workflow, from fetching the EFM package to setting up the service and applying configuration templates.

## What this role does

- Retrieves the EFM tarball from a user-defined or default source
- Installs EFM into a configurable directory
- Sets up the required system user and group for EFM
- Applies configuration using a Jinja2 template for `efm.properties`
- Installs and manages the EFM systemd service unit
- Adjusts permissions for all relevant files and directories
- Supports authentication for protected download sources

# Requirements

- Network access from the target host to the URL specified in `efm_tarball_url`.

## Variables

| Name                            | Purpose                                                      | Default (see `defaults/main.yml`)           |
|----------------------------------|--------------------------------------------------------------|---------------------------------------------|
| `efm_tarball_url`                | Download link for the EFM tarball                            | (default provided in role)                  |
| `efm_directory`                  | Installation directory for EFM                               | `/opt/cloudera/cem`                         |
| `efm_properties_directory`       | Path to the EFM properties file                              | `/opt/cloudera/cem/efm/conf/efm.properties` |
| `efm_service_directory`          | Location for the systemd service file                        | `/etc/systemd/system/efm.service`           |
| `efm_user`                       | System user for EFM                                          | `efm`                                       |
| `efm_group`                      | System group for EFM                                         | `efm`                                       |
| `cloudera_manager_repo_username` | Username for protected repositories (optional)               |                                             |
| `cloudera_manager_repo_password` | Password for protected repositories (optional)               |                                             |
| `efm_tls_enabled` | Enable/disable TLS for EFM server | `false` |
| `efm_ssl_client_auth` | SSL client authentication mode | `WANT` |
| `efm_ssl_keystore_type` | Type of keystore (jks, pkcs12) | `jks` |
| `efm_ssl_truststore_type` | Type of truststore (jks, pkcs12) | `jks` |
| `efm_ssl_keystore_path` | Path to SSL keystore (required when TLS enabled) | |
| `efm_ssl_keystore_password` | SSL keystore password (required when TLS enabled) | |
| `efm_ssl_key_password` | SSL private key password (required when TLS enabled) | |
| `efm_ssl_truststore_path` | Path to SSL truststore (required when TLS enabled) | |
| `efm_ssl_truststore_password` | SSL truststore password (required when TLS enabled) | |
| `efm_ldap_enabled` | Enable/disable LDAP authentication | `false` |
| `efm_ldap_url` | LDAP server URL (required when LDAP enabled) | |
| `efm_ldap_authentication_strategy` | LDAP authentication strategy | `LDAPS` |
| `efm_ldap_user_auth_groups_manager` | Authentication groups manager | `LDAP` |
| `efm_ldap_auth_enabled` | Enable LDAP authentication | `true` |
| `efm_ldap_auth_search_filter` | LDAP search filter for users | `(uid={0})` |
| `efm_ldap_user_search_base` | LDAP search base for users | `cn=users,cn=accounts,dc=cldr,dc=internal` |
| `efm_ldap_user_object_class` | LDAP object class for users | `person` |
| `efm_ldap_tls_protocol` | TLS protocol for LDAP connections | `TLSv1.2` |
| `efm_ldap_user_search_scope` | LDAP search scope | `ONE_LEVEL` |
| `efm_ldap_user_identity_attribute` | LDAP identity attribute | `uid` |
| `efm_db_url` | Database connection URL | `jdbc:postgresql://localhost:5432/efm` |
| `efm_db_driver_class` | Database driver class | `org.postgresql.Driver` |
| `efm_db_username` | Database username | `efm` |
| `efm_db_password` | Database password | `efmPassword` |

## Example usage

```yaml
# Basic EFM installation
- hosts: efm_nodes
  become: true
  tasks:
    - name: Install EFM with basic configuration
      ansible.builtin.import_role:
        name: efm
      vars:
        efm_tarball_url: "https://archive.cloudera.com/p/CEM/redhat9/2.x/updates/2.2.0.0/tars/efm/efm-2.2.0.0-1-bin.tar.gz"
        cloudera_manager_repo_username: "repo_user"
        cloudera_manager_repo_password: "repo_pass"
        efm_encryption_password: "MySecurePassword123"

    - name: Install EFM with TLS and LDAP enabled
      ansible.builtin.import_role:
        name: efm
      vars:
        efm_encryption_password: "MySecurePassword123"
        # TLS Configuration
        efm_tls_enabled: true
        efm_ssl_keystore_path: "/opt/cloudera/cem/certs/keystore.jks"
        efm_ssl_keystore_password: "MyKeystorePass"
        efm_ssl_key_password: "MyKeyPass"
        efm_ssl_truststore_path: "/opt/cloudera/cem/certs/truststore.jks"
        efm_ssl_truststore_password: "MyTruststorePass"
        # LDAP Configuration
        efm_ldap_enabled: true
        efm_ldap_url: "ldaps://your-ldap-server.example.com:636"
        # Database Configuration (if not using defaults)
        efm_db_url: "jdbc:postgresql://db-server:5432/efm_prod"
        efm_db_username: "efm_user"
        efm_db_password: "SecureDbPassword"
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
