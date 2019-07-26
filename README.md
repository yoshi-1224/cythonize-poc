# Sample cythonize project

## Overview

This project demonstrates how to Cythonize pure python projects for faster runtime. No editing of the code is required (although if you do, you will most likely enjoy better performance).

## Motivation

If you want to create a standalone executable using PyInstaller and likes, then it makes sense to cythonize some of your codebase and compile them into `.so` files for faster speed.

## Drawbacks

Cythonizing the scripts will most likely make the file size larger (no pain, no gain). It is therefore recommended to only cythonize a selective portion of the code where performance gains are meaningful.


## References
- https://github.com/cython/cython/wiki/PackageHierarchy
- https://bucharjan.cz/blog/using-cython-to-protect-a-python-codebase.html