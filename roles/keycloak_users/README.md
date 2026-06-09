# keycloak_users

This Ansible role manages Keycloak users, groups, and role mappings using the Keycloak REST API. It creates users with their associated groups and optionally assigns realm roles and client roles.

## Requirements

- An accessible Keycloak instance
- The `community.general` collection (version 5.7.0+) for Keycloak modules
- Valid admin credentials for the Keycloak instance

## Parameters

### Authentication Configuration

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `keycloak__auth_keycloak_url` | **Yes** | - | URL to the Keycloak instance (e.g., `https://keycloak.example.com`) |
| `keycloak__auth_username` | No | `admin` | Username to authenticate for API access |
| `keycloak__auth_password` | **Yes** | - | Password to authenticate for API access |
| `keycloak__auth_client_id` | No | `admin-cli` | OpenID Connect client_id to authenticate with |
| `keycloak__auth_client_secret` | No | `""` | Client Secret (if required) |
| `keycloak__auth_realm` | No | `master` | Keycloak realm name to authenticate to for API access |
| `keycloak__auth_validate_certs` | No | `true` | Whether to validate SSL certificates when connecting to Keycloak |

### User Account Configuration

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `keycloak__useraccounts` | No | `[]` | List of user account definitions (see structure below) |

#### User Account Structure

Each user account in `keycloak__useraccounts` has the following structure:

```yaml
keycloak__useraccounts:
  - username: user1              # Required: Username
    firstName: User1             # Required: User's first name
    lastName: One                # Required: User's last name
    email: user1@example.com     # Required: User's email address
    password: password           # Required: User's password
    realm_name: master           # Required: Realm to create user in
    groups:                      # Optional: List of groups to add user to
      - group1
      - group2
    realm_roles:                 # Optional: List of realm roles to assign
      - admin
      - user
    client_roles:                # Optional: List of client role mappings
      - client_id: my-client     # Client name
        roles:                   # Roles within that client
          - client-admin
          - client-user
```

## Example Playbook

Basic usage:

```yaml
- hosts: localhost
  roles:
    - role: keycloak_users
      vars:
        keycloak__auth_keycloak_url: "https://keycloak.example.com"
        keycloak__auth_password: "AdminPassword123"
        keycloak__auth_validate_certs: false
        keycloak__useraccounts:
          - username: user1
            firstName: User1
            lastName: One
            email: user1@example.com
            password: password123
            realm_name: master
            groups:
              - developers
              - users
```

Admin User with Role Mappings

```yaml
- hosts: localhost
  roles:
    - role: keycloak_users
      vars:
        keycloak__auth_keycloak_url: "https://keycloak.example.com:8543"
        keycloak__auth_username: admin
        keycloak__auth_password: "SecurePassword"
        keycloak__auth_validate_certs: false
        keycloak__useraccounts:
          - username: admin-user
            firstName: Admin
            lastName: User
            email: admin@example.com
            password: adminpass123
            realm_name: master
            groups:
              - admins
            realm_roles:
              - admin
              - create-realm
          - username: app-user
            firstName: Application
            lastName: User
            email: app@example.com
            password: apppass123
            realm_name: my-realm
            groups:
              - app-users
            client_roles:
              - client_id: my-application
                roles:
                  - app-admin
                  - view-metrics
```

## License

```
Copyright 2026 Cloudera, Inc.

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