# Provision

A role that provisions Cloudera-specific inventory.

The role requires the following two files that are locatable by the enclosing play:

* *hostvars.j2* - a Jinja macro that outputs a host's variables in a static inventory file
* *instance_vars.j2* - a Jinja macro that outputs an instance's metadata, i.e. tags, in the provider

These two Jinja macros _expect variables on the host_ which are assigned via the `add_host` call
within the role. To set these variables, use the `module_defaults` assignment within the enclosing
play of the role.

## Examples

### module_defaults

The `node` variable is in scope of the `add_host` module and contains the output of the Terraform
node provisioning configuration.

```yaml
- name: Provision resources
  hosts: localhost
  connection: local
  gather_facts: no
  module_defaults:
    ansible.builtin.add_host:
      groups: "{{ node.groups | default(omit) }}"
      host_template: "{{ node.metadata.host_template | default(omit) }}"
      storage_volumes: "{{ node.storage_volumes | default([]) }}"
      tls: "{{ node.metadata.tls | default(omit) }}"
  tasks: ...
```

### hostvars.j2

```jinja
{# Collect and output individual host variables #}
{% macro host_variables(host) %}
{% set fields = [] %}
{% set _ = fields.append("ansible_user=" + host['ansible_user']) if 'ansible_user' in host %}
{% set _ = fields.append("host_template=" + host['host_template']) if 'host_template' in host %}
{% set _ = fields.append("label=" + host['label']) if 'label' in host %}
{% set _ = fields.append("tls=" + host['tls'] | string) if 'tls' in host %}
{{ host['inventory_hostname'] }} {{ fields | join(' ') }}
{%- endmacro %}
```

### instance_vars.j2

```jinja
{# Define the metadata tags for the individual Openstack instances #}
{# Output should be TF map _entries_, not a map itself #}

{% macro instance_tags(host) %}
{% set tags = {} %}
{% set _ = tags.update({ 'ansible_user': host.ansible_user }) if host.ansible_user is defined %}
{% set _ = tags.update({ 'host_template': host.host_template }) if host.host_template is defined %}
{% set _ = tags.update({ 'groups': host.groups | join(', ') }) if host.groups is defined %}
{% set _ = tags.update({ 'tls': host.tls | string }) if host.tls is defined %}
{% for k, v in tags.items() %}
            {{ k }} = "{{ v }}"{{ "," if not loop.last else "" }}
{% endfor %}
{%- endmacro %}
```
