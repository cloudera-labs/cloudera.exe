# -*- coding: utf-8 -*-
# Copyright 2024 Cloudera, Inc.
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
  name: cm_version
  author: Webster Mudge (@wmudge) <wmudge@cloudera.com>
  short_description: Parse a Cloudera Manager version string
  description:
    - Cloudera Manager version string parsing.
    - Returns a dictionary of the version parts.
  positional: _input
  options:
    _input:
      description: A version string to parse.
      type: dict
      required: True
"""

EXAMPLES = """
- name: Parse a standard version string
  ansible.builtin.set_fact:
    standard: "{{ '1.2.3' | cm_version }}"

- name: Parse a version plus build number
  ansible.builtin.set_fact:
    build: "{{ '1.2.3.4' | cm_version }}"

- name: Parse a version plus build metadata string
  ansible.builtin.set_fact:
    build: "{{ '1.2.3+build7' | cm_version }}"

- name: Parse a version plus prerelease and build string
  ansible.builtin.set_fact:
    full: "{{ '1.2.3-rc1+build7' | cm_version }}"
"""

RETURN = """
_value:
  description:
    - A dictionary of the version parts.
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

CM_REGEX = re.compile(
    "^(?P<major>0|[1-9]\\d*)"
    + "\\.(?P<minor>0|[1-9]\\d*)"
    + "\\.(?P<patch>0|[1-9]\\d*)"
    + "(?:-(?P<prerelease>(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
    + "(?:[\\+|\\.](?P<buildmetadata>[0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?$",
)


def cm_version(version: str):
    """
    Parse a Cloudera Manager version string into its parts.
    """

    try:
        ver = re.fullmatch(CM_REGEX, version)
    except Exception as e:
        raise AnsibleFilterError(orig_exc=e)

    if ver is not None:
        return ver.groupdict()


class FilterModule(object):
    def filters(self):
        filters = {"cm_version": cm_version}

        return filters
