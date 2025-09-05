# prereq_kerberos

Set up for Kerberos

This role prepares a host for Kerberos usage by installing the necessary OS-specific client libraries. It configures the Kerberos credential cache to use KCM (Kerberos Credential Manager) and can optionally set up and configure the SSSD (System Security Services Daemon) for user authentication and authorization.

The role will:
- Install a list of specified Kerberos client packages. If not provided, it will determine and install the appropriate packages based on the target host's operating system.
- Configure the Kerberos client by managing the `krb5.conf` file, including setting the `kerberos_realm`.
- Configure the Kerberos Credential Manager (KCM) to be the default credential cache.
- If SSSD is used, the role will configure the `sssd.conf` file and manage the `sssd` service.
- Set the Kerberos encryption types.

# Requirements

- Root or `sudo` privileges are required on the target host to manage packages and system configuration files.
- Network access to package repositories.
- A functional Kerberos Key Distribution Center (KDC) is assumed to be available on the network to service the specified `kerberos_realm`.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `kerberos_packages` | `list` of `str` | `False` | `[defaults based on OS]` | List of Kerberos client packages to install. If not defined, the role will install default packages based on the OS distribution. |
| `kerberos_config_path` | `path` | `False` | `/etc/krb5.conf` | Path to the main Kerberos configuration file. |
| `kerberos_encryption_types` | `dict` | `False` | `{"default_tgs_enctypes": ["aes256-cts", "aes128-cts"], "default_tkt_enctypes": ["aes256-cts", "aes128-cts"], "permitted_enctypes": ["aes256-cts", "aes128-cts"]}` | Dictionary of Kerberos encryption types to configure. |
| `kerberos_kcm_credential_cache_config_path` | `path` | `False` | `/etc/krb5.conf.d/kcm_default_ccache` | Path to the configuration file that sets the default credential cache type to KCM. |
| `kerberos_realm` | `str` | `True` | | The name of the Kerberos realm to which the host will belong. This is a mandatory parameter. |
| `sssd_config_path` | `path` | `False` | `/etc/sssd/sssd.conf` | Path to the SSSD configuration file. The role will only manage this file if SSSD is part of the overall setup. |
| `sssd_service` | `str` | `False` | `sssd` | The name of the SSSD service to manage. |

# Example Playbook

```yaml
- hosts: all
  tasks:
    - name: Set up Kerberos client for the example.internal realm
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_kerberos
      vars:
        kerberos_realm: "EXAMPLE.INTERNAL"
        # All other options will use their defaults, including packages and SSSD settings.

    - name: Set up Kerberos with custom paths and SSSD configuration
      ansible.builtin.import_role:
        name: cloudera.exe.prereq_kerberos
      vars:
        kerberos_realm: "MY.CUSTOM.REALM"
        kerberos_packages:
          - krb5-workstation # Example custom package
        kerberos_config_path: "/etc/kerberos/krb5.conf"
        sssd_config_path: "/etc/sssd/my_sssd.conf"
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
