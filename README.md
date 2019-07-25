# Sample cythonize project

## Overview

This project demonstrates how to Cythonize pure python projects for faster runtime. No editing of the code is required (although if you do, you will most likely enjoy better performance).

## Motivation

If you want to create a standalone executable using PyInstaller and likes, then it makes sense to cythonize your codebase and compile them into `.so` files.

This is not a real Python project: it tries to just mirror a typical package file structure (with import statements, multiple dependencies i.e. importing a file that imports another file) so that when we apply this to the actual project, we get the idea of how Cython-compiled code behaves.

