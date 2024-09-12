# Testing cloudera.exe

The collection is migrating from `ansible-test` to `pytest` and `molecule` for unit and integration testing. In addition, we use `pre-commit` to handle linting and formatting both for `git` commits and for various Github Action workflows in the repository.

## Setup

Typically, you will want to set up a development `virtualenv`, install `ansible-core~=2.16.0`, and then load the development Python requirements from the `requirements-dev.txt` file in the project root.

```bash
pip install ansible-core~=2.16.0
pip install -r requirements-dev.txt
```

Running the `molecule` tests requires `podman` as the container engine, so you will need to install that service on your test machine.

## Testing

You can either run standalone `molecule`, for roles and more advanced integration testing, or `pytest`. The latter is set up to run any and all tests, including `molecule` scenarios.

### Running standalone `molecule` tests

Currently, `molecule` scenarios are located in the `extensions/molecule` directory. To run a scenario, execute `cd extensions` and then run `molecule`. For example:

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

To see what tests (unit and integration) are available, run the following from the root of the collection:

```bash
pytest --collect-only
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
pytest -k "postgresql_14_tls"
```

To run a Molecule scenario on a selected platform, i.e. target host, set the platform via the environment variable:

```bash
MOLECULE_PLATFORM_NAME="rhel9.4" pytest -k "postgresql_14_tls"
```

> [!warning]
> The above execution copies the current collection into the required Ansible collection path structure within the working directory. That is, running `pytest` at the root of the **collection** creates a `collection/ansible_collections/<namespace>/<name>` **within** the collection.
> To get around this, you can run `pytest` in at the root of the **Ansible collections path**. That is, run `pytest ansible_collections/<namespace>/<name> ...` so that `pytest` doesn't have to bootstrap the collections path.

## Linting and Commits

The `pre-commit` Python application is used to manage linting and other housekeeping functions. The application is installed as a `git` hook and as a Github workflow check.

Commits and pull requests will fail if your contributions do not pass the `pre-commit` checks.  You can check your work-in-progress code by running the following:

```bash
pre-commit run -a
```
