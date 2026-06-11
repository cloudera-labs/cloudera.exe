# keycloak_container

Deploys Keycloak as a Docker container managed by systemd on a Linux host. Creates the necessary user/group structure, and sets up a systemd service for automated startup and management.

## Requirements

- **Docker**: The `docker` service must be installed and running on the target host. Consider using the `docker_install` role as a prerequisite.
- **Systemd**: The target host must use `systemd` for service management.
- Root or sudo access on the target system.

## Parameters

| Variable | Default | Description |
|----------|---------|-------------|
| `keycloak_container_name` | `keycloak-server` | Name of the Docker container |
| `keycloak_container_image` | `quay.io/keycloak/keycloak` | Docker image repository |
| `keycloak_container_tag` | `26.0.7` | Keycloak version tag |
| `keycloak_admin_username` | `admin` | Keycloak admin username |
| `keycloak_admin_password` | **Required** | Keycloak admin password (must be set) |
| `keycloak_container_http_port` | `8180` | HTTP port mapping |
| `keycloak_container_https_port` | `8543` | HTTPS port mapping |
| `keycloak_system_username` | `keycloak` | System user for Keycloak service |
| `keycloak_system_groupname` | `keycloak` | System group for Keycloak service |
| `keycloak_docker_exe` | `/usr/bin/docker` | Path to Docker executable |
| `keycloak_metrics_enabled` | `true` | Enable Keycloak metrics endpoint |
| `keycloak_health_enabled` | `true` | Enable Keycloak health check endpoint |
| `keycloak_container_log_level` | `INFO` | Logging level (DEBUG, INFO, WARN, ERROR) |
| `keycloak_proxy_headers` | `xforwarded` | Proxy headers mode (`xforwarded`, `forwarded`) |
| `keycloak_http_enabled` | `true` | Enable HTTP |
| `keycloak_https_enabled` | `false` | Enable HTTPS |
| `keycloak_tls_key_path` | _(optional)_ | Path on the host to the TLS private key file (required when `keycloak_https_enabled` is `true`) |
| `keycloak_tls_cert_path` | _(optional)_ | Path on the host to the TLS certificate file (required when `keycloak_https_enabled` is `true`) |

## Example Playbook

```yaml
- hosts: keycloak_servers
  become: true
  roles:
    - role: keycloak_container
      vars:
        keycloak_admin_password: "ChangeMe123!"
        keycloak_https_enabled: true
        keycloak_tls_cert_path: /etc/ssl/certs/keycloak.crt
        keycloak_tls_key_path: /etc/ssl/private/keycloak.key
```
