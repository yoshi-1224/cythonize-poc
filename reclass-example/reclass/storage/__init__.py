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

from reclass.storage.common import NameMangler

class NodeStorageBase(object):

    def __init__(self, name):
        self._name = name

    name = property(lambda self: self._name)

    def get_node(self, name, settings):
        msg = "Storage class '{0}' does not implement node entity retrieval."
        raise NotImplementedError(msg.format(self.name))

    def get_class(self, name, environment, settings):
        msg = "Storage class '{0}' does not implement class entity retrieval."
        raise NotImplementedError(msg.format(self.name))

    def enumerate_nodes(self):
        msg = "Storage class '{0}' does not implement node enumeration."
        raise NotImplementedError(msg.format(self.name))

    def path_mangler(self):
        msg = "Storage class '{0}' does not implement path_mangler."
        raise NotImplementedError(msg.format(self.name))


class ExternalNodeStorageBase(NodeStorageBase):

    def __init__(self, name, compose_node_name):
        super(ExternalNodeStorageBase, self).__init__(name)
        self.class_name_mangler = NameMangler.classes
        if compose_node_name:
            self.node_name_mangler = NameMangler.composed_nodes
        else:
            self.node_name_mangler = NameMangler.nodes
