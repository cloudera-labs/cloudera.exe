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
  name: semantic_version
  author: Webster Mudge (@wmudge) <wmudge@cloudera.com>
  short_description: Parse a semantic version string
  description:
    - Semantic version string parsing.
    - Returns a dictionary of the semantic version parts.
    - See https://semver.org
  positional: _input
  options:
    _input:
      description: A semantic version string to parse.
      type: dict
      required: True
"""

EXAMPLES = """
# Parse a standard version string
standard: "{{ '1.2.3' | semantic_version }}"

# Parse a version plus prerelease string
prerelease: "{{ '1.2.3-rc1' | semantic_version }}"

# Parse a version plus build metadata string
build: "{{ '1.2.3+build7' | semantic_version }}"

# Parse a version plus prerelease and build string
full: "{{ '1.2.3-rc1+build7' | semantic_version }}"
"""

RETURN = """
_value:
  description:
    - A dictionary of the semantic version parts.
    - If unable to parse the string, returns C(None).
  type: dict
  options:
    major:
      description: Major version
    minor:
      description: Minor version
    patch:
      description: Patch version
    prerelease:
      description: Prerelease version
      returned: when supported
    buildmetadata:
      description: Build metadata version
      returned: when supported
"""

import re

from ansible.errors import AnsibleFilterError

SEMVER_REGEX = re.compile(
    "^(?P<major>0|[1-9]\\d*)\\.(?P<minor>0|[1-9]\\d*)\\.(?P<patch>0|[1-9]\\d*)(?:-(?P<prerelease>(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?$",
)


def semantic_version(version: str):
    """
    Parse a semantic version string into its parts.

    See: https://semver.org/
    """

    try:
        semver = re.fullmatch(SEMVER_REGEX, version)
    except Exception as e:
        raise AnsibleFilterError(orig_exc=e)

    if semver is not None:
        return semver.groupdict()


class FilterModule(object):
    def filters(self):
        filters = {"semantic_version": semantic_version}

        return filters
