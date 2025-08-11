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

from ansible_collections.cloudera.exe.plugins.module_utils.cldr_version import (
    ClouderaVersion,
)

dataset = [
    # Core
    ("1.2.3", (1, 2, 3, None, None)),
    ("1.2", None),
    ("1", None),
    # Prerelease
    ("1.2.3-rc1", (1, 2, 3, tuple(["rc1"]), None)),
    ("1.2.3-rc1.foo", (1, 2, 3, tuple(["rc1", "foo"]), None)),
    ("1.2.3-rc1.400", (1, 2, 3, tuple(["rc1", 400]), None)),
    ("1.2.3-rc1-foo", (1, 2, 3, tuple(["rc1-foo"]), None)),
    ("1.2.3 SP1", (1, 2, 3, tuple(["SP1"]), None)),
    ("1.2.3 SP1.foo", (1, 2, 3, tuple(["SP1", "foo"]), None)),
    ("1.2.3 SP1.400", (1, 2, 3, tuple(["SP1", 400]), None)),
    ("1.2.3 SP1-foo", (1, 2, 3, tuple(["SP1-foo"]), None)),
    ("1.2.3.100", (1, 2, 3, tuple([100]), None)),
    ("1.2.3.100.400", (1, 2, 3, tuple([100, 400]), None)),
    ("1.2.3.100-400", (1, 2, 3, tuple(["100-400"]), None)),
    # Buildmeta
    ("1.2.3+400", (1, 2, 3, None, tuple([400]))),
    ("1.2.3+400.things", (1, 2, 3, None, tuple([400, "things"]))),
    ("1.2.3+400-things", (1, 2, 3, None, tuple(["400-things"]))),
    # Combined
    ("1.2.3-rc1+400", (1, 2, 3, tuple(["rc1"]), tuple([400]))),
    ("1.2.3-rc1.foo+400", (1, 2, 3, tuple(["rc1", "foo"]), tuple([400]))),
    (
        "1.2.3-rc1.foo+400.things",
        (1, 2, 3, tuple(["rc1", "foo"]), tuple([400, "things"])),
    ),
    # Invalid
    ("1.2.3=boom", None),
    ("1.2.3 boom=boom", None),
    ("1.2.3.boom=boom", None),
    ("1.2.3-boom=boom", None),
    # ("1.2.3+boom=boom", None),
]

comparisons = [
    # Core
    ("1.2.3", "1.2.3", 0),
    ("1.2.3", "1.2.4", -1),
    ("1.2.4", "1.2.3", 1),
    # Prerelease (i.e. service packs)
    ("1.2.3 SP1", "1.2.3 SP1", 0),
    ("1.2.3 SP1", "1.2.3 SP2", -1),
    ("1.2.3 SP2", "1.2.3 SP1", 1),
    # Ignored
    ("1.2.3 SP1+100", "1.2.3 SP1+200", 0),
    ("1.2.3 SP1+100", "1.2.4 SP1+100", -1),
    ("1.2.4 SP1+100", "1.2.3 SP1+100", 1),
    ("1.2.3 SP1+100", "1.2.3 SP1+200", 0),
    ("1.2.3 SP1+100", "1.2.4 SP1+100", -1),
    ("1.2.4 SP1+100", "1.2.3 SP1+100", 1),
]


@pytest.mark.parametrize("vstring,expected", dataset)
def test_parse(vstring, expected):
    version = ClouderaVersion()

    if expected is None:
        with pytest.raises(ValueError, match=vstring):
            version.parse(vstring)
    else:
        version.parse(vstring)

        assert version.major == expected[0]
        assert version.minor == expected[1]
        assert version.patch == expected[2]
        assert version.prerelease == expected[3]
        assert version.buildmetadata == expected[4]

        assert version.core == (expected[0], expected[1], expected[2])


@pytest.mark.parametrize("vstring,compare,expected", comparisons)
def test_comparisons(vstring, compare, expected):
    version = ClouderaVersion(vstring)

    assert version._cmp(compare) == expected
