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

from typing import Tuple
from urllib.parse import quote

from ansible.module_utils.common.dict_transformations import _camel_to_snake

BASE_URL = "https://supportmatrix.cloudera.com/supportmatrices/cldr"

# Mapping of parameter names to actual product names in the API
PRODUCT_NAME_MAPPING = {
    "cloudera_manager": "Cloudera Manager",
    "cloudera_runtime": "CDP Private Cloud Base",
    "cloudera_data_services": "CDP Private Cloud Data Services",
}


def support_matrix_url(product_versions: dict[str, str]) -> Tuple[str, dict[str, str]]:
    """Construct the URL to the Support Matrix server.

    Args:
        product_versions (dict[str, str]): product short names and version strings

    Returns:
        Tuple[str, dict[str, str]]: URL and dictionary of mapped product full names and version strings
    """
    conditions = []
    filters = {}

    # Build single PRODUCT condition with comma-separated values
    if product_versions:
        products = []
        for short_name, version in product_versions.items():
            product_name = PRODUCT_NAME_MAPPING[short_name]
            # URL encode spaces in both product name and version
            # Use urllib.parse.quote for proper URL encoding
            product_version_string = f"{product_name}-{version}"
            encoded_product_version = quote(product_version_string)

            products.append(encoded_product_version)
            filters[product_name] = version

        if products:
            # Join products with commas for a single PRODUCT parameter
            product_condition = f"PRODUCT={','.join(products)}"
            conditions.append(product_condition)

    if conditions:
        # Add trailing semicolon as shown in the curl example
        # Don't URL encode the entire condition string, only spaces are encoded
        api_url = "%s?condition=%s;" % (BASE_URL, ";".join(conditions))
    else:
        api_url = BASE_URL

    return api_url, filters


ENTRY_KEYS = set(
    [
        "description",
        "family",
        "id",
        "version",
        "group",
        "org",
        "productName",
        "release_date",
        "name",
    ]
)


def parse_support_entries(entries: list[dict]) -> list[dict]:
    """Constrain support matrix entries to a known set of keys.

    Args:
        entries (list[dict]): Support matrix entries

    Returns:
        list[dict]: Entries with only 'description', 'family', 'id', 'version', 'group', 'org', 'product_name', and 'release_date'.
    """
    return [
        {_camel_to_snake(k): v for k, v in d.items() if k in ENTRY_KEYS}
        for d in entries
    ]
