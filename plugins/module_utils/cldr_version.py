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

import re

from ansible.module_utils.compat.version import LooseVersion, Version
from ansible.utils.version import _Alpha, _Numeric


CLDR_RE = re.compile(
    r"""
    ^
        (?P<major>0|[1-9]\d*)
        \.
        (?P<minor>0|[1-9]\d*)
        \.
        (?P<patch>0|[1-9]\d*)
        (?:
            [ \.\-]*
            (?P<prerelease>
                (?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)
                (?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*
            )
        )?
        (?:
            \+
            (?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*)
        )?
    $
    """,
    flags=re.X
)

class ClouderaVersion(Version):
    """Version comparison class that implements Cloudera versioning.

    Cloudera versioning is an extension of Semantic Versioning that uses the
    ``prerelease`` segment as service packs or patch releases.
    
    Moreover, this versioning scheme allow the ``prerelease`` delimiter
    to use whitespace (' ') and dots  ('.') in addition to the semantic 
    version's dash ('-').

    Based off of ``distutils.version.Version`` and ``ansible.utils.version``.
    """

    version_re = CLDR_RE

    def __init__(self, vstring=None):
        self.vstring = vstring
        self.major = None
        self.minor = None
        self.patch = None
        self.prerelease = ()
        self.buildmetadata = ()

        if vstring:
            self.parse(vstring)

    def __repr__(self):
        return 'ClouderaVersion(%r)' % self.vstring

    @staticmethod
    def from_loose_version(loose_version):
        """This method is designed to take a ``LooseVersion``
        and attempt to construct a ``ClouderaVersion`` from it

        This is useful where you want to do simple version math
        without requiring users to provide a compliant semver.
        """
        if not isinstance(loose_version, LooseVersion):
            raise ValueError("%r is not a LooseVersion" % loose_version)

        try:
            version = loose_version.version[:]
        except AttributeError:
            raise ValueError("%r is not a LooseVersion" % loose_version)

        extra_idx = 3
        for marker in ('-', '+'):
            try:
                idx = version.index(marker)
            except ValueError:
                continue
            else:
                if idx < extra_idx:
                    extra_idx = idx
        version = version[:extra_idx]

        if version and set(type(v) for v in version) != set((int,)):
            raise ValueError("Non integer values in %r" % loose_version)

        # Extra is everything to the right of the core version
        extra = re.search('[+-].+$', loose_version.vstring)

        version = version + [0] * (3 - len(version))
        return ClouderaVersion(
            '%s%s' % (
                '.'.join(str(v) for v in version),
                extra.group(0) if extra else ''
            )
        )

    def parse(self, vstring) -> None:
        match = CLDR_RE.match(vstring)
        if not match:
            raise ValueError("invalid Cloudera version '%s'" % vstring)

        (major, minor, patch, prerelease, buildmetadata) = match.group(1, 2, 3, 4, 5)
        self.vstring = vstring
        self.major = int(major)
        self.minor = int(minor)
        self.patch = int(patch)

        self.prerelease = None
        self.buildmetadata = None

        if prerelease:
            self.prerelease = tuple(_Numeric(x) if x.isdigit() else _Alpha(x) for x in prerelease.split('.'))
        if buildmetadata:
            self.buildmetadata = tuple(_Numeric(x) if x.isdigit() else _Alpha(x) for x in buildmetadata.split('.'))

    @property
    def core(self) -> tuple[int | None, int | None, int | None]:
        return self.major, self.minor, self.patch

    @property
    def is_prerelease(self) -> bool:
        return bool(self.prerelease)

    @property
    def is_stable(self) -> bool:
        # Major version zero (0.y.z) is for initial development. Anything MAY change at any time.
        # The public API SHOULD NOT be considered stable.
        # https://semver.org/#spec-item-4
        return not (self.major == 0 or self.is_prerelease)

    def _cmp(self, other) -> int:
        if isinstance(other, str):
            other = ClouderaVersion(other)

        if self.core != other.core:
            # if the core version doesn't match
            # prerelease and buildmetadata doesn't matter
            if self.core < other.core:
                return -1
            else:
                return 1

        if not any((self.prerelease, other.prerelease)):
            return 0

        if self.prerelease and not other.prerelease:
            return 1
        elif not self.prerelease and other.prerelease:
            return -1
        else:
            if self.prerelease < other.prerelease:
                return -1
            elif self.prerelease > other.prerelease:
                return 1

        # Build metadata MUST be ignored when determining version precedence
        # https://semver.org/#spec-item-10
        # With the above in mind it is ignored here

        # If we have made it here, things should be equal
        return 0

    # The Py2 and Py3 implementations of distutils.version.Version
    # are quite different, this makes the Py2 and Py3 implementations
    # the same
    def __eq__(self, other):
        return self._cmp(other) == 0

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self._cmp(other) < 0

    def __le__(self, other):
        return self._cmp(other) <= 0

    def __gt__(self, other):
        return self._cmp(other) > 0

    def __ge__(self, other):
        return self._cmp(other) >= 0
