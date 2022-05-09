# -*- coding: utf-8 -*-

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