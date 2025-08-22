# freeipa_client

Set up FreeIPA client, registering the host with a FreeIPA server, configured for DNS updates.

The role will:
- Update `cloud-init` configuration to disable hostname management, if needed
- Update the hostname to the Ansible `inventory_hostname`
- Update `/etc/hosts` with the Ansible `inventory_hostname` and default IPv4 address
- Create and activate a `cldr` connection ethernet profile in `NetworkManager` for the Ansible default IPv4 alias to set domain search and name servers, if needed
- Update the DHCP client configuration to set domain search and name servers, if needed
- Update `/etc/resolv.conf` directly to set domain search and name servers, if needed
- Set the SSSD configuration to enumerate users and groups, if needed.
- Install defined FreeIPA client packages, if needed
- Set up and register FreeIPA client with the FreeIPA servers.

## Requirements

None.

## Dependencies

- `freeipa.ansible_freeipa.ipaclient`

## Examples

```yaml
- name: Install FreeIPA client
  ansible.builtin.import_role:
    name: freeipa_client
  vars:
    ipaclient_domain: example.internal
    ipaclient_realm: EXAMPLE.INTERNAL
    ipaclient_servers: [ "freeipa.example.internal" ]
    ipaclient_dns_servers: [ "10.0.0.4" ]
    ipaadmin_password: "SomEpassWord"
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
