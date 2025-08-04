# rocm

Provision AMD ROCm

This role installs and configures a host for AMD ROCm GPU packages and drivers. It sets up the necessary repositories (including specific ones for Red Hat distributions), installs core ROCm components, AMD GPU drivers, and optional Python packages required for GPU computing. The role ensures the system is ready to utilize AMD GPUs for compute-intensive tasks. See [AMD ROCm and GPU packages](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/package-manager-index.html) for details.

The role will:
- Add and configure the AMD ROCm and AMD GPU driver repositories for the target operating system (with specific options for Red Hat).
- Install core AMD ROCm packages and components.
- Install AMD GPU drivers.
- Optionally install additional Python packages required for ROCm development or specific applications.
- Ensure necessary kernel modules are loaded and system configurations are applied for optimal GPU operation, e.g. configure the shared objects, `LD_LIBRARY_PATH`, and `PATH` for the ROCm libraries.

To test if the AMD GPU kernel drivers are able to load, log into the host and run:

```bash
modprobe amdgpu
```

If this is successful, check to see if the `amdgpu` driver is not set to load automatically:

```bash
sudo grep -r "blacklist amdgpu" /etc/modprobe.d/ /usr/lib/modprobe.d/
sudo grep -r "install amdgpu /bin/false" /etc/modprobe.d/ /usr/lib/modprobe.d/
```

If present, update and reboot. For example:

```bash
sudo vi /usr/lib/modprobe.d/blacklist-amdgpu.conf
sudo reboot
```

For further details, try the following:

```bash
lsmod | grep amdgpu
sudo journalctl -b | grep -i "amdgpu"
rocm-smi
rocminfo
```

# Requirements

- An AMD GPU compatible with the specified ROCm and AMD GPU driver versions must be present on the target host.
- Compatible Linux distribution (e.g., Red Hat Enterprise Linux/CentOS Stream, Ubuntu). Specific repository parameters in this role primarily target Red Hat-based systems.
- Internet access from the target host to download packages and repository keys.
- Root or `sudo` privileges are required to manage package repositories, install packages, and configure system drivers.

# Dependencies

None.

# Parameters

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `rocm_version` | `str` | `False` | `6.4.1` | Version of the AMD ROCm package to install. |
| `amdgpu_version` | `str` | `False` | `6.4.1` | Version of the AMD GPU drivers to install. |
| `rocm_crb_repo_name` | `str` | `False` | | **(Red Hat Specific)** Name of the CodeReady Builder (CRB) repository to enable. |
| `rocm_epel_rpm` | `str` | `False` | | **(Red Hat Specific)** URL or path to the EPEL RPM package to install, often a prerequisite for ROCm dependencies. |
| `rocm_python_packages` | `list` of `str` | `False` | `[]` | List of system Python packages to install, which might be required for ROCm tools or libraries (e.g., `roc-toolkit`, `hip-rocblas`). |
| `rocm_repo_name` | `str` | `False` | | **(Red Hat Specific)** Name (identifier) of the AMD ROCm repository to configure. |
| `rocm_repo_baseurl` | `str` | `False` | | **(Red Hat Specific)** Base URL of the AMD ROCm repository. |
| `rocm_repo_gpgkey` | `str` | `False` | | **(Red Hat Specific)** URL of the AMD ROCm repository GPG key for package signature verification. |
| `amdgpu_repo_name` | `str` | `False` | | **(Red Hat Specific)** Name (identifier) of the AMD GPU driver repository to configure. |
| `amdgpu_repo_baseurl` | `str` | `False` | | **(Red Hat Specific)** Base URL of the AMD GPU driver repository. |
| `amdgpu_repo_gpgkey` | `str` | `False` | | **(Red Hat Specific)** URL of the AMD GPU driver repository GPG key for package signature verification. |

# Example Playbook

```yaml
- hosts: gpu_nodes
  tasks:
    - name: Provision AMD ROCm with default versions
      ansible.builtin.import_role:
        name: cloudera.exe.rocm
      # Uses rocm_version: 6.4.1 and amdgpu_version: 6.4.1 by default.

    - name: Provision AMD ROCm with custom versions and Python packages (Red Hat)
      ansible.builtin.import_role:
        name: cloudera.exe.rocm
      vars:
        rocm_version: "6.0"
        amdgpu_version: "6.0"
        rocm_crb_repo_name: "codeready-builder-for-rhel-8-x86_64-rpms" # Example CRB repo
        rocm_epel_rpm: "https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm"
        rocm_python_packages:
          - "pytorch" # Example Python package that might depend on ROCm
          - "tensorflow-rocm"
        rocm_repo_name: "rocm"
        rocm_repo_baseurl: "https://repo.radeon.com/rocm/rhel8/6.0/main"
        rocm_repo_gpgkey: "https://repo.radeon.com/rocm/rocm.gpg.key"
        amdgpu_repo_name: "amdgpu"
        amdgpu_repo_baseurl: "https://repo.radeon.com/amdgpu/latest/rhel8"
        amdgpu_repo_gpgkey: "https://repo.radeon.com/amdgpu/amdgpu.gpgkey"
```

# License

```
Copyright 2025 Cloudera, Inc.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
```
