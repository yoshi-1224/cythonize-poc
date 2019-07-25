from distutils.core import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext

setup(
    name = "cythonize_before_pyinstaller",
    build_dir = "build",
    # ext_modules = cythonize(['pac1/hello.py', 'pac2/hola.py']),
)

# python setup.py build_ext --inplace

# you either use Extension to dictate where your .so is going to end up, or
#
# pyd on windows, .so on nix