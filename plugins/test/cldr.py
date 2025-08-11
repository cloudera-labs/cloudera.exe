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

import operator as py_operator

from ansible import errors
from ansible.module_utils.common.text.converters import to_native, to_text

from ansible_collections.cloudera.exe.plugins.module_utils.cldr_version import (
    ClouderaVersion,
)


def cldr_version_compare(value, version, operator="eq"):
    """Perform a Cloudera version comparison on a value"""
    op_map = {
        "==": "eq",
        "=": "eq",
        "eq": "eq",
        "<": "lt",
        "lt": "lt",
        "<=": "le",
        "le": "le",
        ">": "gt",
        "gt": "gt",
        ">=": "ge",
        "ge": "ge",
        "!=": "ne",
        "<>": "ne",
        "ne": "ne",
    }

    if operator in op_map:
        operator = op_map[operator]
    else:
        raise errors.AnsibleFilterError(
            "Invalid operator type (%s). Must be one of %s"
            % (operator, ", ".join(map(repr, op_map))),
        )

    try:
        method = getattr(py_operator, operator)
        return method(
            ClouderaVersion(to_text(value)),
            ClouderaVersion(to_text(version)),
        )
    except Exception as e:
        raise errors.AnsibleFilterError("Version comparison failed: %s" % to_native(e))


class TestModule(object):
    """Cloudera jinja2 tests"""

    def tests(self):
        return {
            # failure testing
            "version": cldr_version_compare,
        }
