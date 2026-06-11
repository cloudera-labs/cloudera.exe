# keycloak_container

Deploys Keycloak as a Docker container managed by systemd on a Linux host. Creates the necessary user/group structure, and sets up a systemd service for automated startup and management.

## Requirements

- **Docker**: The `docker` service must be installed and running on the target host. Consider using the `docker_install` role as a prerequisite.
- **Systemd**: The target host must use `systemd` for service management.
- Root or sudo access on the target system.

## Parameters

| Variable | Default | Description |
|----------|---------|-------------|
| `keycloak__container_name` | `keycloak-server` | Name of the Docker container |
| `keycloak__container_image` | `quay.io/keycloak/keycloak` | Docker image repository |
| `keycloak__container_tag` | `26.0.7` | Keycloak version tag |
| `keycloak__admin_username` | `admin` | Keycloak admin username |
| `keycloak__admin_password` | **Required** | Keycloak admin password (must be set) |
| `keycloak__container_http_port` | `8180` | HTTP port mapping |
| `keycloak__container_https_port` | `8543` | HTTPS port mapping |
| `keycloak__system_username` | `keycloak` | System user for Keycloak service |
| `keycloak__system_groupname` | `keycloak` | System group for Keycloak service |
| `keycloak__docker_exe` | `/usr/bin/docker` | Path to Docker executable |
| `keycloak__metrics_enabled` | `true` | Enable Keycloak metrics endpoint |
| `keycloak__health_enabled` | `true` | Enable Keycloak health check endpoint |
| `keycloak__container_log_level` | `INFO` | Logging level (DEBUG, INFO, WARN, ERROR) |
| `keycloak__proxy_headers` | `xforwarded` | Proxy headers mode (`xforwarded`, `forwarded`) |
| `keycloak__http_enabled` | `true` | Enable HTTP |
| `keycloak__https_enabled` | `false` | Enable HTTPS |
| `keycloak__tls_key_path` | _(optional)_ | Path on the host to the TLS private key file (required when `keycloak__https_enabled` is `true`) |
| `keycloak__tls_cert_path` | _(optional)_ | Path on the host to the TLS certificate file (required when `keycloak__https_enabled` is `true`) |

## Example Playbook

```yaml
- hosts: keycloak_servers
  become: true
  roles:
    - role: keycloak_container
      vars:
        keycloak__admin_password: "ChangeMe123!"
        keycloak__https_enabled: true
        keycloak__tls_cert_path: /etc/ssl/certs/keycloak.crt
        keycloak__tls_key_path: /etc/ssl/private/keycloak.key
```
