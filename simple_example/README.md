# Simple example

This example is probably the simplest example on cythonizing a pure-python project structure. 

The project structure is as follows:

```
.
├── main.py
├── pac1
│   ├── hello.py
│   └── __init__.py
└── pac2
    ├── hola.py
    └── __init__.py
```

Where `main.py` imports `pac1.hello`, which in turn imports `pac2.hola`.

When we run it as is, the output is:

```bash
$ cd simple_example && python main.py
hello world from hello.py
hello world from hola.py
hello world from main.py
```

The objective now is to cythonize `pac1` and `pac2`. This means to compile them into `.so` files (`.pyd` on Windows) which `main.py` can then import.

Run:

`cd simple_example && ./cythonize.sh`

This will produce `.c` as well as `.so` files alongside the original `.py` files (because we specified `--inplace` option inside the script). 

Now, before we run `python main.py` again, we can temporarily rename the original python files such that we know for sure that `.so` files are imported by `main.py` and not the original `.py` files.

```
mv pac2/hola.py pac2/hola_temp.py
mv pac1/hello.py pac1/hello_temp.py
```

Finally, the output would be:

```bash
$ cd simple_example && python main.py
hello world from hello.cpython-36m-x86_64-linux-gnu.so
hello world from hola.cpython-36m-x86_64-linux-gnu.so
hello world from main.py
```

These file names confirm that we are indeed importing the `.so` files. Note that the name of the `.so` files will be different according to your platform (but you can still import them using the original package name). And again, if you are on Windows, convert bash commands into batch commands as well as replace `.so` by `.pyd`.

Note that the reason why `main.py` can still identify the packages successfully (e.g. as in `from pac1.hello import *`) is because we have `__init__.py` in each package folder. Even after cythonizing, you will still need these files, and they have to be `.py` extension. Therefore, DO NOT cythonize `__init__.py` files.