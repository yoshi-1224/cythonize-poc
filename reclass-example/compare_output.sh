#!/usr/bin/env bash

python use-python-reclass.py -b examples --inventory > python_out.txt
python use-cython-reclass.py -b examples --inventory > cython_out.txt

DIFF=$(diff python_out.txt cython_out.txt)
if [[ "$DIFF" == "" ]]
then
    echo "The outputs are identical. Erasing the files"
    rm python_out.txt cython_out.txt
fi

