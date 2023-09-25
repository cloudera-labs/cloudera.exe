# Testing cloudera.exe

The collection uses `ansible-test` for unit and integration testing.

```bash
# Sanity tests
ansible-test sanity --docker --python 3.9

# Unit tests
ansible-test units --docker --python 3.9

# Integration tests
ansible-test integration --docker
```

To run the _integration_ tests, you first need to have a running virtual environment configured with Ansible (`core`) and the required collections. When you run `ansible-test`, the program will bootstrap the [requirements|tests/integration/requirements.txt] in the Docker container and mount the `ANSIBLE_COLLECTION_PATHS`.

```bash
# In your favorite VENV...
pip3 install ansible-core
ansible-galaxy collection install -p collections -r galaxy.yml
export ANSIBLE_COLLECTION_PATHS="$(pwd)/collections"
```

You also need to provide AWS credentials and test configuration in the `integration_config.yml` file. This file is *not* included in the project, as it will contain sensitive data, but there is a template -- `integration_config.yml.template` -- that you can copy and update as needed.
