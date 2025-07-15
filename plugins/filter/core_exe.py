#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2023 Cloudera, Inc. All Rights Reserved.
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

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
name: combine_onto
author: Webster Mudge (@wmudge) <wmudge@cloudera.com>
short_description: combine two dictionaries
description:
    - Create a dictionary (hash/associative array) as a result of merging existing dictionaries.
    - This is the reverse of the C(ansible.builtin.combine) filter.
version_added: 1.0.0
positional: _input, _dicts
options:
    _input:
        description:
            - First dictionary to combine.
        type: dict
        required: True
    _dicts:
        description:
            - The list of dictionaries to combine
        type: list
        elements: dict
        required: True
    recursive:
        description:
            - If V(True), merge elements recursively.
        type: boolean
        default: False
    list_merge:
        description: Behavior when encountering list elements.
        type: str
        default: replace
        choices:
            replace: overwrite older entries with newer ones
            keep: discard newer entries
            append: append newer entries to the older ones
            prepend: insert newer entries in front of the older ones
            append_rp: append newer entries to the older ones, overwrite duplicates
            prepend_rp: insert newer entries in front of the older ones, discard duplicates
"""

EXAMPLES = """
# ab => {'a':1, 'b':2, 'c': 4}
ab: "{{ {'a':1, 'b':2} | cloudera.exe.combine_onto({'b':3, 'c':4}) }}"

many: "{{ dict1 | cloudera.exe.combine_onto(dict2, dict3, dict4) }}"

# defaults => {'a':{'b':3, 'c':4}, 'd': 5}
# customization => {'a':{'c':20}}
# final => {'a':{'b':3, 'c':20}, 'd': 5}
final: "{{ customization | cloudera.exe.combine_onto(defaults, recursive=true) }}"
"""

RETURN = """
_value:
    description: Resulting merge of supplied dictionaries.
    type: dict
"""

from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import flatten
from ansible.template import recursive_check_defined
from ansible.utils.vars import merge_hash


def combine_onto(*terms, **kwargs):
    """
    Allow merge of source dictionaries onto target dictionaries.
    """
    recursive = kwargs.pop("recursive", False)
    list_merge = kwargs.pop("list_merge", "replace")
    if kwargs:
        raise AnsibleFilterError(
            "'recursive' and 'list_merge' are the only valid keyword arguments",
        )

    # allow the user to do `[dict1, dict2, ...] | combine`
    dictionaries = flatten(terms, levels=1)

    # recursively check that every elements are defined (for jinja2)
    recursive_check_defined(dictionaries)

    if not dictionaries:
        return {}

    if len(dictionaries) == 1:
        return dictionaries[0]

    # Ignore the original combine() filter's dict precedence
    result = dictionaries.pop(0)
    for dictionary in dictionaries:
        result = merge_hash(dictionary, result, recursive, list_merge)

    return result


class FilterModule(object):
    """Derivatives of Ansible jinja2 filters"""

    def filters(self):
        filters = {"combine_onto": combine_onto}

        return filters
