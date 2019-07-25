#!/usr/bin/env bash

cp -r reclass build

cd build
# step1 : convert all the .py files to .pyx
find . -name "*.py" -exec bash -c 'mv "$1" "${1%.py}".pyx' - '{}' \;
# step2: rename __init__.pyx to __init__.py since Python needs to recognise as packages
find . -name "*__init__.pyx" -exec bash -c 'mv "$1" "${1%.pyx}".py' - '{}' \;
cd ..

# step3: cythonize, generating .so and .c files in place
python cythonize.py build_ext --inplace
# step4: remove all the .c and .pyx files as they are no longer necessary
cd build && find . -name "*.pyx" -type f -delete && find . -name "*.c" -type f -delete
