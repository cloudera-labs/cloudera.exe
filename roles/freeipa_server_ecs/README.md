# freeipa_server_ecs

Configure DNS zones and wildcard records for Cloudera ECS.

This role configures DNS zones and wildcard records within a **FreeIPA** server, which is a key step for Cloudera on Premise **Embedded Container Service (ECS)**. It simplifies the process of setting up name resolution for applications and services within a specific domain by automatically creating a DNS zone and populating it with wildcard DNS records pointing to a single IP address.

The role will:
- Authenticate to a FreeIPA server using the provided administrative credentials.
- Create a new DNS zone based on the `ipaserver_domain` and the `zone_name` defined in the `freeipa_dns_records` list.
- Add wildcard DNS records (`*` records) to the specified zone.
- Point these wildcard records to the target IP address defined in `freeipa_dns_records_address`.
- Optionally, skip a check for overlapping DNS zones if `dnszone_skip_overlap_check` is set to `true`.
- Execute all commands via the FreeIPA API, either on a client or server context.

## Requirements

- A running and accessible **FreeIPA server**.
- The `ipaadmin_principal` must have permissions to create DNS zones and records within the FreeIPA environment.
- Network connectivity from the Ansible controller (or the `ipaapi_context` host) to the FreeIPA server.

## Dependencies

None.

## Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `ipaadmin_password` | `str` | `True` | | **FreeIPA** administrative password for authentication. |
| `ipaadmin_principal` | `str` | `False` | `admin` | **FreeIPA** administrative principal (user) for authentication. |
| `ipaserver_host` | `str` | `False` | `inventory_hostname` | Hostname or IP address of the **FreeIPA** server to connect to. Defaults to the current host. |
| `ipaserver_domain` | `str` | `True` | | The **FreeIPA** domain under which the DNS zone will be created (e.g., `example.internal`). |
| `freeipa_dns_records` | `list` of `dict` | `False` | `[{'zone_name': 'apps.{{ ipaserver_domain }}', 'record_name': '*', 'record_type': 'A'}, {'zone_name': '{{ ipaserver_domain }}', 'record_name': '*', 'record_type': 'A'}]` | A list of DNS records to create within the specified **FreeIPA** domain. Each dictionary defines a record with its `zone_name`, `record_name`, and `record_type`. Defaults to creating two wildcard A records. |
| `freeipa_dns_records_address` | `str` | `True` | | The target IP address for the DNS records defined in `freeipa_dns_records`. All records will point to this address. |
| `dnszone_skip_overlap_check` | `bool` | `False` | `false` | A flag to skip the overlap check when creating DNS zones, which can be useful in specific configurations but should be used with caution. |
| `ipaapi_context` | `str` | `False` | - | The **FreeIPA** role of the host where the DNS Zone creation command will be executed. Choices are `client` or `server`. |

## Example Playbook

```yaml
- hosts: ipaserver_host
  tasks:
    - name: Configure FreeIPA DNS for ECS with default wildcard records
      ansible.builtin.import_role:
        name: cloudera.exe.freeipa_server_ecs
      vars:
        ipaadmin_password: "MySuperSecretAdminPassword" # Use Ansible Vault for this
        ipaserver_domain: "example.internal"
        freeipa_dns_records_address: "10.0.0.100"
        # The role will automatically create '*' records for 'apps.example.internal' and 'example.internal'

    - name: Configure a single custom DNS record for ECS
      ansible.builtin.import_role:
        name: cloudera.exe.freeipa_server_ecs
      vars:
        ipaadmin_password: "MySuperSecretAdminPassword"
        ipaserver_domain: "example.internal"
        freeipa_dns_records_address: "10.0.0.200"
        freeipa_dns_records:
          - zone_name: "custom.{{ ipaserver_domain }}"
            record_name: "customapp"
            record_type: "A"
        dnszone_skip_overlap_check: true
        ipaapi_context: "client"
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
