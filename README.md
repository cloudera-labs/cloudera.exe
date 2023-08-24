# cloudera.exe - Runlevel Management and Utilities for Cloudera Data Platform (CDP)

Readme last updated: 2022-04-07

`cloudera.exe` is an Ansible collection enabling runlevel management of CDP Public Cloud deployments. The collection also contains a number of utilities for common scenarios encountered when managing a CDP deployment.

The collection provides the following roles:

Role | Description
--- | ---
sequence | Runlevel-like "orchestration" of CDP Public Cloud deployments
infrastructure | Cloud provider assets and IaaS
platform | CDP Public Cloud assets, including Environments, Datalakes, Users and Groups, etc.
runtime | CDP Experiences, including Machine Learning, Datahubs, etc.
info | Comprehensive readout of all CDP Public Cloud elements within an Environment
data | Manage external data locations for CDP Public Cloud deployments
common | Shared variables for all roles within collection

# Installation

To install the `cloudera.exe` collection, you have several options. Please note that to date, we have not yet published this collection to the public Ansible Galaxy server, so you cannot install it via direct namespace declaration, rather you must specify a Git project and (optionally) branch.

The collection has several dependencies that should resolve automatically via the
`ansible-galaxy` command:
 
- [cloudera.cloud](https://github.com/cloudera-labs/cloudera.cloud.git) (on Cloudera Labs)
- [ansible.netcommon](https://github.com/ansible-collections/ansible.netcommon)
- [community.general](https://github.com/ansible-collections/community.general)

You may want to install additional cloud provider collections depending on your target platform:

| Cloud Provider | Dependency | Version |
| Azure | [azure.azcollection](https://github.com/ansible-collections/azure) | `1.11.0` |
|| [netapp.azure](https://github.com/ansible-collections/netapp.azure) | `21.10.0` |
| AWS | [amazon.aws](https://github.com/ansible-collections/amazon.aws) | `3.0.0` |
|| [community.aws](https://github.com/ansible-collections/community.aws) | `3.0.1` |
| GCP | [google.cloud](https://github.com/ansible-collections/google.cloud) | `1.0.2` |

## Option #1: Install from GitHub

Create or edit the `collections/requirements.yml` file in your project with the
following:

```yaml
collections:
  - name: https://github.com/cloudera-labs/cloudera.exe.git
    type: git
    version: main
```

And then run in your project:

```bash
ansible-galaxy collection install -r collections/requirements.yml
```

## Option #2: Install the tarball

Periodically, the collection is packaged into a distribution which you can
install directly:

```bash
ansible-galaxy collection install <collection-tarball> -p collections/
```

# Requirements

The `cloudera.exe` collection interacts with both CDP and cloud provider endpoints.

> **NOTE:** At minimum, you will need to install the *base* Python libraries and your target cloud provider libraries. You may choose to install all the cloud provider libraries, if desired.

> **NOTE #2:** We highly recommend using virtual environments for managing these dependencies!

The collection requires Ansible `2.10.0` or higher. 

`cloudera.exe` depends on the following other collections, all of which should be automatically resolved through `ansible-galaxy`.

+ `cloudera.cloud`
+ `ansible.netcommon`
+ `community.general`

You will need to add the following, depending on your target deployment:

+ `community.aws`
+ `amazon.aws`
+ `azure.azcollection`
+ `google.cloud`
+ `netapp.azure`

## Python

The collection has several Python libraries that are needed to support the roles and the underlying modules, i.e. the *base* libraries, including:

*Ansible*

+ `jmespath`
+ `netaddr`

*CDP*

+ `cdpy` (See [cdpy](https://github.com/cloudera-labs/cdpy) on Cloudera Labs)

The [`requirements.txt`](./requirements.txt) file declares these libraries. You may install them via `pip`:

```bash
pip install -r requirements.txt
```

## Amazon Web Services

For AWS, you need to install the following Python libraries:

+ `awscli`
+ `boto`
+ `botocore`
+ `boto3`

The [`requirements_aws.txt`](./requirements_aws.txt) file declares these libraries. You may install them via `pip`:

```bash
pip install -r requirements_aws.txt
```

## Microsoft Azure

For Azure, you must first install the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) for your OS.

Then install the following Python libraries:

+ All of the [Azure Collection requirements](https://raw.githubusercontent.com/ansible-collections/azure/dev/requirements-azure.txt)
+ `azure-mgmt-netapp`

The [`requirements_azure.txt`](./requirements_azure.txt) file declares these libraries. You may install them via `pip`:

```bash
pip install -r requirements_azure.txt
```

## Google Cloud

For Google Cloud, you must first install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) for your OS.

Then install the following Python libraries:

+ `google-auth`

The [`requirements_gcp.txt`](./requirements_gcp.txt) file declares these libraries. You may install them via `pip`:

```bash
pip install -r requirements_gcp.txt
```

# Using the Collection

See the [execution examples](docs/runlevels.md#execution) in the Deployment Runlevels document.

For more information on the collection, check out:

+ [Configuration Guide](docs/configuration.md)
+ [Runlevels Guide](docs/runlevels.md)
+ [Architecture and Design Guide](docs/design.md)

# Getting Involved

Contribution instructions are coming soon!

# License and Copyright

Copyright 2022, Cloudera, Inc.

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
