#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2025 Cloudera, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

DOCUMENTATION = r"""
module: supported
short_description: Retrieve Cloudera Support Matrix information
description:
  - Retrieve product compatibility and support information from the Cloudera Support Matrix API.
  - Supports filtering by Cloudera Runtime, Manager or Data Service product versions.
  - Returns comprehensive support matrix data including compatibility information across different Cloudera products.
author:
  - "Jim Enright (@jimright)"
version_added: "3.0.0"
options:
  cloudera_manager:
    description:
      - Filter by specific Cloudera Manager version.
      - Mutually exclusive with the O(cloudera_runtime) and O(cloudera_data_services) parameters.
    type: str
    required: false
  cloudera_runtime:
    description:
      - Filter by specific CDP Private Cloud Base (Cloudera Runtime) version.
      - Mutually exclusive with the O(cloudera_manager) and O(cloudera_data_services) parameters.
    type: str
    required: false
  cloudera_data_services:
    description:
      - Filter by specific CDP Private Cloud Data Services version.
      - Mutually exclusive with the O(cloudera_manager) and O(cloudera_runtime) parameters.
    type: str
    required: false
  timeout:
    description:
      - HTTP request timeout in seconds.
    type: int
    default: 30
notes:
  - Only one of the O(cloudera_manager), O(cloudera_runtime) or O(cloudera_data_services) parameters can be specified.
"""

EXAMPLES = r"""
- name: Get all support matrix information
  cloudera.exe.supported:
  register: full_matrix

- name: Get support matrix for Cloudera Manager version
  cloudera.exe.supported:
    cloudera_manager: "7.13.1"
  register: cm_support

- name: Get support matrix for Cloudera Runtime version
  cloudera.exe.supported:
    cloudera_runtime: "7.1.9 SP1"
  register: base_support

- name: Get support matrix for Cloudera Data Services version
  cloudera.exe.supported:
    cloudera_data_services: "1.5.4"
  register: ds_support
"""

RETURN = r"""
support_matrix_data:
    description: Complete support matrix information from Cloudera
    type: dict
    returned: always
    contains:
        browsers:
            description: Browser support information
            type: list
            elements: dict
            returned: when supported
        databases:
            description: Database compatibility information
            type: list
            elements: dict
            returned: when supported
            contains:
                description:
                    description: Description of the database
                    type: str
                    returned: always
                family:
                    description: Database family identifier
                    type: str
                    returned: always
                id:
                    description: Support matrix ID for the entry
                    type: int
                    returned: always
                version:
                    description: Version of the database
                    type: str
                    returned: always
            sample: [
                {
                    "version": "13",
                    "family": "PostgreSQL",
                    "description": "PostgreSQL-13",
                    "id": 801
                }
            ]
        jdks:
            description: JDK compatibility information
            type: list
            elements: dict
            returned: when supported
            contains:
                description:
                    description: Description of the JDK
                    type: str
                    returned: always
                family:
                    description: JDK family identifier
                    type: str
                    returned: always
                id:
                    description: Support matrix ID for the entry
                    type: int
                    returned: always
                version:
                    description: Version of the JDK
                    type: str
                    returned: always
            sample: [
                {
                    "version": "JDK11",
                    "family": "OpenJDK",
                    "description": "OpenJDK-JDK11",
                    "id": 797
                }
            ]
        products:
            description: Cloudera product information
            type: list
            elements: dict
            returned: when supported
            contains:
                description:
                    description: Description of the product
                    type: str
                    returned: always
                group:
                    description: Group identifier
                    type: str
                    returned: always
                id:
                    description: Support matrix ID for the entry
                    type: int
                    returned: always
                org:
                    description: Support matrix organization
                    type: str
                    returned: always
                product_name:
                    description: Full product name
                    type: str
                    returned: always
                release_date:
                    description: Release date of the product (DD-MM-YYY)
                    type: str
                    returned: when supported
                version:
                    description: Version of the product
                    type: str
                    returned: always
            sample: [
                {
                    "version": "7.13.1",
                    "productName": "Cloudera Manager",
                    "description": "Cloudera Manager-7.13.1",
                    "id": 1325,
                    "group": "7.13"
                }
            ]
        kubernetes:
            description: Kubernetes platform compatibility
            type: list
            returned: always
        processor:
            description: Processor architecture compatibility
            type: list
            elements: dict
            returned: when supported
            contains:
                description:
                    description: Description of the architecture
                    type: str
                    returned: always
                family:
                    description: Architecture family identifier
                    type: str
                    returned: always
                id:
                    description: Support matrix ID for the entry
                    type: int
                    returned: always
                name:
                    description: Name of the architecture
                    type: int
                    returned: always
                version:
                    description: Version of the architecture
                    type: str
                    returned: always
        operating_systems:
            description: Operating system compatibility
            type: list
            elements: dict
            returned: when supported
            contains:
                description:
                    description: Description of the OS
                    type: str
                    returned: always
                family:
                    description: OS family identifier
                    type: str
                    returned: always
                group:
                    description: Group identifier
                    type: str
                    returned: always
                id:
                    description: Support matrix ID for the entry
                    type: int
                    returned: always
                version:
                    description: Version of the OS
                    type: str
                    returned: always
            sample: [
                {
                    "version": "9.4",
                    "family": "Rocky Linux",
                    "description": "Rocky Linux-9.4",
                    "id": 1087,
                    "group": "9"
                }
            ]
filters:
    description: Summary of filters that were applied to the API request
    type: dict
    returned: always
    contains:
        _product full name_:
            description: Full name and version of the supplied product
            type: str
            returned: when filter applied
"""

