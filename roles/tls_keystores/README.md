# tls_keystores

Creates Java keystores (JKS) and truststores from TLS certificates and private keys. It is designed to work with certificates issued by FreeIPA.

## Features
- Creates JKS keystores from certificate and private key files
- Creates JKS truststores with CA certificates
- Configurable keystore and truststore paths and aliases

## Requirements
- Java keytool (part of Java installation)
- community.general Ansible collection
- Certificate and private key files must exist on target host

## Role Variables

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `keystore_password` | `str` | Yes | `undef` | Password for both keystore and truststore |
| `keystore_alias` | `str` | Yes | `undef` | Alias name for the certificate in the keystore |
| `keystore_output_path` | `str` | No | `/etc/pki/tls/private/keystore.jks` | Path to output JKS keystore file |
| `keystore_cert_path` | `str` | No | `/etc/pki/tls/certs/host.crt` | Path to the certificate file |
| `keystore_key_path` | `str` | No | `/etc/pki/tls/private/host.key` | Path to the private key file |
| `truststore_alias` | `str` | No | `ipa-ca` | Alias name for the CA certificate in the truststore |
| `truststore_path` | `str` | No | `/etc/pki/tls/private/truststore.jks` | Path to output JKS truststore file |
| `ca_cert_path` | `str` | No | `/etc/ipa/ca.crt` | Path to the CA certificate file |

## Example Playbook

```yaml
- hosts: java_servers
  tasks:
    - name: Create Java keystores and truststores with default paths
      ansible.builtin.import_role:
        name: tls_keystores
      vars:
        keystore_password: "MySecurePassword123"
        keystore_alias: "service-cert"
        keystore_cert_path: "/etc/pki/tls/certs/host.crt"
        keystore_key_path: "/etc/pki/tls/private/host.key"
        truststore_alias: "ipa-ca"
        ca_cert_path: "/etc/ipa/ca.crt"

    - name: Create Java keystores for EFM Gateway with custom paths
      ansible.builtin.import_role:
        name: tls_keystores
      vars:
        keystore_password: "MySecurePassword123"
        keystore_alias: "efm-gateway"
        keystore_output_path: "/opt/cloudera/cem/certs/keystore.jks"
        truststore_path: "/opt/cloudera/cem/certs/truststore.jks"
        keystore_cert_path: "/etc/pki/tls/certs/gateway.crt"
        keystore_key_path: "/etc/pki/tls/private/gateway.key"
        truststore_alias: "freeipa-ca"
        ca_cert_path: "/etc/ipa/ca.crt"
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
