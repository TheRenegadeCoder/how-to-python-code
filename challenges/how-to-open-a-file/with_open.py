path = input("Please enter the path to a text file: ")
with open(path, 'r') as my_file: # 'r' means we are opening the file in read mode
	print(my_file.read())

# Few other modes:
# 'w' : We will open the the file in "write" mode. It will rewrite the previously written data.
# 'a' : We will open the file in "append" mode. By this, we will write the data at the end of the file without rewriting.
