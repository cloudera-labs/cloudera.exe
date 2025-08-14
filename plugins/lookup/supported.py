# -*- coding: utf-8 -*-

# Copyright 2025 Cloudera, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
name: supported
short_description: Get support matrix details
description:
    - Retrieve support matrix details for Cloudera Manager, Runtime, or Data Services versions.
author: Cloudera Labs
version_added: 3.0.0
options:
    _terms:
        description:
            - The categories to return from the support matrix.
            - All category entries will be flattened into a single list.
            - If undefined, all categories will be returned.
        type: str
        required: false
        choices:
            - browsers
            - databases
            - jdks
            - kubernetes
            - operating_systems
            - processor
            - products
    version:
        description: The version of the product
        type: str
        required: true
    product:
        description: The anchor product for the support matrix.
        type: str
        required: true
        choices:
            - cloudera_manager
            - cloudera_runtime
            - cloudera_data_services
    timeout:
        description: Query timeout (seconds)
        type: int
        required: false
        default: 30
"""

EXAMPLES = """
"""

RETURN = """
_value:
    description:
        - The contents of the license.
    type: list
    elements: list
    contains: {}
"""

import json
from urllib.error import HTTPError, URLError

from ansible.errors import AnsibleLookupError
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.common.dict_transformations import _snake_to_camel
from ansible.module_utils.urls import open_url, ConnectionError, SSLValidationError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

from ansible_collections.cloudera.exe.plugins.module_utils.cldr_supported import (
    parse_support_entries,
    support_matrix_url,
)

display = Display()


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        self.set_options(var_options=variables, direct=kwargs)

        product = self.get_option("product")
        version = self.get_option("version")
        timeout = self.get_option("timeout")

        matrix_url, filters = support_matrix_url({product: version})

        display.v(f"[DEBUG] Support Matrix URL: {matrix_url}")

        ret = []

        try:
            response = open_url(
                matrix_url,
                headers={
                    "Accept": "*/*",
                    "Content-Type": "application/json",
                },
                http_agent="Ansible/cloudera.cluster",
                timeout=timeout,
                follow_redirects="false",
            )
        except HTTPError as e:
            if e.status == 302:
                msg = ' '.join({f"{key}-{value}" for key, value in filters.items()})
                display.warning(f"{msg} does not exist.")
                return []
            raise AnsibleLookupError(
                "Received HTTP error for %s : %s" % (matrix_url, to_native(e))
            )
        except URLError as e:
            raise AnsibleLookupError(
                "Failed lookup url for %s : %s" % (matrix_url, to_native(e))
            )
        except SSLValidationError as e:
            raise AnsibleLookupError(
                "Error validating the server's certificate for %s: %s"
                % (matrix_url, to_native(e))
            )
        except ConnectionError as e:
            raise AnsibleLookupError(
                "Error connecting to %s: %s" % (matrix_url, to_native(e))
            )

        try:
            matrix = json.loads(response.read())

            if terms:
                for t in terms:
                    ret.extend(parse_support_entries(matrix.get(_snake_to_camel(t), [])))
            else:
                for _, v in matrix.items():
                    if v:
                        ret.extend(parse_support_entries(v))
        except json.JSONDecodeError as e:
            raise AnsibleLookupError(
                "Error parsing support matrix JSON: %s" % to_native(e)
            )

        return ret
