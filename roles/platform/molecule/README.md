# Molecule Testing

Each Molecule scenario represents a networking scheme, e.g. Level0. The default
scheme is Level1, the public/private configuration.

## Dependencies

```bash
pip install "molecule[lint]==3.4"
```

Molecule is configured to execute against `localhost` rather than against a
provisioned `platform`. You will need to ensure that all dependencies are
installed, except for the Ansible collections and roles, which will be gathered
during the `dependency` stage.

NOTE: Molecule `3.5` has a bug that prevents the use of collections, so be sure
to pin to `3.4` until this bug is fixed upstream.

## Execution

From within the `platform` role, execute:

* `molecule prepare` to set up the Terraform cloud provider assets
* `molecule converge` to run the `cloudera.exe.platform` role against these assets
* `molecule cleanup` to tear down the `platform` role and Terraform assets
* or `molecule test` to run the full lifecycle

You can also use `reset` to remove all of the dependencies, e.g. collections, 
from the Molecule cache, in order to start fresh.

NOTE: To run other scenarios, i.e. Level0 networking, use the `-s` flag:
`module test -s level0`.
