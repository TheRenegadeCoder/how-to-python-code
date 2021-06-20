"""
Provides a series of solutions to the challenge provided at the following link:
https://therenegadecoder.com/code/how-to-open-a-file-in-python/#challenge
"""


def cat_1(path: str):
	with open(path, 'r') as my_file:
		return my_file.read()
