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
  - Supports filtering by Cloudera Runtime, Manager and Data Service product versions.
  - Returns comprehensive support matrix data including compatibility information across different Cloudera products.
author:
  - "Jim Enright (@jimright)"
version_added: "3.0.0"
options:
  cloudera_manager_version:
    description:
      - Filter by specific Cloudera Manager version.
      - Mutually exclusive with the O(cloudera_runtime_version) and O(cloudera_data_services_version) parameters.
    type: str
    required: false
  cloudera_runtime_version:
    description:
      - Filter by specific CDP Private Cloud Base (Cloudera Runtime) version.
      - Mutually exclusive with the O(cloudera_manager_version) and O(cloudera_data_services_version) parameters.
    type: str
    required: false
  cloudera_data_services_version:
    description:
      - Filter by specific CDP Private Cloud Data Services version.
      - Mutually exclusive with the O(cloudera_manager_version) and O(cloudera_runtime_version) parameters.
    type: str
    required: false
  timeout:
    description:
      - HTTP request timeout in seconds.
    type: int
    default: 30
notes:
  - Only one of the O(cloudera_manager_version), O(cloudera_runtime_version) or O(cloudera_data_services_version) parameters can be specified.
"""

EXAMPLES = r"""
- name: Get all support matrix information
  cloudera.exe.supported:
  register: full_matrix

- name: Get support matrix for Cloudera Manager version
  cloudera.exe.supported:
    cloudera_manager_version: "7.13.1"
  register: cm_support

- name: Get support matrix for Cloudera Runtime version
  cloudera.exe.supported:
    cloudera_runtime_version: "7.1.9 SP1"
  register: base_support

- name: Get support matrix for Cloudera Data Services version
  cloudera.exe.supported:
    cloudera_data_services_version: "1.5.4"
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
            returned: always
        databases:
            description: Database compatibility information
            type: list
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
            returned: always
        operatingSystems:
            description: Operating system compatibility
            type: list
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
filters_applied:
    description: Summary of filters that were applied to the API request
    type: dict
    returned: always
    contains:
        cloudera_manager_version:
            description: Cloudera Manager version filter applied
            type: str
            returned: when filter applied
        cloudera_runtime_version:
            description: CDP Private Cloud Base version filter applied
            type: str
            returned: when filter applied
        cloudera_data_services_version:
            description: CDP Private Cloud Data Services version filter applied
            type: str
            returned: when filter applied
"""

import json
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.urls import fetch_url, to_text
from urllib.parse import quote


class ClouderaSupportMatrix:
    """
    Class to handle Cloudera Support Matrix API interactions.

    This class manages the construction of API requests, filtering parameters,
    and processing of responses from the Cloudera Support Matrix API.
    """

    BASE_URL = "https://supportmatrix.cloudera.com/supportmatrices/cldr"

    # Mapping of parameter names to actual product names in the API
    PRODUCT_NAME_MAPPING = {
        "cloudera_manager_version": "Cloudera Manager",
        "cloudera_runtime_version": "CDP Private Cloud Base",
        "cloudera_data_services_version": "CDP Private Cloud Data Services",
    }

    def __init__(self, module):
        """
        Initialize the ClouderaSupportMatrix class.

        Args:
            module: AnsibleModule instance
        """
        self.module = module

        # Extract product version parameters
        self.product_versions = {}
        for param_name in self.PRODUCT_NAME_MAPPING.keys():
            version = module.params.get(param_name)
            if version:
                self.product_versions[param_name] = version

        self.timeout = module.params.get("timeout", 30)

        # Initialize return values
        self.support_matrix_data = {}
        self.filters_applied = {}

        # Execute the logic
        self.process()

    def _build_query_conditions(self):
        """
        Build query conditions for API filtering.

        Returns:
            str: Query conditions string for the API request
        """
        conditions = []

        # Build single PRODUCT condition with comma-separated values
        if self.product_versions:
            products = []
            for param_name, version in self.product_versions.items():
                product_name = self.PRODUCT_NAME_MAPPING[param_name]
                # URL encode spaces in both product name and version
                # Use urllib.parse.quote for proper URL encoding
                product_version_string = f"{product_name}-{version}"
                encoded_product_version = quote(product_version_string)
                products.append(encoded_product_version)
                self.filters_applied[param_name] = version

            if products:
                # Join products with commas for a single PRODUCT parameter
                product_condition = f"PRODUCT={','.join(products)}"
                conditions.append(product_condition)

        return ";".join(conditions)

    def _build_api_url(self):
        """
        Build the complete API URL with query parameters.

        Returns:
            str: Complete API URL
        """
        conditions = self._build_query_conditions()

        if conditions:
            # Add trailing semicolon as shown in the curl example
            # Don't URL encode the entire condition string, only spaces are encoded
            api_url = f"{self.BASE_URL}?condition={conditions};"
        else:
            api_url = self.BASE_URL

        return api_url

    def process(self):
        """
        Fetch support matrix data from the Cloudera API using Ansible's fetch_url.

        Returns:
            bool: True if successful, False otherwise
        """

        try:
            # Build the API URL
            api_url = self._build_api_url()

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

            if info.get("status") != 200:
                self.module.fail_json(
                    msg=f"HTTP error occurred: {info.get('msg', 'Unknown error')}",
                    api_url=api_url,
                    http_status=info.get("status"),
                    http_reason=info.get("msg"),
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
                self.support_matrix_data = json.loads(response_text)
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
            cloudera_manager_version=dict(type="str", required=False),
            cloudera_runtime_version=dict(type="str", required=False),
            cloudera_data_services_version=dict(type="str", required=False),
            timeout=dict(type="int", default=30),
        ),
        mutually_exclusive=[
            (
                "cloudera_manager_version",
                "cloudera_runtime_version",
                "cloudera_data_services_version",
            ),
        ],
    )

    # Create and Fetch support matrix
    result = ClouderaSupportMatrix(module)

    # Prepare successful response
    output = dict(
        changed=False,
        support_matrix_data=result.support_matrix_data,
        filters_applied=result.filters_applied,
    )

    module.exit_json(**output)


if __name__ == "__main__":
    main()
