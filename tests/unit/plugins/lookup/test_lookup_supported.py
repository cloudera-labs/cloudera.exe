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

from ansible.plugins.loader import lookup_loader


@pytest.mark.skip("Unable to load non-builtin collection resources")
def test_lookup_supported():
    supported_lookup = lookup_loader.get("cloudera.exe.supported") # , collection_list=[request.config.rootdir]

    # lookup('cloudera.exe.supported', "7.1.9", type="cloudera_manager", categories=["jdks", "products"])
    # lookup('cloudera.exe.supported', ["jdks", "products"], version="7.1.9", type="cloudera_manager")
    # lookup('cloudera.exe.supported', version="7.1.9", type="cloudera_manager")
    # lookup('cloudera.exe.supported', "jdks", version="7.3.1 SP2", type="cloudera_runtime")
    actual = supported_lookup.run(["7.1.9"], type="cloudera_manager")
