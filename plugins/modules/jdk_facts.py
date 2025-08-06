#!/usr/bin/python

# Copyright 2024 Cloudera, Inc.
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

DOCUMENTATION = r"""
module: jdk_facts
short_description: Retrieve JDK information
description:
  - Retrieve information about the installed Java JDK as facts.
options: {}
author:
  - Webster Mudge <wmudge@cloudera.com>
extends_documentation_fragment:
  - action_common_attributes
  - action_common_attributes.facts
attributes:
  check_mode:
    support: full
  diff_mode:
    support: none
  facts:
    support: full
  platform:
    support: full
  seealso:
    description: Java version history
    link: https://en.wikipedia.org/wiki/Java_version_history
"""

EXAMPLES = r"""
- name: Retrieve JDK details
  cloudera.exe.jdk_facts:
"""

RETURN = r"""
ansible_facts:
  description: Facts to add to ansible_facts.
  returned: always
  type: complex
  contains:
    jdk:
      description:
        - Details on installed Java JDK executable.
      returned: always
      type: dict
      contains:
        provider:
          description:
            - JDK provider.
            - Normalized for Oracle trademark.
            - Returns C(None) if no JDK is discovered.
          returned: always
        version:
          description:
            - JDK version string in its entirety.
          returned: when supported
        major:
          description:
            - JDK C(major) version.
          returned: when supported
        minor:
          description:
            - JDK C(minor) version.
          returned: when supported
        patch:
          description:
            - JDK C(patch) version.
          returned: when supported
        release:
          description:
            - JDK C(release) version.
          returned: when supported
        build:
          description:
            - JDK C(build) version.
          returned: when supported
        update:
          description:
            - JDK C(update) details.
          returned: when supported
"""


import re

from ansible.module_utils.basic import AnsibleModule

VERSION_REGEX = re.compile(
    "(?P<provider>[\\w\\(\\)]+)"
    + ".*"
    + "\\(build\\s*"
    + "(?P<version>"
    + "(?P<major>\\d*)"
    + "\\.?(?P<minor>\\d*)"
    + "\\.?(?P<patch>\\d*)"
    + "[+-_]?(?P<release>[\\w\\d]*)"
    + "[+-_]?(?P<build>[\\w\\d]*)"
    + ")"
    + "\\)",
)

UPDATE_REGEX = re.compile('".+"\\s*([\\w-]*)')


def main():
    result = dict(
        ansible_facts=dict(jdk=dict()),
        changed=False,
    )

    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)

    rc, _, stderr = module.run_command("/usr/bin/java -version")
    if rc != 0:
        module.warn(f"Unable to discover JDK facts: {stderr}")
        result["ansible_facts"]["jdk"].update(provider=None)
    else:
        output = stderr.splitlines()

        version = VERSION_REGEX.search(output[1])
        update = UPDATE_REGEX.search(output[0])

        result["ansible_facts"]["jdk"].update(
            provider=(
                "Oracle"
                if version.group("provider") == "Java(TM)"
                else version.group("provider")
            ),
            version=version.group("version"),
            major=version.group("major"),
            minor=version.group("minor"),
            patch=version.group("patch"),
            release=version.group("release"),
            build=version.group("build"),
            update=(update[1] if update is not None else ""),
        )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
