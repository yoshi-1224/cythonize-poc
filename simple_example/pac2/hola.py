from pac1.hello import hello_world
from os import path

# the print statement from cython prints some tuples
def hello_world2():
    hello_world()
    print('hello world from {}'.format(path.basename(__file__)))
