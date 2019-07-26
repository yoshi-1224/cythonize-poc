from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


# build will not be recognized as valid package to some IDEs like pycharm
# without proper configuration
import build.cli
build.cli.main()
