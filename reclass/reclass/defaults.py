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

import os, sys
from .version import RECLASS_NAME

# defaults for the command-line options
OPT_STORAGE_TYPE = 'yaml_fs'
OPT_INVENTORY_BASE_URI = os.path.join('/etc', RECLASS_NAME)
OPT_NODES_URI = 'nodes'
OPT_CLASSES_URI = 'classes'
OPT_PRETTY_PRINT = True
OPT_GROUP_ERRORS = True
OPT_COMPOSE_NODE_NAME = False
OPT_NO_REFS = False
OPT_OUTPUT = 'yaml'

OPT_IGNORE_CLASS_NOTFOUND = False
OPT_IGNORE_CLASS_NOTFOUND_REGEXP = ['.*']
OPT_IGNORE_CLASS_NOTFOUND_WARNING = True

OPT_IGNORE_OVERWRITTEN_MISSING_REFERENCES = True
OPT_STRICT_CONSTANT_PARAMETERS = True

OPT_ALLOW_SCALAR_OVER_DICT = False
OPT_ALLOW_SCALAR_OVER_LIST = False
OPT_ALLOW_LIST_OVER_SCALAR = False
OPT_ALLOW_DICT_OVER_SCALAR = False
OPT_ALLOW_NONE_OVERRIDE = False

OPT_INVENTORY_IGNORE_FAILED_NODE = False
OPT_INVENTORY_IGNORE_FAILED_RENDER = False

CONFIG_FILE_SEARCH_PATH = [os.getcwd(),
                           os.path.expanduser('~'),
                           OPT_INVENTORY_BASE_URI,
                           os.path.dirname(sys.argv[0])
                          ]
CONFIG_FILE_NAME = RECLASS_NAME + '-config.yml'

REFERENCE_SENTINELS = ('${', '}')
EXPORT_SENTINELS = ('$[', ']')
PARAMETER_INTERPOLATION_DELIMITER = ':'
PARAMETER_DICT_KEY_OVERRIDE_PREFIX = '~'
PARAMETER_DICT_KEY_CONSTANT_PREFIX = '='
ESCAPE_CHARACTER = '\\'

AUTOMATIC_RECLASS_PARAMETERS = True
DEFAULT_ENVIRONMENT = 'base'
