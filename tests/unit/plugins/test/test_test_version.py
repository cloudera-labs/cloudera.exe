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

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest


dataset = [
    # Equal
    ("1.2.3", "1.2.3", "eq", True),
    ("1.2.3", "1.2.4", "eq", False),
    ("1.2.3", "1.2.2", "eq", False),
    ("1.2.3 SP1", "1.2.3 SP1", "eq", True),
    ("1.2.3 SP1", "1.2.3 SP2", "eq", False),
    ("1.2.3 SP2", "1.2.3 SP1", "eq", False),
    ("1.2.3 SP2", "1.2.2 SP2", "eq", False),
    ("1.2.2 SP2", "1.2.3 SP2", "eq", False),
    ("1.2.3+100", "1.2.3+100", "eq", True),  # Buildmetadata is ignored
    ("1.2.3+100", "1.2.3+200", "eq", True),
    ("1.2.3+200", "1.2.3+100", "eq", True),
    ("1.2.3+100", "1.2.4+100", "eq", False),
    ("1.2.3+100", "1.2.2+100", "eq", False),
    # Not equal
    ("1.2.3", "1.2.3", "ne", False),
    ("1.2.3", "1.2.4", "ne", True),
    ("1.2.3", "1.2.2", "ne", True),
    ("1.2.3 SP1", "1.2.3 SP1", "ne", False),
    ("1.2.3 SP1", "1.2.3 SP2", "ne", True),
    ("1.2.3 SP2", "1.2.3 SP1", "ne", True),
    ("1.2.3 SP2", "1.2.2 SP2", "ne", True),
    ("1.2.2 SP2", "1.2.3 SP2", "ne", True),
    ("1.2.3+100", "1.2.3+100", "ne", False),  # Buildmetadata is ignored
    ("1.2.3+100", "1.2.3+200", "ne", False),
    ("1.2.3+200", "1.2.3+100", "ne", False),
    ("1.2.3+100", "1.2.4+100", "ne", True),
    ("1.2.3+100", "1.2.2+100", "ne", True),
    # Less than
    ("1.2.3", "1.2.3", "lt", False),
    ("1.2.3", "1.2.4", "lt", True),
    ("1.2.3", "1.2.2", "lt", False),
    ("1.2.3 SP1", "1.2.3 SP1", "lt", False),
    ("1.2.3 SP1", "1.2.3 SP2", "lt", True),
    ("1.2.3 SP2", "1.2.3 SP1", "lt", False),
    ("1.2.3 SP2", "1.2.2 SP2", "lt", False),
    ("1.2.2 SP2", "1.2.3 SP2", "lt", True),
    ("1.2.3+100", "1.2.3+100", "lt", False),  # Buildmetadata is ignored
    ("1.2.3+100", "1.2.3+200", "lt", False),
    ("1.2.3+200", "1.2.3+100", "lt", False),
    ("1.2.3+100", "1.2.4+100", "lt", True),
    ("1.2.3+100", "1.2.2+100", "lt", False),
    # Less than or equal
    ("1.2.3", "1.2.3", "le", True),
    ("1.2.3", "1.2.4", "le", True),
    ("1.2.3", "1.2.2", "le", False),
    ("1.2.3 SP1", "1.2.3 SP1", "le", True),
    ("1.2.3 SP1", "1.2.3 SP2", "le", True),
    ("1.2.3 SP2", "1.2.3 SP1", "le", False),
    ("1.2.3 SP2", "1.2.2 SP2", "le", False),
    ("1.2.2 SP2", "1.2.3 SP2", "le", True),
    ("1.2.3+100", "1.2.3+100", "le", True),  # Buildmetadata is ignored
    ("1.2.3+100", "1.2.3+200", "le", True),
    ("1.2.3+200", "1.2.3+100", "le", True),
    ("1.2.3+100", "1.2.4+100", "le", True),
    ("1.2.3+100", "1.2.2+100", "le", False),
    # Greater than
    ("1.2.3", "1.2.3", "gt", False),
    ("1.2.3", "1.2.4", "gt", False),
    ("1.2.3", "1.2.2", "gt", True),
    ("1.2.3 SP1", "1.2.3 SP1", "gt", False),
    ("1.2.3 SP1", "1.2.3 SP2", "gt", False),
    ("1.2.3 SP2", "1.2.3 SP1", "gt", True),
    ("1.2.3 SP2", "1.2.2 SP2", "gt", True),
    ("1.2.2 SP2", "1.2.3 SP2", "gt", False),
    ("1.2.3+100", "1.2.3+100", "gt", False),  # Buildmetadata is ignored
    ("1.2.3+100", "1.2.3+200", "gt", False),
    ("1.2.3+200", "1.2.3+100", "gt", False),
    ("1.2.3+100", "1.2.4+100", "gt", False),
    ("1.2.3+100", "1.2.2+100", "gt", True),
    # Greater than or equal
    ("1.2.3", "1.2.3", "ge", True),
    ("1.2.3", "1.2.4", "ge", False),
    ("1.2.3", "1.2.2", "ge", True),
    ("1.2.3 SP1", "1.2.3 SP1", "ge", True),
    ("1.2.3 SP1", "1.2.3 SP2", "ge", False),
    ("1.2.3 SP2", "1.2.3 SP1", "ge", True),
    ("1.2.3 SP2", "1.2.2 SP2", "ge", True),
    ("1.2.2 SP2", "1.2.3 SP2", "ge", False),
    ("1.2.3+100", "1.2.3+100", "ge", True),  # Buildmetadata is ignored
    ("1.2.3+100", "1.2.3+200", "ge", True),
    ("1.2.3+200", "1.2.3+100", "ge", True),
    ("1.2.3+100", "1.2.4+100", "ge", False),
    ("1.2.3+100", "1.2.2+100", "ge", True),
]


@pytest.mark.parametrize("vstring,comparison,operator,expected", dataset)
def test_test_version(test, vstring, comparison, operator, expected):
    version_test = test("version")

    assert version_test(vstring, comparison, operator) == expected
