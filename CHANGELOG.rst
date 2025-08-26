==========================
cloudera.exe Release Notes
==========================

.. contents:: Topics

v3.0.0
======

Major Changes
-------------

- Rename nodeexporter role to node_exporter and update documentation, specs, and linting fixes (https://github.com/cloudera-labs/cloudera.exe/pull/209)
- Update Blackbox Exporter role for documentation, specs, and rename (https://github.com/cloudera-labs/cloudera.exe/pull/210)
- Update freeipa_client role (https://github.com/cloudera-labs/cloudera.exe/pull/220)
- Update freeipa_server role (https://github.com/cloudera-labs/cloudera.exe/pull/219)

Minor Changes
-------------

- Add AMD ROCm drivers installation role (https://github.com/cloudera-labs/cloudera.exe/pull/218)
- Add CM agent installation role (https://github.com/cloudera-labs/cloudera.exe/pull/227)
- Add CM repository installation role (https://github.com/cloudera-labs/cloudera.exe/pull/224)
- Add CM server installation role (https://github.com/cloudera-labs/cloudera.exe/pull/226)
- Add CSD installation role (https://github.com/cloudera-labs/cloudera.exe/pull/225)
- Add Caddy reverse proxy role (https://github.com/cloudera-labs/cloudera.exe/pull/217)
- Add Docker installation role (https://github.com/cloudera-labs/cloudera.exe/pull/215)
- Add FreeIPA DNS for ECS role (https://github.com/cloudera-labs/cloudera.exe/pull/257)
- Add FreeIPA users role (https://github.com/cloudera-labs/cloudera.exe/pull/258)
- Add Molecule testing (https://github.com/cloudera-labs/cloudera.exe/pull/197)
- Add Molecule testing (https://github.com/cloudera-labs/cloudera.exe/pull/265)
- Add PostgreSQL client installation role (https://github.com/cloudera-labs/cloudera.exe/pull/222)
- Add PostgreSQL server installation role (https://github.com/cloudera-labs/cloudera.exe/pull/221)
- Add ansible-lint, update hatch environments and pre-commit (https://github.com/cloudera-labs/cloudera.exe/pull/205)
- Add changelog (https://github.com/cloudera-labs/cloudera.exe/pull/271)
- Add cloudera service users role (https://github.com/cloudera-labs/cloudera.exe/pull/267)
- Add cloudera_manager_release parameter (https://github.com/cloudera-labs/cloudera.exe/pull/276)
- Add deprecation module for legacy roles (https://github.com/cloudera-labs/cloudera.exe/pull/229)
- Add module to query Cloudera support matrix (https://github.com/cloudera-labs/cloudera.exe/pull/246)
- Add pgAdmin installation role (https://github.com/cloudera-labs/cloudera.exe/pull/216)
- Add prerequisite roles for Cloudera on premise (private cloud) (https://github.com/cloudera-labs/cloudera.exe/pull/223)
- Add raw_filters parameter to supported lookup and module (https://github.com/cloudera-labs/cloudera.exe/pull/262)
- Add roles and example playbook for PVC cert renewal (https://github.com/cloudera-labs/cloudera.exe/pull/189)
- Add unit tests for cloudera.exe.jdk_facts (https://github.com/cloudera-labs/cloudera.exe/pull/266)
- Add variables to skip of overlap check for FreeIPA server DNS zones (https://github.com/cloudera-labs/cloudera.exe/pull/272)
- Add yamllint config (https://github.com/cloudera-labs/cloudera.exe/pull/277)
- Update API docs and fix linting issues (https://github.com/cloudera-labs/cloudera.exe/pull/268)
- Update cm_repo role to use supported lookup (https://github.com/cloudera-labs/cloudera.exe/pull/264)
- Update copyright (https://github.com/cloudera-labs/cloudera.exe/pull/270)
- Update deprecated actions (https://github.com/cloudera-labs/cloudera.exe/pull/190)
- Update grafana role for ansible-lint, consolidate tasks, and add README (https://github.com/cloudera-labs/cloudera.exe/pull/211)
- Update mount role for ansible-lint, argument specs, and README (https://github.com/cloudera-labs/cloudera.exe/pull/212)
- Update prereq_jdk role to validate Manager and Runtime versions (https://github.com/cloudera-labs/cloudera.exe/pull/260)
- Update prereq_python to use support matrix lookup (https://github.com/cloudera-labs/cloudera.exe/pull/263)
- Update support matrix plugins and role (https://github.com/cloudera-labs/cloudera.exe/pull/259)
- Update tests and filters to include Cloudera versioning scheme (https://github.com/cloudera-labs/cloudera.exe/pull/256)
- Update version_added to roles, modules, and plugins (https://github.com/cloudera-labs/cloudera.exe/pull/269)
- Update volume discovery in mount role to exclude root volume (https://github.com/cloudera-labs/cloudera.exe/pull/200)

Deprecated Features
-------------------

- Deprecate auto_repo_mirror role (https://github.com/cloudera-labs/cloudera.exe/pull/230)
- Deprecate common role (https://github.com/cloudera-labs/cloudera.exe/pull/231)
- Deprecate data role (https://github.com/cloudera-labs/cloudera.exe/pull/232)
- Deprecate dynamic_inventory role (https://github.com/cloudera-labs/cloudera.exe/pull/233)
- Deprecate freeipa_host_group role (https://github.com/cloudera-labs/cloudera.exe/pull/234)
- Deprecate info role (https://github.com/cloudera-labs/cloudera.exe/pull/235)
- Deprecate infrastructure role (https://github.com/cloudera-labs/cloudera.exe/pull/236)
- Deprecate init_deployment role (https://github.com/cloudera-labs/cloudera.exe/pull/237)
- Deprecate platform role (https://github.com/cloudera-labs/cloudera.exe/pull/238)
- Deprecate provision role (https://github.com/cloudera-labs/cloudera.exe/pull/239)
- Deprecate rdbms.client and rdbms.server roles (https://github.com/cloudera-labs/cloudera.exe/pull/240)
- Deprecate rdbms_server role (https://github.com/cloudera-labs/cloudera.exe/pull/241)
- Deprecate runtime role (https://github.com/cloudera-labs/cloudera.exe/pull/242)
- Deprecate sequence role (https://github.com/cloudera-labs/cloudera.exe/pull/243)

Bugfixes
--------

- Add JMESPath to requirements (https://github.com/cloudera-labs/cloudera.exe/pull/207)
- Replace blackbox and nodeexporter role symlinks with copy (https://github.com/cloudera-labs/cloudera.exe/pull/261)
- Update RDBMS PostgreSQL server role (https://github.com/cloudera-labs/cloudera.exe/pull/194)
- Update playbooks for ansible-lint (https://github.com/cloudera-labs/cloudera.exe/pull/213)
- Update plugins for ansible-lint (https://github.com/cloudera-labs/cloudera.exe/pull/214)
- Update prometheus role for ansible-lint, argument specs, and README (https://github.com/cloudera-labs/cloudera.exe/pull/208)
- Update support matrix lookup maps for Rocky (https://github.com/cloudera-labs/cloudera.exe/pull/273)
- Update upload-artifact to v4 (https://github.com/cloudera-labs/cloudera.exe/pull/202)
- freeipa_sidecar and freeipa_client & server fixes for el9 (https://github.com/cloudera-labs/cloudera.exe/pull/199)

New Plugins
-----------

Filter
~~~~~~

- cloudera.exe.version - Parse a Cloudera Manager version string.

Lookup
~~~~~~

- cloudera.exe.supported - Get support matrix details.

Test
~~~~

- cloudera.exe.version - compare Cloudera version strings.

New Modules
-----------

- cloudera.exe.cm_prepare_db - Configure the external Cloudera Manager server database.
- cloudera.exe.deprecation - Display a deprecation warning.
- cloudera.exe.jdk_facts - Retrieve JDK information.
- cloudera.exe.supported - Retrieve Cloudera Support Matrix information.

New Roles
---------

- cloudera.exe.blackbox_exporter - Install Blackbox Exporter.
- cloudera.exe.caddy - Install Caddy proxy packages.
- cloudera.exe.cm_agent - Install Cloudera Manager agent packages.
- cloudera.exe.cm_csd - Install Cloudera CSDs.
- cloudera.exe.cm_repo - Manage the package repository for Cloudera Manager.
- cloudera.exe.cm_server - Install Cloudera Manager server.
- cloudera.exe.docker - Install Docker.
- cloudera.exe.freeipa_server_ecs - Configure DNS zones and wildcard records for ECS.
- cloudera.exe.freeipa_server_users - Set up superusers in FreeIPA.
- cloudera.exe.node_exporter - Install Node Exporter.
- cloudera.exe.pgadmin - Install pgAdmin.
- cloudera.exe.postgresql_client - Client configuration for PostgreSQL database.
- cloudera.exe.postgresql_server - Install PostgreSQL server for Cloudera Manager.
- cloudera.exe.prereq_accumulo - Set up user accounts for Accumulo.
- cloudera.exe.prereq_activitymonitor - Set up database and user accounts for Activity Monitor.
- cloudera.exe.prereq_atlas - Set up user accounts for Atlas.
- cloudera.exe.prereq_cloudera_manager - Set up user accounts and LDAP for Kerberos for Cloudera Manager.
- cloudera.exe.prereq_cloudera_users - Set up user accounts Cloudera Manager.
- cloudera.exe.prereq_cm_database - Set up database and user accounts for Cloudera Manager.
- cloudera.exe.prereq_database - Create and manage databases and users.
- cloudera.exe.prereq_dataviz - Set up user accounts for Dataviz.
- cloudera.exe.prereq_dataviz_database - Set up database and user accounts for Dataviz.
- cloudera.exe.prereq_druid - Set up user accounts for Druid.
- cloudera.exe.prereq_ecs - Set up firewall, and networking for ECS.
- cloudera.exe.prereq_firewall - Disable firewalls for a deployment.
- cloudera.exe.prereq_flink - Set up user accounts for Flink.
- cloudera.exe.prereq_flume - Set up user accounts for Flume.
- cloudera.exe.prereq_hadoop - Set up user accounts for Hadoop.
- cloudera.exe.prereq_hbase - Set up user accounts for HBase.
- cloudera.exe.prereq_hdfs - Set up for Hdfs.
- cloudera.exe.prereq_hive - Set up user accounts for Hive.
- cloudera.exe.prereq_hive_database - Set up database and user accounts for Hive.
- cloudera.exe.prereq_httpfs - Set up user accounts for HttpFS.
- cloudera.exe.prereq_hue - Set up user accounts and Kerberos for Hue.
- cloudera.exe.prereq_hue_database - Set up database and user accounts for Hue.
- cloudera.exe.prereq_impala - Set up user accounts for Impala.
- cloudera.exe.prereq_jdk - Set up the JDK.
- cloudera.exe.prereq_kafka - Set up user accounts for Kafka.
- cloudera.exe.prereq_kerberos - Set up Kerberos for deployments.
- cloudera.exe.prereq_kernel - Update OS kernel parameters for deployments.
- cloudera.exe.prereq_keytrustee - Set up user accounts for Key Trustee.
- cloudera.exe.prereq_kms - Set up user accounts for KMS.
- cloudera.exe.prereq_knox - Set up user accounts for Knox.
- cloudera.exe.prereq_knox_database - Set up database and user accounts for Knox.
- cloudera.exe.prereq_kudu - Set up user accounts for Kudu.
- cloudera.exe.prereq_livy - Set up user accounts for Livy.
- cloudera.exe.prereq_local_account - Set up local user accounts.
- cloudera.exe.prereq_mapreduce - Set up user accounts for MapReduce.
- cloudera.exe.prereq_network_dns - Set up hostname and DNS networking.
- cloudera.exe.prereq_nifi - Set up user accounts for NiFi.
- cloudera.exe.prereq_nifiregistry - Set up user accounts for NiFi Registry.
- cloudera.exe.prereq_ntp - Set up NTP services for deployments.
- cloudera.exe.prereq_oozie - Set up user accounts for Oozie.
- cloudera.exe.prereq_oozie_database - Set up database and user accounts for Oozie.
- cloudera.exe.prereq_os - Update general OS requirements for deployments.
- cloudera.exe.prereq_phoenix - Set up user accounts for Phoenix.
- cloudera.exe.prereq_psycopg2 - Install psycopg2 for PostgreSQL for deployments.
- cloudera.exe.prereq_python - Install Python for deployments.
- cloudera.exe.prereq_query_processor_database - Set up database and user accounts for Query Processor.
- cloudera.exe.prereq_ranger - Set up user accounts for Ranger.
- cloudera.exe.prereq_ranger_database - Set up database and user accounts for Ranger.
- cloudera.exe.prereq_reportsmanager - Set up database and user accounts for Reports Manager.
- cloudera.exe.prereq_rngd - Install the Random Number Generator package for deployments.
- cloudera.exe.prereq_schemaregistry - Set up user accounts for Schema Registry.
- cloudera.exe.prereq_schemaregistry_database - Set up database and user accounts for Schema Registry.
- cloudera.exe.prereq_selinux - Manage SELinux policy enforcement for deployments.
- cloudera.exe.prereq_sentry - Set up user accounts for Sentry.
- cloudera.exe.prereq_services - Manage operating system services for deployments.
- cloudera.exe.prereq_smm - Set up user accounts and directories for Streams Messaging Manager.
- cloudera.exe.prereq_smm_database - Set up database and user accounts for Streams Messaging Manager.
- cloudera.exe.prereq_solr - Set up user accounts for Solr.
- cloudera.exe.prereq_spark - Set up user accounts for Spark.
- cloudera.exe.prereq_spark2 - Set up user accounts for Spark2.
- cloudera.exe.prereq_sqoop - Set up user accounts for Sqoop.
- cloudera.exe.prereq_ssb - Set up user accounts for SSB.
- cloudera.exe.prereq_ssb_database - Set up database and user accounts for SQL Stream Builder.
- cloudera.exe.prereq_superset - Set up user accounts for Superset.
- cloudera.exe.prereq_supported - Verify configuration against support matrix.
- cloudera.exe.prereq_thp - Disable Transparent Huge Pages for deployments.
- cloudera.exe.prereq_tls_acls - Set up local user ACLs for TLS.
- cloudera.exe.prereq_yarn - Set up user accounts for YARN.
- cloudera.exe.prereq_zeppelin - Set up user accounts for Zeppelin.
- cloudera.exe.prereq_zookeeper - Set up for Zookeeper.
- cloudera.exe.rdbms_server - Install standalone RDBMS instance.
- cloudera.exe.rocm - Provision AMD ROCm GPU drivers.
- cloudera.exe.tls_fetch_ca_certs - Bring CA root and intermediate cert back to controller.
- cloudera.exe.tls_generate_csr - Generates a CSR on each host and copies it back to the Ansible controller.
- cloudera.exe.tls_install_certs - Copy and install the signed TLS certificates to each cluster.
- cloudera.exe.tls_signing - Sign of CSRs by a CA Server.

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
