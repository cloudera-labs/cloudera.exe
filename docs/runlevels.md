# CDP Deployment Runlevels

The core role, `cloudera.exe.sequence`, employs Ansible tags to drive [runlevel](https://en.wikipedia.org/wiki/Runlevel)-like functionality for CDP deployments. The `sequence` role ensures that each runlevel state is met, coordinating the tearing down of higher-level runlevels, setting up lower-level runlevels, and reconciling existing state of current runlevels.

*Deployment Runlevels*

Runlevel | Tag
--- | ---
[Teardown](#teardown) | `teardown`
[Validation](#validation) | `validation`
[Initialization](#initialization) | none
[Infrastructure](#infrastructure) | `infra`
[Platform](#platform) | `plat`
[Runtime](#runtime) | `run`
[Installation](#installation)| `install` (not implemented by `cloudera.exe`)
[Application](#application)| `app` (not implemented by `cloudera.exe`)
[Operations](#operations) | none

# Execution

Using these tags within a playbook that has imported `cloudera.exe.sequence` is straightforward Ansible.

```bash
# Validate the configuration
ansible-playbook main.yml -t validate

# Set up everything (infra, platform, runtime)
ansible-playbook main.yml

# Destroy the runtime, but keep/reconcile infra and plat
ansible-playbook main.yml -t plat

# Rebuild the runtime, but skip the infra reconciliation
ansible-playbook main.yml -t run --skip-tags infra

# Take it all down
ansible-playbook main.yml -t teardown
```

# Definitions

## Teardown
Destroys all cloud provider and CDP assets, subject to configuration allowances. This runlevel is in scope of the `cloudera.exe` collection.

The runlevel is invoked with the `teardown` tag.

## Validation
Checks the incoming configuration parameters for errors and misalignment. No external interaction. This runlevel is in scope of the `cloudera.exe` collection.

The runlevel is invoked with the `validate` tag.

## Initialization
Checks and initializes authentication and authorization for the cloud and VM control planes as well as validate access to bare-metal systems. External interaction is read-only. This runlevel is in scope of the `cloudera.exe` collection.

The runlevel is not directly invocable.

## Infrastructure
Manages cloud-provider resources, VM control planes, instance OS and services management, networking, etc. This runlevel is in scope of the `cloudera.exe` collection.

The runlevel is invoked with the `infra` tag.

## Platform
Installs and manages CDP and its shared and base elements, e.g. SDX, Credentials, IAM users and groups. This runlevel is in scope of the `cloudera.exe` collection.

The runlevel is invoked with the `plat` tag.

## Runtime
Installs and manages the computing infrastructures of CDP, e.g. DWX, CML. This runlevel is in scope of the `cloudera.exe` collection.

The runlevel is invoked with the `run` tag.

## Installation
Executes post-runtime and platform configurations. This runlevel is outside the scope of the `cloudera.exe` collection. Actual runtime projects should define or import additional runlevel roles and/or tasks as required.

The suggested tag for this runlevel is `install`.

## Application
Executes user- and application-specific tasks, e.g. table definitions, security policy configurations, data loading and management. This runlevel is outside the scope of the `cloudera.exe` collection. Actual runtime projects should define or import additional runlevel roles and/or tasks as required.

The suggested tag for this runlevel is `app`.

## Operations
Executes management tasks broadly. This runlevel is outside the scope of the `cloudera.exe` collection. Actual runtime projects should define or import additional runlevel roles and/or tasks as required.

There are no suggested tags for this runlevel.
