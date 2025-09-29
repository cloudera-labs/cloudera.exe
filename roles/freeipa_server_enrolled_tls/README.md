# freeipa_server_enrolled_tls

Issue a TLS certificate for an enrolled host

This role issues a **TLS certificate** for a host that is enrolled in FreeIPA. This is useful for hosts that are already members of the FreeIPA domain and need TLS certificates for their services. The process includes generating a private key and Certificate Signing Request (CSR), and then requesting a certificate from FreeIPA's Certificate Authority (CA) using the host's enrolled identity.

The role will:

  * Authenticate to the FreeIPA server using the provided administrative credentials.
  * Generate a private key and CSR directly on the target host.
  * Request a TLS certificate from FreeIPA's CA for the enrolled host.
  * The certificate and key will be saved directly to their final locations.
  * Optionally, it can use a specific certificate profile if `enrolled_cert_profile` is provided.

## Requirements

  * The target host must be already enrolled in the FreeIPA domain.
  * The `ipaadmin_principal` must have permissions to issue certificates in FreeIPA.
  * Write access to the specified certificate and key paths on the target host.

## Dependencies

None.

## Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `ipaadmin_password` | `str` | `True` | | **FreeIPA** admin password for authentication. This should be stored securely, for example, using Ansible Vault. |
| `ipaadmin_principal` | `str` | `False` | `admin` | **FreeIPA** admin principal for authentication. |
| `enrolled_hostname` | `str` | `True` | | The hostname for which the certificate will be issued. Must be an enrolled FreeIPA client. |
| `enrolled_cert_profile` | `str` | `False` | | The name of the certificate profile to use for issuing the certificate (e.g., `wildcard`). |
| `enrolled_cert_key_path` | `path` | `False` | `/etc/pki/tls/private/service.key` | The path on the target host to save the generated private key file. |
| `enrolled_cert_csr_path` | `path` | `False` | `/etc/pki/tls/private/service.csr` | The path on the target host to save the generated CSR file. |
| `enrolled_cert_path` | `path` | `False` | `/etc/pki/tls/certs/service.crt` | The path on the target host to save the issued TLS certificate. |

## Example Playbook

```yaml
- hosts: enrolled_clients
  vars:
    ipaadmin_password: "MySuperSecretAdminPassword" # Use Ansible Vault
    enrolled_hostname: "{{ ansible_fqdn }}"
  roles:
    - freeipa_server_enrolled_tls

- hosts: enrolled_clients
  tasks:
    - name: Issue a TLS certificate for enrolled host
      ansible.builtin.import_role:
        name: freeipa_server_enrolled_tls
      vars:
        ipaadmin_password: "MySuperSecretAdminPassword"
        enrolled_hostname: "gateway.example.internal"
        enrolled_cert_key_path: "/etc/pki/tls/private/gateway.key"
        enrolled_cert_path: "/etc/pki/tls/certs/gateway.crt"

    - name: Issue a TLS certificate using a custom certificate profile
      ansible.builtin.import_role:
        name: freeipa_server_enrolled_tls
      vars:
        ipaadmin_password: "MySuperSecretAdminPassword"
        enrolled_hostname: "app.example.internal"
        enrolled_cert_profile: "wildcard"
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
