# Molecule Testing

Each Molecule scenario represents a networking scheme, e.g. Level0. The default
scheme is Level1, the public/private configuration.

## Dependencies

```bash
pip install "molecule[lint]==3.4"
```

Molecule is configured to execute against `localhost` rather than against a
provisioned `platform`. You will need to ensure that all Python and OS
dependencies are installed, except for the Ansible collections and roles, which
will be gathered during the `dependency` stage.

In short, set up a `cldr-runner` runtime environment without the Ansible
collections and roles.

NOTE: Molecule `3.5` has a bug that prevents the use of collections, so be sure
to pin to `3.4` until this bug is fixed upstream.

## Execution

From within the `platform` role, execute:

* `molecule prepare` to set up the Terraform cloud provider assets
* `molecule converge` to run the `cloudera.exe.platform` role against these
assets
* `molecule cleanup` to tear down the `platform` role and Terraform assets
* or `molecule test` to run the full lifecycle

You can also use `reset` to remove all of the dependencies, e.g. collections,
from the Molecule cache, in order to start fresh.

NOTE: To run other scenarios, i.e. Level0 networking, use the `-s` flag:
`module test -s level0`.

## Configuration

The `molecule.yml` configuration file can accept the following environment
variables:

- `FOUNDRY_NAME_PREFIX`, the "primary key" for the CDP deployment. Defaults to
scenario-specific values.
- `FOUNDRY_INFRA_TYPE`, targeted cloud provider. Defaults to `aws`.
- `FOUNDRY_AWS_REGION`, the AWS region for deployment. Defaults to `us-east-2`.

## SSH Access

The Molecule scenarios create a temporary SSH key for each `prepare`-d run. The
private key is saved to the ephemeral `deployment` directory within the scenerio
parent directory. The SSH key is deleted from the cloud provider during
`cleanup`.

## Terraform

The Molecule scenarios each create a Terraform state directory -- the
`deployment` directory within the scenario parent directory.
