import os
from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext
from Cython.Build import cythonize

# scan the 'dvedit' directory for extension files, converting
# them to extension names in dotted notation
def scandir(dir, files=[]):
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if os.path.isfile(path) and path.endswith(".pyx"):
            files.append(path.replace(os.path.sep, ".")[:-4])
        elif os.path.isdir(path):
            scandir(path, files)
    return files


# generate an Extension object from its dotted name
def makeExtension(extName):
    extPath = extName.replace(".", os.path.sep)+".pyx"
    return Extension(
        extName,
        [extPath],
        # include_dirs = [libdvIncludeDir, "."],   # adding the '.' to include_dirs is CRUCIAL!!
        # extra_compile_args = ["-O3", "-Wall"],
        # extra_link_args = ['-g'],
        # libraries = ["dv",],
        )

# get the list of extensions
extNames = scandir("build")

# and build up the set of Extension objects
extensions = [makeExtension(name) for name in extNames]

# finally, we can pass all this to distutils
setup(
  name="dvedit",
  packages=["dvedit", "dvedit.filters"],
  ext_modules=cythonize(extensions),
  cmdclass = {'build_ext': build_ext},
)