# Role Design and Structure

The whole of `cloudera.exe` centers on three subjects: _runlevels_, _tags_, and _shared dependencies_.

Specifically, the `cloudera.exe` collection defines three core roles -- `cloudera.exe.infrastructure`, `cloudera.exe.platform`, and `cloudera.exe.runtime` -- that encapsulate the standard operating processes for installing, managing, and uninstalling a CDP deployment. These roles satisfy the first five runlevels illustrated in the [Runlevels Guide](runlevels.md) by implementing a defined set of [task lists](#task_lists). This design is extensible, and developers seeking additional runlevel capabilities should expect to [add new roles and retag existing roles](#additional-runlevels).

The runlevel-like processes are coordinated by the `cloudera.exe.sequence` role, which uses a cascading set of [Ansible tags](#tags) to call these functions. This "orchestration" role is itself referenced by playbooks using the `ansible.builtin.import_role`.

All of four of these roles [share common variables](#variables) through a simple role dependency to `cloudera.exe.common`.

Other roles use the shared dependencies and tagging approach, yet are not directly referenced by these core roles. For example, the `cloudera.exe.data` role is typically used within an _application_ level playbook, yet does drawn on the same configuration variables provided by `cloudera.exe.common`.

# Task Lists

Each of the three core roles (`infrastructure`, `platform`, and `runtime`) consist of four entrypoint task lists:

+ `validate.yml`
+ `initialize.yml`
+ `setup.yml`
+ `teardown.yml`

These tasks lists are referenced by the `ansible.builtin.include_role` module's `tasks_from` by "orchestation" roles like `cloudera.exe.sequence`. The _execution_ of each task list for each role is governed by a [cascading set of Ansible tags](runlevels.md). Which tag and when they are applied to trigger a given task list is defined _only_ by "orchestration" roles, e.g. `cloudera.exe.sequence`.

# Variables

The variables used by any `cloudera.exe` role are defined _completely_ within the role's `defaults` and prefixed to isolate variables to that role alone. Roles also reference a [canonical set of variables](configuration.md) to normalize usage. (See [Configuration Mapping](#configuration-mapping) for customization options).

Variables that are shared among roles should be defined within the `cloudera.exe.common` role, which is a dependency for each of the core roles, and then mapped into a prefixed role default.

For example:

```yaml
---
# cloudera.exe/roles/common/defaults/main.yml
common__infra_type:     "{{ globals.infra_type | default('aws') }}"

---
# cloudera.exe/roles/infrastructure/defaults/main.yml
# NOTE: common__infra_type is inherited by role dependency
plat__infra_type:       "{{ common__infra_type }}"
```

This mapping isolates changes to shared variables to a single location (`cloudera.exe.common`) and facilitates debugging and overrides.

# Tags

The core roles - `infrastructure`, `platform`, and `runtime` -- are designed to be invoked by [Ansible tags](https://docs.ansible.com/ansible/latest/user_guide/playbooks_tags.html).

Roles like `cloudera.exe.sequence` have a tagging structure which "cascades" execution to provide runlevel prerequisites. For example, the `plat` tag (representing the [Platform](runlevels.md#platform) runlevel) invokes the _teardown_ sequence for [Runtime](runlevels.md#runtime) and then the _setup_ sequence for [Infrastructure](runlevels.md#infrastructure) and then Platform itself, reconciling the state of each setup if needed.

The _validate_ sequence for the [Validation](runlevels.md#validation) runlevel is always invoked, as is the _initialization_ sequence -- the [Initialization](runlevels.md#initialization) for each affected high-level runlevel.

The tagging structure also includes the `teardown` tag to enable the [Teardown](runlevels.md#teardown) runlevel to destroy a deployment in its entirety.

# Customization and Extension

The collection is designed to run _as-is_ yet also allow for customization and extension to fit the majority of deployment needs.

## Configuration Mapping

The three core roles and the supporting `common` role all expect a [normalized, nested data structure](configuration.md) for configuration. Developers can have an `ansible.builtin.include_vars` task or some other variable interpolation function that maps an incoming configuration data structure to this normalized structure for easy customized configuration options. One good example of this technique is the [Cloudera Deploy](https://github.com/cloudera-labs/cloudera-deploy) project, which takes a user `profile` and a deployment `definition` and merges these two configurations to the normalized structure.

```yaml
---
# my_project/vars/runlevel-mapping.yml
# Map a series of INI-style, flat-structured variables to the canonical, nested configuration
globals:
  infra_type:       "{{ ini_cloud | mandatory }}"
  admin_password:   "{{ ini_admin_password | default('MyDogHasFleas') }}"
  ssh:
    public_key_id:  "{{ ini_public_key | default('some_public_key_id') }}"

---
# my_project/developer_playbook.yml
# Load the mapping and import the core runlevel roles
- name: Custom Configuration Mapping
  hosts: localhost
  connection: local
  gather_facts: yes
  vars_files:
    - vars/runlevel-mapping.yml
  tasks:
    - name: Import the core Runlevels
      ansible.builtin.import_role:
        name: cloudera.exe.sequence
```

## Tag Extension

Playbook developers that import the `cloudera.exe.sequence` role (or other future "orchestration" roles) can add both additional and existing "runlevel" tags to invoke other roles or tasks. This technique is well-suited for extending the core to handle [additional runlevels](#additional-runlevels).

For example, to add a pre-deploy role:

```yaml
# custom-setup.yml

- name: Pre-install dialogue
  hosts: localhost
  connection: local
  gather_facts: yes
  tasks:
    - name: Talk to the animals, walk with the animals
      ansible.builtin.include_role:
        name: my_namespace.my_collection.animals
        apply:
          tags:
            - validate
            - infra
            - plat
            - run
            - animals
            - ml
            - dw
            - opdb
            - dh
      tags:
        - validate
        - infra
        - plat
        - run
        - animals
        - ml
        - dw
        - opdb
        - dh
    - name: Import the core Runlevels (and their tags)
      ansible.builtin.import_role:
        name: cloudera.exe.sequence
```

This example above can execute just the _pre-setup_ role:

```bash
ansible-playbook custom-setup.yml -t animals
```
as well as the "active" runlevels used by the default `sequence` role:

```bash
ansible-playbook custom-setup.yml -t plat
```

# Additional Runlevels

Developers can handle the other runlevels not covered by the core roles, i.e. [Installation](runlevels.md#installation), [Application](runlevels.md#application), and [Operations](runlevels.md#operations), by several different means.

For some use cases, writing your own "orchestration" role and calling each core role directly provides the most control, yet also carries the burden of the correct tag structure to maintain the runlevel prerequisites.

For example, adding an explicit `install` tag to execute the [Installation](runlevels.md#installation) runlevel:

```yaml
# install-runlevel-example.yml

- name: Install Runlevel Example
  hosts: localhost
  connection: local
  gather_facts: yes
  tasks:
    - name: Validate Infrastructure Configuration
      ansible.builtin.include_role:
        name: cloudera.exe.infrastructure
        tasks_from: validate
        apply:
        tags:
            - validate
            - infra
            - plat
            - run
            - install
            - ml
            - dw
            - opdb
            - dh
      tags:
        - validate
        - infra
        - plat
        - run
        - install
        - ml
        - dw
        - opdb
        - dh

    - name: Validate Platform Configuration
      ansible.builtin.include_role:
        name: cloudera.exe.platform
        tasks_from: validate
        apply:
        tags:
            - validate
            - plat
            - run
            - install
            - ml
            - dw
            - opdb
            - dh
      tags:
        - validate
        - plat
        - run
        - install
        - ml
        - dw
        - opdb
        - dh

    - name: Validate Runtime Configuration
      ansible.builtin.include_role:
        name: cloudera.exe.runtime
        tasks_from: validate
        apply:
        tags:
            - validate
            - run
            - install
            - ml
            - dw
            - opdb
            - dh
      tags:
        - validate
        - run
        - install
        - ml
        - dw
        - opdb
        - dh

    - name: Validate Installation Configuration
      ansible.builtin.include_role:
        name: my_namespace.my_collection.my_app_role
        tasks_from: validate
        apply:
          tags:
            - validate
            - install
      tags:
        - validate
        - install

    ... so on and so forth ...

```

## Dependencies

Additional runlevels commonly have a dependency on the `cloudera.exe.common` role; in the example above, the `my_namespace.my_collection.my_app_role/meta/main.yml` could have an entry in the `dependencies` parameter referencing `cloudera.exe.common`.
