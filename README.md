# cloudera.exe - Runlevel Management and Utilities for Cloudera Data Platform (CDP)

[![API documentation](https://github.com/cloudera-labs/cloudera.exe/actions/workflows/publish_docs.yml/badge.svg?branch=main&event=push)](https://github.com/cloudera-labs/cloudera.exe/actions/workflows/publish_docs.yml)

`cloudera.exe` is an Ansible collection that offers runlevel management of your **[Cloudera Data Platform (CDP)](https://www.cloudera.com/products/cloudera-data-platform.html) Public Cloud and Private Cloud** deployments. The collection contains a number of utilities for common scenarios encountered when managing a CDP deployment, including:
* Set up and management of external dependencies, e.g. database, Kerberos, LDAP
* Execution of Common deployment sequences (via importable playbooks)

The collection is unabashedly an _opinionated_ approach of managing your CDP resources - it's resources can be used to set up your CDP infrastructure, configure the host machines, install and configure CDP and its services, and more. The collection interacts across several control planes from CDP Public Cloud and cloud provider endpoints to Cloudera Manager for CDP Private Cloud and Public Cloud Data Hubs. In short, it has opinions about how to get things done. If you are looking for automation resources that _only_ interact with CDP resources - that is, assets that are focused solely on Cloudera software - please look at [`cloudera.cloud` for Public Cloud](https://github.com/cloudera-labs/cloudera.cloud) and [`cloudera.cluster` for Private Cloud and Cloudera Manager](https://github.com/cloudera-labs/cloudera.cluster).

Core to the collection is the [configuration file](./docs/configuration.yml) which many of the collection's roles use as a central "switchboard" for their functions. The collection works hand-in-hand with the [`cloudera-deploy` application](https://github.com/cloudera-labs/cloudera-deploy/) to execute _definitions_ which include variations on this configuration; many of the functions in `cloudera-deploy` have relocated to this collection to streamline its use.

The collection provides _playbooks_, _roles_, and _plugins_ for working with CDP deployments. Notably, the playbooks encapsulate typical set up and tear down deployment operations, aka runlevels:

| Name | Description |
| --- | --- |
| `pbc_infra_setup.yml` | Public Cloud infrastructure setup (AWS, Azure, GCP), using either Terraform or Ansible |
| `pbc_infra_teardown.yml` | Public Cloud infrastructure teardown (AWS, Azure, GCP), using either Terraform or Ansible |
| `pbc_setup.yml` | Public Cloud Datalake and Data Services setup |
| `pbc_teardown.yml` | Public Cloud Datalake and Data Services teardown |
| `pvc_base_postfix.yml` | Private Cloud setup, postfix |
| `pvc_base_prereqs_ext.yml` | Private Cloud external dependencies, e.g. JVM, Kerberos, database |
| `pvc_base_prereqs_int.yml` | Private Cloud internal dependencies, e.g. Cloudera Manager server and agent install |
| `pvc_base_setup.yml` | Private Cloud cluster setup |
| `pvc_base_teardown.yml` | Private Cloud cluster teardown |

`cloudera.exe`-powered applications, like `cloudera-deploy`, import these playbooks to enable these runlevel operations.

The other collection assets - the _roles_ and _plugins_ - are detailed in the [API documentation](https://cloudera-labs.github.io/cloudera.exe/). While these resource can be used separately, most expect the common configuration noted above and a sequence of execution defined within the noted playbooks.

## Quickstart

1. [Install the collection](#installation)
2. [Install the requirements](#requirements)
3. [Use the collection](#using-the-collection)

## API

See the [API documentation](https://cloudera-labs.github.io/cloudera.exe/) for details for each plugin and role within the collection. 

## Roadmap

If you want to see what we are working on or have pending, check out:

*  the [Milestones](https://github.com/cloudera-labs/cloudera.exe/milestones) and [active issues](https://github.com/cloudera-labs/cloudera.exe/issues?q=is%3Aissue+is%3Aopen+milestone%3A*) to see our current activity,
* the [issue backlog](https://github.com/cloudera-labs/cloudera.exe/issues?q=is%3Aopen+is%3Aissue+no%3Amilestone) to see what work is pending or under consideration, and
* read up on the [Ideas](https://github.com/cloudera-labs/cloudera.exe/discussions/categories/ideas) we have in mind.

Are we missing something? Let us know by [creating a new issue](https://github.com/cloudera-labs/cloudera.exe/issues/new) or [posting a new idea](https://github.com/cloudera-labs/cloudera.exe/discussions/new?category=ideas)!

## Contribute

For more information on how to get involved with the `cloudera.exe` Ansible collection, head over to [CONTRIBUTING.md](CONTRIBUTING.md).

## Installation

To install the `cloudera.exe` collection, you have several options. Please note that to date, we have not yet published this collection to the public Ansible Galaxy server, so you cannot install it via direct namespace declaration, rather you must specify a Git project and (optionally) branch.

### Option #1: Install from GitHub

Create or edit the `requirements.yml` file in your project with the
following:

```yaml
collections:
  - name: https://github.com/cloudera-labs/cloudera.exe.git
    type: git
    version: main
```

And then run in your project:

```bash
ansible-galaxy collection install -r requirements.yml
```

You can also install the collection directly:

```bash
ansible-galaxy collection install git+https://github.com/cloudera-labs/cloudera.exe.git@main
```

### Option #2: Install the tarball

Periodically, the collection is packaged into a distribution which you can
install directly:

```bash
ansible-galaxy collection install <collection-tarball>
```

See [Building the Collection](#building-the-collection) for details on creating a local tarball.

## Requirements

The `cloudera.exe` expects `ansible-core>=2.10,<2.13`.

> [!WARNING]
> The current functionality of the `cloudera.cluster` dependency does not yet work with Ansible version `2.13` and later.

The collection has the following _required_ dependencies:

| Name | Type | Version |
|------|------|---------|
| `cloudera.cloud` | collection | `main` |
| `cloudera.cluster` | collection | `main` |
| `ansible.netcommon` | collection | `2.5.1` |
| `community.general` | collection | `4.5.0` |

You will need to add the following, depending on your target deployment, but all are collectively _optional_ dependencies:

**Private Cloud**

See the [requirements for `cloudera-labs/cloudera.cluster`](https://github.com/wmudge/cloudera.cluster#requirements) for details.

| Name | Type | Version |
|------|------|---------|
| `community.mysql` | collection | `3.8.0` |
| `community.postgresql` | collection | `3.3.0` |
| `freeipa.ansible_freeipa` | collection | `1.11.1` |
| `geerlingguy.postgresql` | role | `3.3.0` |
| `geerlingguy.mysql` (patched) | role | `master` |

**Terraform**

If you intend to use Terraform as your infrastructure engine within the `cloudera.exe.infra` role, then install the following: 

| Name | Type | Version |
|------|------|---------|
| `cloud.terraform` | collection | `1.1.1` |

**AWS**

See the [AWS Execution Environment configuration](https://github.com/cloudera-labs/cldr-runner/blob/main/aws/execution-environment.yml) in `cloudera-labs/cldr-runner` for details on setting up the Python and system requirements.

| Name | Type | Version |
|------|------|---------|
| `amazon.aws` | collection | `3.0.0` |
| `community.aws` | collection | `3.0.1` |

**Azure**

See the [Azure Execution Environment configuration](https://github.com/cloudera-labs/cldr-runner/blob/main/azure/execution-environment.yml) in `cloudera-labs/cldr-runner` for details on setting up the Python and system requirements.

| Name | Type | Version |
|------|------|---------|
| `azure.azcollection` | collection | `1.11.0` |
| `netapp.azure` | collection | `21.10.0` |

**GCP**

See the [GCP Execution Environment configuration](https://github.com/cloudera-labs/cldr-runner/blob/main/gcp/execution-environment.yml) in `cloudera-labs/cldr-runner` for details on setting up the Python and system requirements.

| Name | Type | Version |
|------|------|---------|
| `google.cloud` | collection | `1.0.2` |

The collection also requires the following Python libraries to operate its modules and tasks:

  * [netaddr](https://pypi.org/project/netaddr/)

The collection's Python dependencies alone, _not_ the required Python libraries of its collection dependencies, are in `requirements.txt`.

All collection dependencies, required and optional, can be found in `requirements.yml`; only the _required_ **non-Cloudera** dependencies are in `galaxy.yml`. `ansible-galaxy` will install only the _required_ **non-Cloudera** collection dependencies; you will need to add `cloudera.cloud`, `cloudera.cluster`, and the _optional_ collection dependencies as needed (see above).

`ansible-builder` can discover and install all Python dependencies - current collection and dependencies - if you wish to use that application to construct your environment. Otherwise, you will need to read each collection and role dependency and follow its installation instructions.

See the [Collection Metadata](https://ansible.readthedocs.io/projects/builder/en/latest/collection_metadata/) section for further details on how to install (and manage) collection dependencies.

You may wish to use a _virtual environment_ to manage the Python dependencies.

## Using the Collection

This collection is designed to work hand-in-hand with the [`cloudera-deploy` application](https://github.com/cloudera-labs/cloudera-deploy), which uses the reference playbooks in the `playbooks` directory to drive the operations of its example definitions.

Once installed, reference the collection in your playbooks and roles.

For example, here we use the
[`cloudera.exe.init_deployment` role](https://github.com/cloudera-labs/cloudera.exe/tree/main/roles/init_deployment) to read the configuration details and then import the Public Cloud playbooks to set up and provision an Environment and Datalake:

```yaml
- name: Marshal the variables
  hosts: localhost
  connection: local
  gather_facts: yes
  tasks:
    - name: Read definition variables
      ansible.builtin.include_role:
        name: cloudera.exe.init_deployment
        public: yes
      when: init__completed is undefined
  tags:
    - always

- name: Set up CDP Public Cloud infrastructure (Ansible-based)
  ansible.builtin.import_playbook: cloudera.exe.pbc_infra_setup.yml

- name: Set up CDP Public Cloud (Env and DL example)
  ansible.builtin.import_playbook: cloudera.exe.pbc_setup.yml
```

> [!IMPORTANT]
> You **must** run `cloudera.exe.init_deployment` before calling any of the collection's playbooks. This call must occur within the source project, otherwise Ansible's `playbook_dir` will change to the collection's installation directory and variable lookups might not work as expected.

### Legacy Execution Modes

> [!WARNING]
> These documents and their modes of operation are deprecated in version 2.x. For example, the use of Ansible tags to trigger coarse runlevels have been replaced by explicit playbook execution. However, the "inner" tag structures still remain and might be relevant to some execution modes.

See the [execution examples](docs/runlevels.md#execution) in the Deployment Runlevels document.

For more information on the collection, check out:

+ [Configuration Guide](docs/configuration.md)
+ [Runlevels Guide](docs/runlevels.md)
+ [Architecture and Design Guide](docs/design.md)

## Building the Collection

To create a local collection tarball, run:

```bash
ansible-galaxy collection build 
```

## Building the API Documentation

To create a local copy of the API documentation, first make sure the collection is in your `ANSIBLE_COLLECTIONS_PATHS`. Then run the following:

```bash
# change into the /docsbuild directory
cd docsbuild

# install the build requirements (antsibull-docs); you may want to set up a
# dedicated virtual environment
pip install ansible-core https://github.com/cloudera-labs/antsibull-docs/archive/cldr-docsite.tar.gz

# Install the collection's build dependencies
pip install requirements.txt

# Then run the build script
./build.sh
```

## License and Copyright

Copyright 2023, Cloudera, Inc.

```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
