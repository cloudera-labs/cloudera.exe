# Testing cloudera.exe

The collection is migrating from `ansible-test` to `pytest` and `molecule` for unit and integration testing. In addition, we use `pre-commit` to handle linting and formatting both for `git` commits and for various Github Action workflows in the repository.

## Setup

To set up a development and test environment for the collection, you need to:

1. Set up the Ansible Collection and Role paths
1. Install Ansible and the Python dependencies
1. Install the collection and its dependencies
1. Configure the PYTHONPATH to use the correct location of the collections code
1. Install the Molecule driver dependencies

### Ansible Collection and Role Paths

You have to install your Ansible collections, both the collection under test and its dependencies, into the `ansible_collections/<namespace>/<name>` folder structure.  For the collection under test, run the following _in the parent directory of your choosing_:

```bash
git clone https://github.com/cloudera-labs/cloudera.exe.git ansible_collections/cloudera/exe
```

Then create the `roles` directory in the _parent directory_:

```bash
mkdir roles
```

Lastly, set the Ansible [COLLECTION](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#envvar-ANSIBLE_COLLECTIONS_PATH) and [ROLE](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#envvar-ANSIBLE_ROLES_PATH) configurations for these two locations:

```bash
export ANSIBLE_COLLECTIONS_PATH=$(pwd)
export ANSIBLE_ROLES_PATH="$(pwd)/roles"
```

### Set the PYTHONPATH

Include the `ANSIBLE_COLLECTIONS_PATH` variable to the `PYTHONPATH` to allow module imports.

```bash
export PYTHONPATH="${ANSIBLE_COLLECTIONS_PATH}":"${PYTHONPATH}"
```

### Ansible

Set up a development `virtualenv` and install `ansible-core~=2.16.0` and `ansible-navigator`.

```bash
pip install ansible-core~=2.16.0 ansible-navigator
```

> [!warning]
> Installing `>=2.17` will require that the target hosts run Python 3.7. This requirement extends to RHEL 8.x and its `platform-python`, which means that `2.17` will not work on these platforms.

### Python Dependencies

Install the development and collection Python requirements from the `requirements-dev.txt` and `requirements.txt` files respectively in the project root.

```bash
pip install -r ansible_collections/cloudera/exe/requirements.txt
pip install -r ansible_collections/cloudera/exe/requirements-dev.txt
```

### Collection Dependencies

You also need to install the collection's dependencies and install them into the `ANSIBLE_COLLECTIONS_PATH`:

```bash
ansible-galaxy collection install -r ansible_collections/cloudera/exe/requirements.yml -p "${ANSIBLE_COLLECTIONS_PATH}"
```

And install any role dependencies as well into the `ANSIBLE_ROLES_PATH`:

```bash
ansible-galaxy role install -r ansible_collections/cloudera/exe/requirements.yml -p "${ANSIBLE_ROLES_PATH}"
```

If the collection has any system requirements, run `bindep` on its requirements file:

```bash
bindep -f ansible_collections/cloudera/exe/bindep.txt
```

### Molecule

Running the `molecule` tests requires `podman` as the container engine, so you will need to install that service on your test machine. Read more about [Podman](https://podman.io/) or [Podman Desktop](https://podman-desktop.io/).

## Testing

You can either run standalone `molecule`, for roles and more advanced integration testing, or `pytest`. The latter is set up to run any and all tests, including `molecule` scenarios.

### Running standalone `molecule` tests

Currently, `molecule` scenarios are located in the `extensions/molecule` directory of the collection. To run a scenario, change to `extensions` as your current working directory and then run `molecule`. For example:

| Command | Description |
| --- | --- |
| `molecule test -s rdbms_server_postgresql_14_tls` | Execute the full test lifecyle for the PostgreSQL 14 server role with TLS |
| `molecule create -s rdbms_server_postgresql_14_tls` | Create the `platforms`, i.e. the inventory, that are the target hosts of the role testing |
| `molecule prepare -s rdbms_server_postgresql_14_tls` | Prep the target hosts for testing the roles |
| `molecule converge -s rdbms_server_postgresql_14_tls` | Run the testing playbook, i.e. converge the test code, on the target hosts |
| `molecule side-effect -s rdbms_server_postgresql_14_tls` | Prep the target hosts, post-`converge`, for any additional setup prior to verification or idempotency testing |
| `molecule verify -s rdbms_server_postgresql_14_tls` | Verify the target hosts |
| `molecule cleanup -s rdbms_server_postgresql_14_tls` | Clean up any resources, for example, temporary files created on the controller |
| `molecule destroy -s rdbms_server_postgresql_14_tls` | Destroy the `platform` hosts |

You can limit testing to a `platform` within a scenario by using the `-p/--platform-name` parameter (or via the `MOLECULE_PLATFORM_NAME` environment variable):

```bash
molecule test -s rdbms_server_postgresql_14_tls -p rhel9.4
```

To stop tests from destroying the platforms after encountering an error (or at all, even on a successful test), pass the `--destroy=never` parameter:

```bash
molecule test -s rdbms_server_postgresql_14_tls -p rhel9.4 --destroy=never
```

You can log into a running platform via the `login` subcommand and the `-h/--host` parameter:

```bash
molecule login -s rdbms_server_postgresql_14_tls -h rhel9.4
```

As well as pass extra parameters to the underlying playbook (`converge` command only!):

```bash
molecule converge -s rdbms_server_postgresql_14_tls -- -vvv -t tls_config
```

### Running `pytest` tests

We use the `ansible-pytest` plugin to run unit and integration tests for the collection.

To see what tests (unit and integration) are available, run the following from the `ANSIBLE_COLLECTIONS_PATH` directory:

```bash
pytest ansible_collections/cloudera/exe --collect-only
```

You should see something like:

```
platform darwin -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
ansible: 2.16.11
rootdir: /Users/wmudge/Devel/ansible_collections/cloudera/exe
configfile: pyproject.toml
testpaths: tests
plugins: ansible-24.9.0, xdist-3.6.1
collected 8 items

<Dir exe>
  <Dir tests>
    <Dir integration>
      <Module test_molecule_integration.py>
        <Function test_integration[extensions-rdbms_server_postgresql_14_tls]>
        <Function test_integration[extensions-rdbms_server_postgresql_default]>
        <Function test_integration[extensions-rdbms_server_postgresql_14]>
        <Function test_integration[platform-default]>
        <Function test_integration[platform-level0]>
        <Function test_integration[runtime-default]>
        <Function test_integration[runtime-level0]>
    <Package unit>
      <Package plugins>
        <Package filter>
          <Module test_core_exe.py>
            <UnitTestCase TestFilterModule>
              <TestCaseFunction test_combine_onto>
```

To run a selected test, execute with a regex:

```bash
pytest ansible_collections/cloudera/exe -k "postgresql_14_tls"
```

To run a Molecule scenario on a selected platform, i.e. target host, set the platform via the environment variable:

```bash
MOLECULE_PLATFORM_NAME="rhel9.4" pytest ansible_collections/cloudera/exe -k "postgresql_14_tls"
```

> [!warning]
> If you run `pytest` in the root of the collection, `pytest` will copies the current collection into the required Ansible collection path structure within the working directory. That is, running `pytest` at the root of the **collection** creates a `collection/ansible_collections/<namespace>/<name>` **within** the collection.
> Thus, our recommendation is that you can run `pytest` in at the root of the **Ansible collections path**. That is, run `pytest ansible_collections/<namespace>/<name> ...` so that `pytest` doesn't have to bootstrap the collections path.

## Linting and Commits

The `pre-commit` Python application is used to manage linting and other housekeeping functions. The application is installed as a `git` hook and as a Github workflow check.

Commits and pull requests will fail if your contributions do not pass the `pre-commit` checks.  You can check your work-in-progress code by running the following:

```bash
pre-commit run -a
```

---

# Testing

This project uses [Hatch](https://hatch.pypa.io/dev/) to manage the project's dependencies, testing environments, and other activities. It also makes heavy use of [Ansible Molecule](https://ansible.readthedocs.io/projects/molecule/) and employs the [EC2 driver](https://github.com/ansible-community/molecule-plugins) to test using cloud instances.

## Setup

### Hatch Build System

You should install `hatch` as [per its documentation](https://hatch.pypa.io/dev/install/#installers). `hatch` should be able to handle all dependencies, including Python versions and virtual environments.

> [!danger] OSX `dirs.data` default!
> The [default data directory](https://hatch.pypa.io/1.13/config/hatch/#data) for `hatch` is `~/Library/Application Support/hatch`, which causes trouble for `molecule`! You might need to change this location to a path with spaces!

### AWS Credentials

You will need valid AWS credentials set in your environment for `molecule` to operate successfully.

In addition, make sure you have a default region declared, either in your `AWS_PROFILE` or `AWS_DEFAULT_REGION`.

### Test Network

`molecule` only manages the EC2 instances, not the VPC and associated networking.  To set up the required infrastructure, you can run the following `hatch` commands.

```bash
hatch run molecule:init
```

This will initialize the `tests/terraform` project which establishes the testing network in AWS.

```bash
hatch run molecule:setup
```

This command executes the `tests/terraform` project.

Once your network is set up, be sure to set the `TEST_VPC_SUBNET_ID` and `TEST_VPC_SECURITY_GROUP` variables with the public subnet ID and intra-traffic security group name, respectively, of your testing network.

```bash
$(hatch run molecule:export-subnet)
$(hatch run molecule:export-security-group)
```

## Execution

Running `molecule` is straightforward. First, enable the `hatch` environment:

```bash
hatch shell molecule
```

And then change into the role directory that you wish to test, e.g. `cd roles/prereq_thp`, and run `molecule` from there.

> [!info]
> In some cases, you might need to set your `ANSIBLE_ROLES_PATH` to the `roles` directory of this project.

## Teardown

First, make sure that you have destroyed any `molecule` scenarios that are using your test infrastructure.

And then, from the _project root_, run:

```bash
hatch run molecule:teardown
```
