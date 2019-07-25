#
# -*- coding: utf-8 -*-
#
# This file is part of reclass (http://github.com/madduck/reclass)
#
# Copyright © 2007–14 martin f. krafft <madduck@madduck.net>
# Released under the terms of the Artistic Licence 2.0
#
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import six
import re

class DictPath(object):
    '''
    Represents a path into a nested dictionary.

    Given a dictionary like

      d['foo']['bar'] = 42

    it can be desirable to obtain a reference to the value stored in the
    sub-levels, allowing that value to be accessed and changed. Unfortunately,
    Python provides no easy way to do this, since

      ref = d['foo']['bar']

    does become a reference to the integer 42, but that reference is
    overwritten when one assigns to it. Hence, DictPath represents the path
    into a nested dictionary, and can be "applied to" a dictionary to obtain
    and set values, using a list of keys, or a string representation using
    a delimiter (which can be escaped):

      p = DictPath(':', 'foo:bar')
      p.get_value(d)
      p.set_value(d, 43)

    This is a bit backwards, but the right way around would require support by
    the dict() type.

    The primary purpose of this class within reclass is to cater for parameter
    interpolation, so that a reference such as ${foo:bar} in a parameter value
    may be resolved in the context of the Parameter collections (a nested
    dict).

    If the value is a list, then the "key" is assumed to be and interpreted as
    an integer index:

      d = {'list': [{'one':1},{'two':2}]}
      p = DictPath(':', 'list:1:two')
      p.get_value(d)  → 2

    This heuristic is okay within reclass, because dictionary keys (parameter
    names) will always be strings. Therefore it is okay to interpret each
    component of the path as a string, unless one finds a list at the current
    level down the nested dictionary.
    '''

    def __init__(self, delim, contents=None):
        self._delim = delim

        if contents is None:
            self._parts = []
        elif isinstance(contents, list):
            self._parts = contents
        elif isinstance(contents, six.string_types):
            self._parts = self._split_string(contents)
        elif isinstance(contents, tuple):
            self._parts = list(contents)
        else:
            raise TypeError('DictPath() takes string or list, '\
                                'not %s' % type(contents))

    def __repr__(self):
        return "DictPath(%r, %r)" % (self._delim, str(self))

    def __str__(self):
        return self._delim.join(str(i) for i in self._parts)

    def __eq__(self, other):
        if not (isinstance(other, six.string_types) or
                isinstance(other, self.__class__)):
            return False
        if isinstance(other, six.string_types):
            other = DictPath(self._delim, other)
        return self._parts == other._parts and self._delim == other._delim

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self))

    @property
    def path(self):
        return self._parts

    def _get_key(self):
        if len(self._parts) == 0:
            return None
        return self._parts[-1]

    def _get_innermost_container(self, base):
        container = base
        for i in self.path[:-1]:
            if isinstance(container, (list, tuple)):
                container = container[int(i)]
            else:
                container = container[i]
        return container

    def _split_string(self, string):
        return re.split(r'(?<!\\)' + re.escape(self._delim), string)

    def key_parts(self):
        return self._parts[:-1]

    def new_subpath(self, key):
        return DictPath(self._delim, self._parts + [key])

    def get_value(self, base):
        return self._get_innermost_container(base)[self._get_key()]

    def set_value(self, base, value):
        self._get_innermost_container(base)[self._get_key()] = value

    def drop_first(self):
        del self._parts[0]
        return self

    def is_empty(self):
        return len(self._parts) == 0

    def delete(self, base):
        del self._get_innermost_container(base)[self._get_key()]

    def add_subpath(self, key):
        self._parts.append(key)

    def add_ancestor(self, key):
        self._parts.insert(0, key)

    def is_ancestor_of(self, other):
        if len(other._parts) <= len(self._parts):
            return False
        for i in range(len(self._parts)):
            if other._parts[i] != self._parts[i]:
                return False
        return True

    def exists_in(self, container):
        item = container
        for part in self._parts:
            if isinstance(item, (dict, list)):
                if part in item:
                    if isinstance(item, dict):
                        item = item[part]
                    elif isinstance(container, list):
                        item = item[int(part)]
                else:
                    return False
            else:
                if item == self._parts[-1]:
                    return True
                return False
        return True
