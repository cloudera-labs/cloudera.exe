# Testing cloudera.exe

This project uses [Hatch](https://hatch.pypa.io/dev/) to manage the project dependencies, testing environments, common utilities and scripts, and other activities. It also makes heavy use of [pytest](https://pytest.org), [Ansible Molecule](https://ansible.readthedocs.io/projects/molecule/), and employs the [EC2 driver](https://github.com/ansible-community/molecule-plugins) to test using cloud instances (if needed).  We also use [pre-commit](https://pre-commit.com/), [antsibull-docs](https://ansible.readthedocs.io/projects/antsibull-docs/), and [ansible-lint](https://ansible.readthedocs.io/projects/lint/) for linting and hygiene.

To set up a development and test environment for the collection, you need to:

1. Set up the Hatch build system
1. Set up the Ansible Collection and Role paths
1. Configure the PYTHONPATH to use the correct location of the collections code
1. Install the Molecule driver dependencies (AWS resources)

## Hatch Build System

You should install `hatch` as [per its documentation](https://hatch.pypa.io/dev/install/#installers). `hatch` should be able to handle all dependencies, including Python versions and virtual environments.

> [!danger] OSX `dirs.data` default!
> The [default data directory](https://hatch.pypa.io/1.13/config/hatch/#data) for `hatch` is `~/Library/Application Support/hatch`, which causes trouble for `molecule`! You might need to change this location to a path with spaces!

## Ansible Collection and Role Paths

You have to install your Ansible collections, both the collection under test and its dependencies, into the `ansible_collections/<namespace>/<name>` folder structure.  For the collection under test, run the following _in the parent directory of your choosing_:

```bash
git clone https://github.com/cloudera-labs/cloudera.exe.git ansible_collections/cloudera/exe
```

Then create the `roles` directory in this _parent directory_:

```bash
mkdir roles
```

Lastly, set the Ansible [COLLECTION](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#envvar-ANSIBLE_COLLECTIONS_PATH) and [ROLE](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#envvar-ANSIBLE_ROLES_PATH) configurations for these two locations:

```bash
export ANSIBLE_COLLECTIONS_PATH=$(pwd)
export ANSIBLE_ROLES_PATH="$(pwd)/roles"
```

## PYTHONPATH

Make sure to include the `ANSIBLE_COLLECTIONS_PATH` variable to the `PYTHONPATH` to allow module imports.

```bash
export PYTHONPATH="${ANSIBLE_COLLECTIONS_PATH}":"${PYTHONPATH}"
```

# Linting and Commits

The `pre-commit` Python application is used to manage linting and other housekeeping functions. The application is installed as a `git` hook and as a Github workflow check.

Commits and pull requests will fail if your contributions do not pass the `pre-commit` checks.  You can check your work-in-progress code by running the following:

```bash
hatch run lint
```

Or manually:

```bash
pre-commit run -a
```

# pytest Testing

To see what tests (unit and integration) are available, run the following from the `ANSIBLE_COLLECTIONS_PATH` directory:

```bash
pushd ${ANSIBLE_COLLECTIONS_PATH};
pytest ansible_collections/cloudera/exe --collect-only;
popd;
```

You should see something like:

```
platform darwin -- Python 3.12.8, pytest-8.4.1, pluggy-1.6.0
rootdir: /Users/wmudge/Devel/collections/ansible_collections/cloudera/exe
configfile: pyproject.toml
collected 128 items
<Dir exe>
  <Dir tests>
    <Package unit>
      <Package plugins>
        <Package filter>
          <Module test_filter_combine_onto.py>
            <Function test_filter_version[source0-target0-False-expected0]>
            <Function test_filter_version[source1-target1-True-expected1]>
          <Module test_filter_version.py>
            <Function test_filter_version[1.2.3-expected0]>
            <Function test_filter_version[1.2.3 SP1-expected1]>
            <Function test_filter_version[1.2.3-SP1-expected2]>
            <Function test_filter_version[1.2.3.SP1-expected3]>
            <Function test_filter_version[1.2.3 SP1.400-expected4]>
            <Function test_filter_version[1.2.3+Build-expected5]>
            <Function test_filter_version[1.2.3+Build.400-expected6]>
        <Dir lookup>
          <Module test_lookup_supported.py>
            <Function test_lookup_supported>
        <Dir module_utils>
          <Module test_cldr_version.py>
            <Function test_parse[1.2.3-expected0]>
            <Function test_parse[1.2-None]>
            <Function test_parse[1-None]>
```

To run all of the tests:

```bash
pushd ${ANSIBLE_COLLECTIONS_PATH};
pytest ansible_collections/cloudera/exe;
popd;
```

To run a selected test, execute with a regex:

```bash
pushd ${ANSIBLE_COLLECTIONS_PATH};
pytest ansible_collections/cloudera/exe -k "test_filter_version"
popd;
```

# Molecule Testing

Running the `molecule` tests requires AWS [credentials](#aws-credentials) and [test network](#network-setup), as all tests offload the VMs to AWS.

You can either run standalone `molecule`, for roles and more advanced integration testing, or `pytest`. The latter is set up to run any and all tests, including `molecule` scenarios.

## Running standalone `molecule` tests

Running `molecule` is straightforward. First, enable the `hatch` environment:

```bash
hatch shell molecule
```

The `molecule` scenarios are located within each of the roles of the collection. To run a scenario, change to the role as your current working directory and then run `molecule`. See the [molecule documentation](https://ansible.readthedocs.io/projects/molecule/) for details.

```bash
pushd roles/cm_agent;
molecule test;
popd;
```

> [!info]
> In some cases, you might need to set your `ANSIBLE_ROLES_PATH` to the `roles` directory of this project.

Some common `molecule` commands (again, check the [molecule documentation](https://ansible.readthedocs.io/projects/molecule/) for full details):

| Command | Description |
| --- | --- |
| `molecule test` | Execute the full test lifecyle |
| `molecule create` | Create the `platforms`, i.e. the inventory, that are the target hosts of the role testing |
| `molecule prepare` | Prep the target hosts for testing the roles |
| `molecule converge` | Run the testing playbook, i.e. converge the test code, on the target hosts |
| `molecule side-effect` | Prep the target hosts, post-`converge`, for any additional setup prior to verification or idempotency testing |
| `molecule verify` | Verify the target hosts |
| `molecule cleanup` | Clean up any resources, for example, temporary files created on the controller |
| `molecule destroy` | Destroy the `platform` hosts |

You can limit testing to a `platform` within a scenario by using the `-p/--platform-name` parameter (or via the `MOLECULE_PLATFORM_NAME` environment variable):

```bash
molecule test -p rhel9.4
```

To stop tests from destroying the platforms after encountering an error (or at all, even on a successful test), pass the `--destroy=never` parameter:

```bash
molecule test -p rhel9.4 --destroy=never
```

You can log into a running platform via the `login` subcommand and the `-h/--host` parameter:

```bash
molecule login -h rhel9.4
```

As well as pass extra parameters to the underlying playbook (`converge` command only!):

```bash
molecule converge -- -vvv -t tls_config
```

## Running `molecule` via `pytest`

> [!warning]
> Not yet implemented!

We use the `ansible-pytest` plugin to run unit and integration tests for the collection.

To run a Molecule scenario on a selected platform, i.e. target host, set the platform via the environment variable:

```bash
MOLECULE_PLATFORM_NAME="rhel9.4" pytest ansible_collections/cloudera/exe -k "tktk"
```

> [!warning]
> If you run `pytest` in the root of the collection, `pytest` will copies the current collection into the required Ansible collection path structure within the working directory. That is, running `pytest` at the root of the **collection** creates a `collection/ansible_collections/<namespace>/<name>` **within** the collection.
> Thus, our recommendation is that you can run `pytest` in at the root of the **Ansible collections path**. That is, run `pytest ansible_collections/<namespace>/<name> ...` so that `pytest` doesn't have to bootstrap the collections path.

## AWS Credentials

You will need valid AWS credentials set in your environment for `molecule` to operate successfully.

In addition, make sure you have a default region declared, either in your `AWS_PROFILE` or `AWS_DEFAULT_REGION` environment variables.

## Network Setup

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

## Network Teardown

First, make sure that you have destroyed any `molecule` scenarios that are using your test infrastructure.

And then run:

```bash
hatch run molecule:teardown
```
