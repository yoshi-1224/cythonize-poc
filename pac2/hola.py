from pac1.hello import hello_world

# the print statement from cython prints some tuples
def hello_world2():
    hello_world()
    print ('hello world 2: {}'.format(__file__))
