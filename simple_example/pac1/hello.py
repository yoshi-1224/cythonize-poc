from os import path


def hello_world():
	print("hello world from {}".format(path.basename(__file__)))
