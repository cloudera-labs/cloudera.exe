==========================
cloudera.exe Release Notes
==========================

.. contents:: Topics

v2.4.1
======

Minor Changes
-------------

- Add pre-commit hooks, workflow, and instructions (https://github.com/cloudera-labs/cloudera.exe/pull/188)
- migrate rdbms role - fixes for rhel9 (https://github.com/cloudera-labs/cloudera.exe/pull/181)

Bugfixes
--------

- Update guard condition on dynamic inventory AMI lookup (https://github.com/cloudera-labs/cloudera.exe/pull/191)

v2.4.0
======

Minor Changes
-------------

- Add analytics to API documents (https://github.com/cloudera-labs/cloudera.exe/pull/183)
- Add workflow and steps to validate for and publish to Ansible Galaxy (https://github.com/cloudera-labs/cloudera.exe/pull/184)
- Update role READMEs to enable Ansible Galaxy publication (https://github.com/cloudera-labs/cloudera.exe/pull/185)
- Update to version 2.4.0 (https://github.com/cloudera-labs/cloudera.exe/pull/186)

New Roles
---------

- cloudera.exe.blackbox - Install Blackbox Exporter.
- cloudera.exe.grafana - Set up Grafana server.
- cloudera.exe.nodeexporter - Install Node Exporter.
- cloudera.exe.prometheus - Install Prometheus.

v2.3.1
======

Minor Changes
-------------

- Add Blackbox Role (https://github.com/cloudera-labs/cloudera.exe/pull/178)
- Add Monitoring roles (https://github.com/cloudera-labs/cloudera.exe/pull/174)
- Add minor changes to Monitoring Roles (https://github.com/cloudera-labs/cloudera.exe/pull/177)
- Adds RHEL9 support for free_ipaserver & free_ipaclient (https://github.com/cloudera-labs/cloudera.exe/pull/176)
- Don't run GPC VPC discovery tasks when the subnet was already specified. (https://github.com/cloudera-labs/cloudera.exe/pull/149)

v2.3.0
======

Minor Changes
-------------

- Allow skipping GCP availability zones validation. (https://github.com/cloudera-labs/cloudera.exe/pull/150)
- GCP: Add support for specifying the backups storage bucket. (https://github.com/cloudera-labs/cloudera.exe/pull/172)
- Move listing cross account keys to teardown playbook. (https://github.com/cloudera-labs/cloudera.exe/pull/147)
- Update AWS SG rules to use Prefix List for extra CIDR block access (https://github.com/cloudera-labs/cloudera.exe/pull/168)
- Variables that are set in roles/runtime/tasks/initialize_setup_gcp.yml are never used. (https://github.com/cloudera-labs/cloudera.exe/pull/148)

Bugfixes
--------

- Remove duplicate namespace entry in freeipa_server role (https://github.com/cloudera-labs/cloudera.exe/pull/170)

v2.2.0
======

Minor Changes
-------------

- Add PostgreSQL Connector install to pvc_base_prereqs_ext Playbook (https://github.com/cloudera-labs/cloudera.exe/pull/167)

v2.1.0
======

Bugfixes
--------

- Remove PVC Base teardown environment vars  (https://github.com/cloudera-labs/cloudera.exe/pull/165)

v2.0.1
======

Minor Changes
-------------

- Add PvC infra provision role (https://github.com/cloudera-labs/cloudera.exe/pull/159)
- Add storage volume mount role (https://github.com/cloudera-labs/cloudera.exe/pull/160)

Bugfixes
--------

- Fixes for FreeIPA client and server roles (https://github.com/cloudera-labs/cloudera.exe/pull/158)
- Update pip requirements for the latest 2.12.* point releases (https://github.com/cloudera-labs/cloudera.exe/pull/162)

New Roles
---------

- cloudera.exe.mount - Create and mount a storage volume.
- cloudera.exe.provision - Provision.

v2.0.0
======

Minor Changes
-------------

- Add Ansible documentation generation resources and workflows (https://github.com/cloudera-labs/cloudera.exe/pull/151)
- Add GCP region zones to CDP Env creation (https://github.com/cloudera-labs/cloudera.exe/pull/143)
- Add cloudera-deploy playbooks (https://github.com/cloudera-labs/cloudera.exe/pull/146)
- Add freeipa roles for PvC pre_setup RHEL only (https://github.com/cloudera-labs/cloudera.exe/pull/144)
- Update release/v2.0.0 (#153) (https://github.com/cloudera-labs/cloudera.exe/pull/155)
- Update release/v2.0.0 (https://github.com/cloudera-labs/cloudera.exe/pull/153)

Bugfixes
--------

- Remove "virtual" collection dependencies (https://github.com/cloudera-labs/cloudera.exe/pull/156)
- Update check for MSI consistency (https://github.com/cloudera-labs/cloudera.exe/pull/145)

New Roles
---------

- cloudera.exe.auto_repo_mirror - Repository preseed.
- cloudera.exe.dynamic_inventory - Dynamic inventory.
- cloudera.exe.freeipa_client - Set up FreeIPA client.
- cloudera.exe.freeipa_server - Set up FreeIPA server.
- cloudera.exe.init_deployment - Configuration init.

v1.7.5
======

Minor Changes
-------------

- Added subnet filters to the df_service module. (https://github.com/cloudera-labs/cloudera.exe/pull/118)
- RAZ Implementation for Azure (https://github.com/cloudera-labs/cloudera.exe/pull/111)
- Rebase of devel-pvc-update onto devel (https://github.com/cloudera-labs/cloudera.exe/pull/141)

Bugfixes
--------

- Fix unset variable in runtime deployment for DW VW config (https://github.com/cloudera-labs/cloudera.exe/pull/136)
- Fixing regression due to recent changes to DataFlow runtime. (https://github.com/cloudera-labs/cloudera.exe/pull/137)

v1.7.4
======

Bugfixes
--------

- Update bindep installation and operations (https://github.com/cloudera-labs/cloudera.exe/pull/140)

v1.7.3
======

Minor Changes
-------------

- Add support to choosing the GCP subnet to deploy to. (https://github.com/cloudera-labs/cloudera.exe/pull/132)
- PR validation workflows and ansible-builder support (https://github.com/cloudera-labs/cloudera.exe/pull/139)

v1.7.2
======

Minor Changes
-------------

- Add import of DF Custom Flows to runtime role (https://github.com/cloudera-labs/cloudera.exe/pull/116)
- Allow skipping of GCP Service and IAM management (https://github.com/cloudera-labs/cloudera.exe/pull/130)
- CDW Round 47 (https://github.com/cloudera-labs/cloudera.exe/pull/102)
- Fixes for RHEL8.6 support and Dynamic Inventory (https://github.com/cloudera-labs/cloudera.exe/pull/127)
- Improve GCP APIs Services check and Enable (https://github.com/cloudera-labs/cloudera.exe/pull/129)
- Refactor Terraform into pure-TF resource files and Jinja tfvars (https://github.com/cloudera-labs/cloudera.exe/pull/125)
- Update GCP for L2 networking deployment (https://github.com/cloudera-labs/cloudera.exe/pull/115)
- Update collection version to 2.0.0-alpha1 (https://github.com/cloudera-labs/cloudera.exe/pull/121)
- WIP PvC Prereqs and Control Plane merge (https://github.com/cloudera-labs/cloudera.exe/pull/119)

Bugfixes
--------

- Fix Azure deployment (https://github.com/cloudera-labs/cloudera.exe/pull/128)
- Fix git branch in collection dependency (https://github.com/cloudera-labs/cloudera.exe/pull/123)
- Hotfix- Update CentOS 7 AMI search terms (https://github.com/cloudera-labs/cloudera.exe/pull/133)
- Update collection dependency for PVC development (https://github.com/cloudera-labs/cloudera.exe/pull/122)

v1.7.1
======

Bugfixes
--------

- Change lookup search for Azure Service Principal Object ID (https://github.com/cloudera-labs/cloudera.exe/pull/120)

v1.7.0
======

Minor Changes
-------------

- Initial commit for ansible-test support (https://github.com/cloudera-labs/cloudera.exe/pull/63)
- RAZ impl in exe (https://github.com/cloudera-labs/cloudera.exe/pull/107)
- Remove calls to the unsupported cloudera.cloud.env_auth (https://github.com/cloudera-labs/cloudera.exe/pull/117)

v1.6.2
======

Bugfixes
--------

- Fix MSI teardown to delete MSIs (https://github.com/cloudera-labs/cloudera.exe/pull/108)
- Support configurable AWS ARN partition for policies (https://github.com/cloudera-labs/cloudera.exe/pull/113)

v1.6.1
======

Bugfixes
--------

- Update parameters for EC2 module (https://github.com/cloudera-labs/cloudera.exe/pull/110)

v1.6.0
======

Minor Changes
-------------

- Add Terraform deployment engine for cloud resources (https://github.com/cloudera-labs/cloudera.exe/pull/56)
- Azure AuthZ/Single Resource Group Work - EXE (https://github.com/cloudera-labs/cloudera.exe/pull/68)
- Convert terraform related global variables to a dictionary (https://github.com/cloudera-labs/cloudera.exe/pull/100)
- Map common__azure_sp_login_env to infra (https://github.com/cloudera-labs/cloudera.exe/pull/101)
- Pin collection dependencies to single versions (https://github.com/cloudera-labs/cloudera.exe/pull/98)
- Support AWSCLI v2 (https://github.com/cloudera-labs/cloudera.exe/pull/81)
- Support for DataFlow Deployments (https://github.com/cloudera-labs/cloudera.exe/pull/82)
- Support the use of other CDP control planes (https://github.com/cloudera-labs/cloudera.exe/pull/91)
- Update Azure MSI and role assignment handling (https://github.com/cloudera-labs/cloudera.exe/pull/80)
- Update config docs (https://github.com/cloudera-labs/cloudera.exe/pull/96)
- fix ec2 dynamic inventory and el8 deployment (https://github.com/cloudera-labs/cloudera.exe/pull/94)

Bugfixes
--------

- Fix AWS ELB teardown (https://github.com/cloudera-labs/cloudera.exe/pull/97)
- Fix default Azure Netapp volume size (https://github.com/cloudera-labs/cloudera.exe/pull/79)
- Fix dynamic inventory public IP check (https://github.com/cloudera-labs/cloudera.exe/pull/99)
- Fix failed_when condition for GCP Service Accounts Policies (https://github.com/cloudera-labs/cloudera.exe/pull/106)
- Hotfix for Issue #83 (https://github.com/cloudera-labs/cloudera.exe/pull/84)
- Rearrange teardown tasks for GCP (https://github.com/cloudera-labs/cloudera.exe/pull/93)
- Update Azure NetApp management and add NFS protocol version (https://github.com/cloudera-labs/cloudera.exe/pull/86)
- Use infra__security_group_vpce_name as variable for VPC Endpoint SG (https://github.com/cloudera-labs/cloudera.exe/pull/104)

v1.5.2
======

Bugfixes
--------

- Fix bug with __infra_aws_storage_tags_list (https://github.com/cloudera-labs/cloudera.exe/pull/74)
- Fix invalid subnet variables for CDW creation (https://github.com/cloudera-labs/cloudera.exe/pull/77)
- region statement missing from modify-vpc-endpoint awscli call (https://github.com/cloudera-labs/cloudera.exe/pull/75)

v1.5.1
======

Bugfixes
--------

- Fix reference to undefined storage tags variable (https://github.com/cloudera-labs/cloudera.exe/pull/73)

v1.5.0
======

Minor Changes
-------------

- AWS VPC Endpoint Support (https://github.com/cloudera-labs/cloudera.exe/pull/54)
- Add GCP support to FreeIPA host group role (https://github.com/cloudera-labs/cloudera.exe/pull/61)
- Add Ubuntu 20.04 focal fossa as optional OS for dynamic inventory (https://github.com/cloudera-labs/cloudera.exe/pull/69)
- Add network discovery and assignment functions (https://github.com/cloudera-labs/cloudera.exe/pull/62)
- Add role, policy, and storage tagging to AWS (https://github.com/cloudera-labs/cloudera.exe/pull/55)
- Add selectable distribution support for cloudera.cluster (https://github.com/cloudera-labs/cloudera.exe/pull/51)
- Add support for CDE (https://github.com/cloudera-labs/cloudera.exe/pull/58)
- Add support for CDE (part 2 - virtual clusters) (https://github.com/cloudera-labs/cloudera.exe/pull/60)
- Allow optional deletion of GCP Custom roles during teardown (https://github.com/cloudera-labs/cloudera.exe/pull/44)
- Extensible tagging for Cloudera Experiences (https://github.com/cloudera-labs/cloudera.exe/pull/48)
- Molecule test harness for platform role (https://github.com/cloudera-labs/cloudera.exe/pull/59)
- Move DFX Beta implementation to GA process (https://github.com/cloudera-labs/cloudera.exe/pull/47)
- Update streams messaging default template (https://github.com/cloudera-labs/cloudera.exe/pull/65)

Bugfixes
--------

- Add guard conditionals for CDE setup (https://github.com/cloudera-labs/cloudera.exe/pull/66)
- Add missing CDF configurations (https://github.com/cloudera-labs/cloudera.exe/pull/64)
- Fix AWS network discovery (https://github.com/cloudera-labs/cloudera.exe/pull/72)

v1.4.2
======

v1.4.1
======

Minor Changes
-------------

- Enhancement to sudoers role to add groups and work with user sync (https://github.com/cloudera-labs/cloudera.exe/pull/50)

Bugfixes
--------

- Fix AWS network creation error when no tags are defined (https://github.com/cloudera-labs/cloudera.exe/pull/46)

v1.4.0
======

Minor Changes
-------------

- AWS Level 2 networking (including shared resources) (https://github.com/cloudera-labs/cloudera.exe/pull/32)
- Add Centos8 to Dynamic Inventory options (https://github.com/cloudera-labs/cloudera.exe/pull/25)
- Changes for DF-beta (https://github.com/cloudera-labs/cloudera.exe/pull/20)
- Ciao dynamo (https://github.com/cloudera-labs/cloudera.exe/pull/33)
- Improve Azure deployment stability (https://github.com/cloudera-labs/cloudera.exe/pull/34)
- Improve GCP teardown idempotence (https://github.com/cloudera-labs/cloudera.exe/pull/39)
- Improve network security port determination logic (https://github.com/cloudera-labs/cloudera.exe/pull/29)
- Improve purge functionality with further edge cases (https://github.com/cloudera-labs/cloudera.exe/pull/35)
- Improve teardown and support purge mode, other minor fixes (https://github.com/cloudera-labs/cloudera.exe/pull/24)
- Remove initialize tasks in sudoers role (https://github.com/cloudera-labs/cloudera.exe/pull/42)
- Support Private Networks (https://github.com/cloudera-labs/cloudera.exe/pull/15)
- Update Azure Teardown - Currently broken (https://github.com/cloudera-labs/cloudera.exe/pull/18)
- Update ML Workspace setup to use definition of a single instance group (https://github.com/cloudera-labs/cloudera.exe/pull/40)
- Update env setup to include passing freeipa instance count. Add some … (https://github.com/cloudera-labs/cloudera.exe/pull/38)

Bugfixes
--------

- Correct references to AWS policy documents (https://github.com/cloudera-labs/cloudera.exe/pull/30)
- Correcting Idbroker Role policy definitions for AWS (https://github.com/cloudera-labs/cloudera.exe/pull/41)
- Fix L1 networking teardown when purge is used (https://github.com/cloudera-labs/cloudera.exe/pull/43)
- Fix default opdb teardown (https://github.com/cloudera-labs/cloudera.exe/pull/22)
- Fix unused DWX variable and more accurate datahub definition filters (https://github.com/cloudera-labs/cloudera.exe/pull/19)

v1.3.1
======

v1.3.0
======

Minor Changes
-------------

- Add support for DFX Tech Preview (https://github.com/cloudera-labs/cloudera.exe/pull/12)

Bugfixes
--------

- Reopening PR after revert on Cloudera Labs (https://github.com/cloudera-labs/cloudera.exe/pull/16)

v1.2.1
======

v1.2.0
======

Minor Changes
-------------

- Add tasks for retrieving datahub definitions and filtering by datalak… (https://github.com/cloudera-labs/cloudera.exe/pull/9)
- Improve Azure Storage Account name check to be more informative (https://github.com/cloudera-labs/cloudera.exe/pull/13)
- New Roles to facilitate creation of FreeIPA sudoers group and rule  (https://github.com/cloudera-labs/cloudera.exe/pull/6)
- Remove extraneous user_ports from Extra security group (https://github.com/cloudera-labs/cloudera.exe/pull/14)

New Roles
---------

- cloudera.exe.freeipa_host_group - FreeIPA host inventory.
- cloudera.exe.sudoers - Sudoers.

v1.1.2
======

v1.1.1
======

v1.1.0
======

v1.0.0
======

New Plugins
-----------

Filter
~~~~~~

- cloudera.exe.combine_onto - Combine two dictionaries.

New Roles
---------

- cloudera.exe.common - Common configuration.
- cloudera.exe.data - Data.
- cloudera.exe.info - Info.
- cloudera.exe.infrastructure - Infrastructure.
- cloudera.exe.platform - Platform.
- cloudera.exe.runtime - Runtime.
- cloudera.exe.sequence - Sequence.
