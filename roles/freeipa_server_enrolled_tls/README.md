# freeipa_server_enrolled_tls

Issue a TLS certificate and private key for an enrolled host

This role issues a **TLS certificate and private key** for a host that is enrolled in FreeIPA. This is useful for hosts that are already members of the FreeIPA domain and need TLS certificates for their services. The process includes generating a private key and Certificate Signing Request (CSR), and then requesting a certificate from FreeIPA's Certificate Authority (CA) using the host's enrolled identity.

The role will:

  * Authenticate to the FreeIPA server using the provided administrative credentials.
  * Generate a private key and CSR directly on the target host.
  * Request a TLS certificate from FreeIPA's CA for the enrolled host.
  * The certificate and key will be saved directly to their final locations.


## Requirements

  * The target host must be already enrolled in the FreeIPA domain.
  * The `ipaadmin_principal` must have permissions to issue certificates in FreeIPA.
  * Write access to the specified certificate and key paths on the FreeIPA server.

## Dependencies

None.

## Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `ipaadmin_password` | `str` | `True` | | **FreeIPA** admin password for authentication. |
| `ipaadmin_principal` | `str` | `False` | `admin` | **FreeIPA** admin principal for authentication. |
| `enrolled_hostname` | `str` | `True` | | The hostname for which the certificate will be issued. Must be an enrolled FreeIPA client. |
| `enrolled_principal_type` | `str` | `False` | `host` | The type of principal for certificate request (e.g., host, service). |
| `enrolled_cert_key_path` | `path` | `False` | `/etc/pki/tls/private/host.key` | The path on the target host to save the generated private key file. |
| `enrolled_cert_csr_path` | `path` | `False` | `/etc/pki/tls/private/host.csr` | The path on the target host to save the generated CSR file. |
| `enrolled_cert_path` | `path` | `False` | `/etc/pki/tls/certs/host.crt` | The path on the target host to save the issued TLS certificate. |
| `enrolled_cert_owner` | `str` | `False` |  | Owner (user) for the generated certificate and private key files. |
| `enrolled_cert_group` | `str` | `False` |  | Group for the generated certificate and private key files. |

## Example Playbook

```yaml
- hosts: enrolled_hosts
  tasks:
    - name: Issue a TLS certificate and private key for enrolled host
      ansible.builtin.import_role:
        name: cloudera.exe.freeipa_server_enrolled_tls
      vars:
        enrolled_hostname: "hostname.example.internal"
        ipaadmin_password: "password"
        enrolled_cert_key_path: "/etc/pki/tls/private/gateway.key"
        enrolled_cert_path: "/etc/pki/tls/certs/gateway.crt"

- hosts: enrolled_hosts
  tasks:
    - name: Issue a TLS certificate and private key for PostgreSQL service
      ansible.builtin.import_role:
        name: freeipa_server_enrolled_tls
      vars:
        enrolled_hostname: "postgres.example.internal"
        ipaladmin_password: "password"
        enrolled_cert_key_path: "/etc/pki/tls/private/postgres.key"
        enrolled_cert_path: "/etc/pki/tls/certs/postgres.crt"
        enrolled_cert_owner: "postgres"
        enrolled_cert_group: "postgres"
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
