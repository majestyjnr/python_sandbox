# Question 3

repository = open('lines_file.txt')

# Create an empty list to receive all new data
my_list = []


def reverse_line(file):
    for line in repository:
        # Append all lines with text into the list but exclude lines with no text
        my_list.append(line.strip())

        # =========== The process of Reversing the list and also returning all the elements in it =============
        # In order to grab the entire elements of the list, I omitted the start and the end arguments
        # By setting the STEP argument to a negative number, I was able to iterate through the collection in a reversed state

        # my_list[start: end: step]
        reversed_list = my_list[::-1]

    # Only return the list when the for loop has been completed in order to grab just the final list
    return reversed_list


print(reverse_line(repository))


