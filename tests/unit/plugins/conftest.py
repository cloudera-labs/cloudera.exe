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

import logging
import pytest

from ansible_collections.cloudera.exe.plugins.filter.core_exe import FilterModule as filters_exe
from ansible_collections.cloudera.exe.plugins.test.cldr import TestModule as tests_exe


LOG = logging.getLogger(__name__)

# Pytest fixtures

@pytest.fixture(scope="module")
def filter():
    def get_filter(filter_short_name: str):
        return filters_exe().filters().get(filter_short_name)
    return get_filter

@pytest.fixture(scope="module")
def test():
    def get_test(test_short_name: str):
        return tests_exe().tests().get(test_short_name)
    return get_test
