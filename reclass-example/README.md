# Reclass example overview

It works mostly in the same way as simple-example. Simply run:

```
./cythonize.sh
```

This will create a folder named "build" whose structure is exactly the same as "reclass" folder, except all the python files are compiled into `.so` files. We can then use this as a package, exactly in the same way as "reclass" package (except you need to import as "build" rather than "reclass" due to the name of the folder). For example, have a look at `use-cython-reclass.py`.

Read through the comments in `cythonize.py` and `cythonize.sh` how the cythonizing is done.

Reclass (https://github.com/salt-formulas/reclass.git) was chosen only because it was relevant to a project I am working on. We should be able to apply the same principle to any project.

## Changes made to reclass source

Due to compile error raised by unresolved variable in `reclass/core.py`, I removed the if statement concerned.

## Comparing the output
 In order to compare the output of pure-python reclass and cython-compiled reclass, run:
 
 ```bash
 ./compare_output.sh
 ```
