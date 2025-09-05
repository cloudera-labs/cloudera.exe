# freeipa_server_unenrolled_tls

Issue a TLS certificate for an unenrolled host

This role issues a **TLS certificate** for a host that is not enrolled in FreeIPA. This is useful for hosts in a deployment that need a trusted certificate but don't require full FreeIPA client services such as DNS. The process includes creating a host entry in FreeIPA, generating a private key and Certificate Signing Request (CSR), and then requesting a certificate from FreeIPA's Certificate Authority (CA).

The role will:

  * Authenticate to the FreeIPA server using the provided administrative credentials.
  * Create a host entry in FreeIPA for the `unenrolled_hostname`.
  * Generate a private key and a CSR on the FreeIPA server, storing them at the specified paths.
  * Request a TLS certificate from FreeIPA's CA, which is signed and issued to the unenrolled host.
  * The certificate will be saved to the path specified by `unenrolled_cert_path`.
  * Optionally, it can use a specific certificate profile if `unenrolled_cert_profile` is provided.
  * Retrieve the issued TLS certificate and private key to the controller.

## Requirements

  * The `ipaadmin_principal` must have permissions to create host entries and issue certificates in FreeIPA.
  * The role expects to be run directly on the **FreeIPA server**.
  * Write access to the specified certificate and key paths on the FreeIPA server.

## Dependencies

None.

## Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `ipaadmin_password` | `str` | `True` | | **FreeIPA** admin password for authentication. This should be stored securely, for example, using Ansible Vault. |
| `ipaadmin_principal` | `str` | `False` | `admin` | **FreeIPA** admin principal for authentication. |
| `unenrolled_hostname` | `str` | `True` | | The hostname for which the certificate will be issued. A DNS record for this host will **not** be created. |
| `unenrolled_description` | `str` | `False` | | A descriptive string for the unenrolled host entry in FreeIPA. |
| `unenrolled_cert_profile` | `str` | `False` | | The name of the certificate profile to use for issuing the certificate (e.g., `wildcard`). |
| `unenrolled_cert_key_path` | `path` | `False` | `/etc/pki/tls/private/<unenrolled_hostname>.pem` | The path on the FreeIPA server to save the generated private key file. |
| `unenrolled_cert_csr_path` | `path` | `False` | `/etc/pki/tls/private/<unenrolled_hostname>.csr` | The path on the FreeIPA server to save the generated CSR file. |
| `unenrolled_cert_path` | `path` | `False` | `/etc/pki/tls/certs/<unenrolled_hostname>.crt` | The path on the FreeIPA server to save the issued TLS certificate. |

## Example Playbook

```yaml
- hosts: ipaserver_host
  tasks:
    - name: Issue a TLS certificate for a new host entry
      ansible.builtin.import_role:
        name: cloudera.exe.freeipa_server_unenrolled_tls
      vars:
        ipaadmin_password: "MySuperSecretAdminPassword" # Use Ansible Vault
        unenrolled_hostname: "client1.example.internal"
        unenrolled_description: "Client host for monitoring"

    - name: Issue a TLS certificate using a custom certificate profile
      ansible.builtin.import_role:
        name: cloudera.exe.freeipa_server_unenrolled_tls
      vars:
        ipaadmin_password: "MySuperSecretAdminPassword"
        unenrolled_hostname: "app.example.internal"
        unenrolled_cert_profile: "wildcard" # Assumes a 'wildcard' profile exists
        unenrolled_cert_path: "/opt/pki/certs/app.crt"
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
