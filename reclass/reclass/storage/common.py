# -*- coding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

class NameMangler:
    @staticmethod
    def nodes(relpath, name):
        # nodes are identified just by their basename, so
        # no mangling required
        return relpath, name

    @staticmethod
    def composed_nodes(relpath, name):
        if relpath == '.' or relpath == '':
            # './' is converted to None
            return None, name
        parts = relpath.split(os.path.sep)
        if parts[0].startswith("_"):
            return relpath, name
        parts.append(name)
        return relpath, '.'.join(parts)

    @staticmethod
    def classes(relpath, name):
        if relpath == '.' or relpath == '':
            # './' is converted to None
            return None, name
        parts = relpath.split(os.path.sep)
        if name != 'init':
            # "init" is the directory index, so only append the basename
            # to the path parts for all other filenames. This has the
            # effect that data in file "foo/init.yml" will be registered
            # as data for class "foo", not "foo.init"
            parts.append(name)
        return relpath, '.'.join(parts)
