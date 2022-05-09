#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2022 Cloudera, Inc. All Rights Reserved.
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

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import flatten
from ansible.template import recursive_check_defined
from ansible.utils.vars import merge_hash


def combine_onto(*terms, **kwargs):
    """
    Allow merge of source dictionaries onto target dictionaries.
    """
    recursive = kwargs.pop('recursive', False)
    list_merge = kwargs.pop('list_merge', 'replace')
    if kwargs:
        raise AnsibleFilterError("'recursive' and 'list_merge' are the only valid keyword arguments")

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
    ''' Derivatives of Ansible jinja2 filters '''

    def filters(self):
        filters = {
            'combine_onto': combine_onto
        }

        return filters
