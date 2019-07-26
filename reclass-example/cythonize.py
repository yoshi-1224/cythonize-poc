import os
from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext
from Cython.Build import cythonize
import Cython.Compiler.Options
Cython.Compiler.Options.docstrings = False

build_folder = "build"


# this is required since if we only do cythonize([*.pyx]) it would only
# compile files in the current directory
# we therefore need to explicitly pass in all the .pyx files that we want to compile
def find_all_pyx_files(dir, files=[]):
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if os.path.isfile(path) and path.endswith(".pyx"):
            files.append(path.replace(os.path.sep, ".")[:-4])
        elif os.path.isdir(path):
            find_all_pyx_files(path, files)
    return files


# generate an Extension object from its dotted name
def make_extension_objs(ext_name):
    ext_name = ext_name.replace(".", os.path.sep) + ".pyx"
    # this for example converts package stored at pac1/utils to
    # Extension('pac1.utils', 'pac1/utils')
    return Extension(ext_name, [ext_name],
                     extra_link_args=['-Wl,--strip-all']
                     )


# get the list of extensions
extNames = find_all_pyx_files(build_folder)

# and build up the set of Extension objects
extensions = [make_extension_objs(name) for name in extNames]

# finally, we can pass all this to distutils
setup(
  name="cythonise",
  ext_modules=cythonize(extensions),
  cmdclass={'build_ext': build_ext},
)