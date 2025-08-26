# cloudera.exe - Tools and Utilities for Cloudera Deployments

[![API documentation](https://github.com/cloudera-labs/cloudera.exe/actions/workflows/publish_docs.yml/badge.svg?branch=main&event=push)](https://github.com/cloudera-labs/cloudera.exe/actions/workflows/publish_docs.yml)

`cloudera.exe` is an Ansible collection for helping setup **[Cloudera Data Platform (CDP)](https://www.cloudera.com/products/cloudera-data-platform.html) on cloud (Public Cloud) and on premise (Private Cloud)** deployments. The collection contains a number of utilities for common scenarios encountered when managing a deployment, including:

* Supporting databases
* Kerberos
* LDAP
* TLS
* Cloudera Manager Server and Agent binaries
* Repositories
* OS kernel best practices

The collection is unabashedly an _opinionated_ approach of managing your resources - its resources can be used to configure the host machines, install and configure Cloudera and its services, and more. To be clear, **these resources are OPTIONAL**, yet they are helpful for greenfield, developer-centric, and quickstart deployments.  The collection interacts with cloud provider endpoints to host systems. In short, it has opinions about how to get things done.

If you are looking for automation resources that _only_ interact with Cloudera resources - that is, assets that are focused solely on Cloudera software - please look at [`cloudera.cloud`](https://github.com/cloudera-labs/cloudera.cloud) and [`cloudera.cluster`](https://github.com/cloudera-labs/cloudera.cluster).

## Quickstart

See the [API documentation](https://cloudera-labs.github.io/cloudera.exe/) for details for each plugin and role within the collection.

1. [Install the collection](#installation)
2. [Install the requirements](#requirements)
3. [Use the collection](#using-the-collection)

## Roadmap

If you want to see what we are working on or have pending, check out:

* the [Milestones](https://github.com/cloudera-labs/cloudera.exe/milestones) and [active issues](https://github.com/cloudera-labs/cloudera.exe/issues?q=is%3Aissue+is%3Aopen+milestone%3A*) to see our current activity,
* the [issue backlog](https://github.com/cloudera-labs/cloudera.exe/issues?q=is%3Aopen+is%3Aissue+no%3Amilestone) to see what work is pending or under consideration, and
* read up on the [Ideas](https://github.com/cloudera-labs/cloudera.exe/discussions/categories/ideas) we have in mind.

Are we missing something? Let us know by [creating a new issue](https://github.com/cloudera-labs/cloudera.exe/issues/new) or [posting a new idea](https://github.com/cloudera-labs/cloudera.exe/discussions/new?category=ideas)!

## Contribute

For more information on how to get involved with the `cloudera.exe` Ansible collection, head over to [CONTRIBUTING.md](CONTRIBUTING.md).

## Installation

To install the `cloudera.exe` collection, you have several options.

The preferred method is to install via Ansible Galaxy; in your `requirements.yml` file, add the following:

```yaml
collections:
  - name: cloudera.exe
```

If you want to install from GitHub, add to your `requirements.yml` file:
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
# From Ansible Galaxy
ansible-galaxy collection install cloudera.exe
```

```bash
# From GitHub
ansible-galaxy collection install git+https://github.com/cloudera-labs/cloudera.exe.git@main
```

`ansible-builder` can discover and install all Python dependencies - current collection and dependencies - if you wish to use that application to construct your environment. Otherwise, you will need to read each collection and role dependency and follow its installation instructions.

See the [Collection Metadata](https://ansible.readthedocs.io/projects/builder/en/latest/collection_metadata/) section for further details on how to install (and manage) collection dependencies.

You may wish to use a _virtual environment_ to manage the Python dependencies.

## Using the Collection

This collection is designed to help you get up and running with Cloudera on cloud and on premise.  It is decidedly _opinionated_ -- that is, these roles and plugins make assumes as to how certain configurations and requirements are met. **THESE RESOURCES ARE COMPLETELY OPTIONAL. THEY EXIST ONLY TO ASSIST YOU WITH BOOTSTRAPPING AND GREENFIELD EXAMPLES!**

Feel free to use these resources as needed!

Once installed, reference the collection in playbooks and roles.

For example, here we use the
[`cloudera.exe.cm_agent` role](https://github.com/cloudera-labs/cloudera.exe/tree/main/roles/cm_agent) to download and install the Cloudera Manager agent software from the Cloudera Archive repository:

```yaml
- name: Install the CM agent
  hosts: cluster_hosts
  gather_facts: yes
  tasks:
    - name: Install the agent and register with Cloudera Manager
      ansible.builtin.import_role:
        name: cloudera.exe.cm_agent
      vars:
        cloudera_manager_host: cm.example.internal
```

## Building the API Documentation

If you wish to create a local copy of the API documentation, first set up the `hatch` build tool, as shown in the [TESTING](./TESTING.md) guide.

Then, you can run:

```bash
hatch run docs:build
```

This will kick off the build toolchain. The local documentation can be found in `docsbuild/build/html`.

## License and Copyright

Copyright 2025, Cloudera, Inc.

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