import json

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.common.dict_transformations import _camel_to_snake
from ansible.module_utils.urls import fetch_url, to_text

from ansible_collections.cloudera.exe.plugins.module_utils.cldr_supported import (
    PRODUCT_NAME_MAPPING,
    parse_support_entries,
    support_matrix_url,
)


class ClouderaSupportMatrix:
    """
    Class to handle Cloudera Support Matrix API interactions.

    This class manages the construction of API requests, filtering parameters,
    and processing of responses from the Cloudera Support Matrix API.
    """

    def __init__(self, module):
        """
        Initialize the ClouderaSupportMatrix class.

        Args:
            module: AnsibleModule instance
        """
        self.module = module

        # Extract product version parameters
        self.product_versions = {}
        for param_name in PRODUCT_NAME_MAPPING.keys():
            version = module.params.get(param_name)
            if version:
                self.product_versions[param_name] = version

        self.timeout = module.params.get("timeout", 30)

        # Initialize return values
        self.support_matrix_data = {}
        self.filters = {}

        # Execute the logic
        self.process()

    def process(self):
        """
        Fetch support matrix data from the Cloudera API using Ansible's fetch_url.
        """

        try:
            # Build the API URL
            api_url, self.filters = support_matrix_url(self.product_versions)

            # Prepare headers
            headers = {
                "Accept": "*/*",
                "Content-Type": "application/json",
                "User-Agent": "Ansible/cloudera.cluster",
            }

            # Use Ansible's fetch_url
            response, info = fetch_url(
                self.module,
                api_url,
                headers=headers,
                timeout=self.timeout,
            )

            if info.get("status") == 302:
                self.module.fail_json(
                    msg=f"Product(s) not found: {', '.join(f"{key}-{value}" for key, value in self.filters.items())}",
                )
            elif info.get("status") != 200:
                self.module.fail_json(
                    msg=f"HTTP error occurred: {info.get('msg', 'Unknown error')}",
                    url=api_url,
                    status=info.get("status"),
                    reason=info.get("msg"),
                )

            if response:
                response_text = to_text(response.read())
            else:
                self.module.fail_json(
                    msg="Empty response received from API",
                    api_url=api_url,
                )

            # Parse JSON response
            try:
                matrix = json.loads(response_text)
                for k, v in matrix.items():
                    self.support_matrix_data[_camel_to_snake(k)] = (
                        parse_support_entries(v)
                    )
            except json.JSONDecodeError as e:
                self.module.fail_json(
                    msg=f"Failed to parse JSON response: {to_native(e)}",
                    api_url=api_url,
                    response_text=response_text,
                )

        except Exception as e:
            self.module.fail_json(
                msg=f"Unexpected error occurred: {to_native(e)}",
                api_url=api_url,
            )


def main():
    """
    Main function to execute the Ansible module.
    """

    # Define module arguments
    module = AnsibleModule(
        argument_spec=dict(
            cloudera_manager=dict(type="str", required=False),
            cloudera_runtime=dict(type="str", required=False),
            cloudera_data_services=dict(type="str", required=False),
            timeout=dict(type="int", default=30),
        ),
        mutually_exclusive=[
            (
                "cloudera_manager",
                "cloudera_runtime",
                "cloudera_data_services",
            ),
        ],
    )

    # Create and Fetch support matrix
    result = ClouderaSupportMatrix(module)

    # Prepare successful response
    output = dict(
        changed=False,
        support_matrix_data=result.support_matrix_data,
        filters=result.filters,
    )

    module.exit_json(**output)


if __name__ == "__main__":
    main()
