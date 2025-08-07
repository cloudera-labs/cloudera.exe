# freeipa_server

Install FreeIPA server with support for DNS, Kerberos, TLS, and LDAP.

The role is typically used to support an internal domain, e.g. `.internal`.

The role will:
- Enable local IPv6 networking, per FreeIPA installation requirements.
- Install FreeIPA server packages.
- Install and configure FreeIPA server for DNS, Kerberos, TLS, and LDAP.
- Set up an ACL for DNS recursion.
- Establish DNS zones for the defined domain.

## Requirements

None.

## Dependencies

- `freeipa.ansible`

## Examples

```yaml
- name: Install FreeIPA server for DNS, Kerberos, TLS, and LDAP.
  ansible.builtin.import_role:
    name: cloudera.exe.freeipa_server
  vars:
    ipaserver_forwarders: [ "1.1.1.1" ]
    ipaserver_cidr: [ "10.0.0.1/20" ]
    ipaserver_recursion_acl_cidr: [ "10.0.0.1/20" ]
    ipaserver_domain: "example.internal"
    ipaserver_realm: "EXAMPLE.INTERNAL"
    ipaadmin_password: "krb_example"
    ipadm_password: "dir_example"
```

To bind to explicit IP addresses, provide optional (push-down) parameters:

```yaml
ipaserver_ip_addresses: [ "10.0.0.14"]  # Bind DNS to these IP addresses only
ipaclient_ip_address: "10.0.1.122"      # Join with this IP address
```

## License

```
Copyright 2024 Cloudera, Inc.

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
