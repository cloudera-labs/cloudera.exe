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

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest


from tests.unit import (
    AnsibleExitJson,
)

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.cloudera.exe.plugins.modules import jdk_facts


def test_execution_error(module_args, monkeypatch):
    module_args()

    def mock_exec(*args, **kwargs):
        return 1, None, "ERROR"

    monkeypatch.setattr(AnsibleModule, "run_command", mock_exec)

    with pytest.raises(AnsibleExitJson) as e:
        jdk_facts.main()

    assert e.value.ansible_facts["jdk"]
    assert e.value.ansible_facts["jdk"]["provider"] == None


def test_oracle_5(module_args, monkeypatch):
    module_args()

    def mock_exec(*args, **kwargs):
        stderr = [
            'java version "1.5.0_07"',
            "Java(TM) 2 Runtime Environment, Standard Edition (build 1.5.0_07-b03)",
            "Java HotSpot(TM) Client VM (build 1.5.0_07-b03, mixed mode, sharing)",
        ]
        return 0, "", "\n".join(stderr)

    monkeypatch.setattr(AnsibleModule, "run_command", mock_exec)

    with pytest.raises(AnsibleExitJson) as e:
        jdk_facts.main()

    assert e.value.ansible_facts["jdk"]
    assert e.value.ansible_facts["jdk"]["provider"] == "Oracle"
    assert e.value.ansible_facts["jdk"]["version"] == "1.5.0_07-b03"
    assert e.value.ansible_facts["jdk"]["major"] == "1"
    assert e.value.ansible_facts["jdk"]["minor"] == "5"
    assert e.value.ansible_facts["jdk"]["patch"] == "0"
    assert e.value.ansible_facts["jdk"]["release"] == "07"
    assert e.value.ansible_facts["jdk"]["build"] == "b03"
    assert e.value.ansible_facts["jdk"]["update"] == ""


def test_openjdk_23(module_args, monkeypatch):
    module_args()

    def mock_exec(*args, **kwargs):
        stderr = [
            'openjdk version "23" 2024-09-17',
            "OpenJDK Runtime Environment Homebrew (build 23)",
            "OpenJDK 64-Bit Server VM Homebrew (build 23, mixed mode, sharing)",
        ]
        return 0, "", "\n".join(stderr)

    monkeypatch.setattr(AnsibleModule, "run_command", mock_exec)

    with pytest.raises(AnsibleExitJson) as e:
        jdk_facts.main()

    assert e.value.ansible_facts["jdk"]
    assert e.value.ansible_facts["jdk"]["provider"] == "OpenJDK"
    assert e.value.ansible_facts["jdk"]["version"] == "23"
    assert e.value.ansible_facts["jdk"]["major"] == "23"
    assert e.value.ansible_facts["jdk"]["minor"] == ""
    assert e.value.ansible_facts["jdk"]["patch"] == ""
    assert e.value.ansible_facts["jdk"]["release"] == ""
    assert e.value.ansible_facts["jdk"]["build"] == ""
    assert e.value.ansible_facts["jdk"]["update"] == "2024-09-17"


def test_openjdk_8(module_args, monkeypatch):
    module_args()

    def mock_exec(*args, **kwargs):
        stderr = [
            'openjdk version "1.8.0_432"',
            "OpenJDK Runtime Environment (build 1.8.0_432-b06)",
            "OpenJDK 64-Bit Server VM (build 25.432-b06, mixed mode)",
        ]
        return 0, "", "\n".join(stderr)

    monkeypatch.setattr(AnsibleModule, "run_command", mock_exec)

    with pytest.raises(AnsibleExitJson) as e:
        jdk_facts.main()

    assert e.value.ansible_facts["jdk"]
    assert e.value.ansible_facts["jdk"]["provider"] == "OpenJDK"
    assert e.value.ansible_facts["jdk"]["version"] == "1.8.0_432-b06"
    assert e.value.ansible_facts["jdk"]["major"] == "1"
    assert e.value.ansible_facts["jdk"]["minor"] == "8"
    assert e.value.ansible_facts["jdk"]["patch"] == "0"
    assert e.value.ansible_facts["jdk"]["release"] == "432"
    assert e.value.ansible_facts["jdk"]["build"] == "b06"
    assert e.value.ansible_facts["jdk"]["update"] == ""
