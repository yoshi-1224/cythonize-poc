#!/usr/bin/env bash

python cython_setup.py build_ext --inplace

# --inplace will basically put the .so files where the .py files are