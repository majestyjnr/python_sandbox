# There are four different methods (modes) for opening a file:
#
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists

# ================================ To Open a File ===================================
# To open a file, we use the built-in open() function.
# The open() function takes two parameters; filename, and mode

# f = open("test.txt")

# ================================ To read a File ===================================
# The read() method is used for reading the content of the file
# print(f.read())

# To loop through the file line by line:
# for x in f:
#     print(x)

# ================================= To read line ======================================
# You can return one line by using the readline() method:

# print(f.readline())


# ================================= Writing to an existing file ====================================

# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# =================================== TO APPEND TO A FILE ===========================================
# f = open("number.txt", 'a')
# f.write("10\n15\n17\n18\n19")
# count = 0
# sum = 0
#
# for x in f:
#     if x.isdigit():
#         print()
#     else:
#        new_number = int(x)
#        count += 1
#        sum = sum + new_number
#
#
# print(sum/count)

# =================================== TO OVERWRITE AN EXISTING FILE ==================================
# f = open("number.txt", "w")
# f.write("This will overwrite the data")


# ================================ Creating a New File ================================================
# # To create a new file in Python, use the open() method, with one of the following parameters:
#
# # "x" - Create - will create a file, returns an error if the file exist
# # "a" - Append - will create a file if the specified file does not exist
# # "w" - Write - will create a file if the specified file does not exist
#
# f = open("majesty.txt", "x")
# f = open("majesty.txt", "a")
# f.write('This is a new file')
# # f = open("majesty.txt", "w")
#
# # f.write('This is developer majesty')


# =============================== Deleting a file =======================================================
import os
# os.remove("majesty.txt")

# To remove a folder

# os.mkdir('Abigail')
# os.rmdir("folder")

