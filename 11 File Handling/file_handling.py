# There are four different methods (modes) for opening a file:
#
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists

# To Open a File
# To open a file, we use the built-in open() function.
# The open() function takes two parameters; filename, and mode

f = open("test.txt")

# To read a File
# The read() method is used for reading the content of the file
# print(f.read())

# To loop through the file line by line:
# for x in f:
#     print(x)

# To read line
# You can return one line by using the readline() method:
# print(f.readline())


# ============================ Writing to an existing file =============================================

# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# TO APPEND TO A FILE
f = open("test.txt", "a")
f.write("I have a vision!")

# TO OVERWRITE AN EXISTING FILE
# f = open("test.txt", "w")
# f.write("Damn it! I just deleted my bio!")







