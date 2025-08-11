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
    ("1.2.3", (1, 2, 3, None, None)),
    ("1.2.3 SP1", (1, 2, 3, tuple(["SP1"]), None)),
    ("1.2.3-SP1", (1, 2, 3, tuple(["SP1"]), None)),
    ("1.2.3.SP1", (1, 2, 3, tuple(["SP1"]), None)),
    ("1.2.3 SP1.400", (1, 2, 3, tuple(["SP1", 400]), None)),
    ("1.2.3+Build", (1, 2, 3, None, tuple(["Build"]))),
    ("1.2.3+Build.400", (1, 2, 3, None, tuple(["Build", 400]))),
]


@pytest.mark.parametrize("vstring,expected", dataset)
def test_filter_version(filter, vstring, expected):
    version_filter = filter("version")

    actual = version_filter(vstring)

    assert actual.get("major") == expected[0]
    assert actual.get("minor") == expected[1]
    assert actual.get("patch") == expected[2]
    assert actual.get("prerelease") == expected[3]
    assert actual.get("buildmetadata") == expected[4]
