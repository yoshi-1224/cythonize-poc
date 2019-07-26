# Reclass example overview

It works mostly in the same way as simple-example. Read through the comments in `cythonize.py` and `cythonize.sh` for the differences. 

Reclass (https://github.com/salt-formulas/reclass.git) was only chosen as it was relevant to my project.

## Changes made to reclass source

Due to compile error raised by unresolved variable in `reclass/core.py`, I removed the if statement concerned.

## Comparing the output
 In order to compare the output of pure-python reclass and cython-compiled reclass, run:
 
 ```bash
 ./compare_output.sh
 ```