# caddy

Install Caddy proxy packages.

This role installs the Caddy web server and reverse proxy, configuring it for self-signed TLS by default, or optionally with external CA certificates, or via Let's Encrypt. It sets up an initial global configuration with an import directory, configures a WWW root directory, and can retrieve Caddy's generated self-signed CA certificate to the target host if applicable.

The role will:
- Install the Caddy proxy service.
- Configure an initial global configuration for Caddy, including an import directory for modular configuration.
- Set up a designated WWW root directory for serving static content.
- Manage TLS certificates based on the `caddy_self_signed`, `caddy_ca_pem`, and `caddy_ca_key` parameters:
    - If `caddy_self_signed` is `true` (default) and `caddy_ca_pem` is not defined, Caddy will generate its own self-signed root CA and issue certificates. The Caddy self-signed CA certificate will be retrieved to the target host.
    - If `caddy_self_signed` is `false`, Caddy will attempt to use Let's Encrypt's ACME service to obtain trusted certificates.
    - If `caddy_ca_pem` and `caddy_ca_key` are provided, Caddy will use these external CA credentials for TLS.
- Ensure the Caddy service is running and enabled.

# Requirements

- A DNS A record resolving `caddy_domain` to the target host's IP address is recommended for proper certificate validation.
- Ports 80 and 443 must be open on the target host and accessible for inbound connections.
- For Let's Encrypt (when `caddy_self_signed` is `false`), ports 80/443 must be publicly accessible and the domain must be resolvable via public DNS.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `caddy_domain` | `str` | `True` | | Domain name for the Caddy reverse proxy (e.g., `proxy.example.com`). |
| `caddy_www_root` | `path` | `False` | `/var/www_root` | Directory where static WWW service content will be served from. |
| `caddy_self_signed` | `bool` | `False` | `true` | Flag enabling Caddy to issue self-signed TLS certificates. If `false`, Caddy defaults to using the Let's Encrypt ACME service. If `true` and `caddy_ca_pem` is not defined, Caddy generates its own root CA. |
| `caddy_ca_pem` | `path` | `False` | | Path to an external CA certificate file (PEM format) to be used by Caddy for TLS. |
| `caddy_ca_key` | `path` | `False` | | Path to the private key for the external CA (`caddy_ca_pem`). This parameter is required if `caddy_ca_pem` is defined. |

# Example Playbook

```yaml
- hosts: proxy_servers
  tasks:
    - name: Install Caddy with default self-signed TLS
      ansible.builtin.import_role:
        name: cloudera.exe.caddy
      vars:
        caddy_domain: "dev-proxy.example.com"
        # caddy_self_signed will default to true
        # caddy_www_root will default to /var/www_root

    - name: Install Caddy using Let's Encrypt
      ansible.builtin.import_role:
        name: cloudera.exe.caddy
      vars:
        caddy_domain: "prod-proxy.example.com"
        caddy_self_signed: false # Enable Let's Encrypt ACME

    - name: Install Caddy with external CA certificates
      ansible.builtin.import_role:
        name: cloudera.exe.caddy
      vars:
        caddy_domain: "internal-proxy.example.com"
        caddy_self_signed: true # Still technically self-signed, but by an external CA
        caddy_ca_pem: "/path/to/my_org_ca.pem"
        caddy_ca_key: "/path/to/my_org_ca.key"
        caddy_www_root: "/srv/my_app_html"
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
