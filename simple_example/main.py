"""
this is just a script that imports pac2 which ultimately imports pac1
"""

from pac2.hola import hello_world2


def use_imports():
    hello_world2()
    print('hello world from {}'.format(__file__))


if __name__ == '__main__':
    use_imports()
