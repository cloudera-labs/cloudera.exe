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

import pytest
import unittest
from unittest.mock import patch, MagicMock

from ansible_collections.cloudera.exe.plugins.filter import core_exe
from ansible.plugins.loader import filter_loader


class TestFilterModule(unittest.TestCase):

    def setUp(self):
        self.filter = filter_loader.get('cloudera.exe.core_exe')

    def test_combine_onto(self):
        self.assertIn("combine_onto", self.filter.filters().keys())
        test_filter = self.filter.filters().get('combine_onto')

        # Source will combine ONTO the target, overriding the target
        source_dict = {
            "foo": "bar",
            "gaz": "blaz",
            "nested": {
                "duz": "ferr"
            }
        }
        target_dict = {
            "gaz": "blergh",
            "derr": "zaar",
            "nested": {
                "wuz": "gug"
            }
        }

        expected_results = {
            "foo": "bar",
            "gaz": "blaz",
            "derr": "zaar",
            "nested": {
                "duz": "ferr"
            }
        }
        self.assertDictEqual(expected_results,
                             test_filter([source_dict, target_dict]))

        expected_results_recursive = {
            "foo": "bar",
            "gaz": "blaz",
            "derr": "zaar",
            "nested": {
                "duz": "ferr",
                "wuz": "gug"
            }
        }
        self.assertDictEqual(expected_results_recursive,
                             test_filter([source_dict, target_dict], recursive=True))
