path = input("Please enter the path to a text file: ")
with open(path) as my_file:
	print(my_file.read())
