# Question 2
repository = open('lines_file.txt')
alphabet = "abcdefghijklmnopqrstuvwxyz"


def checker(str):
    letter = str[0] + str[-1]

    first_index = alphabet.find(str[0])
    second_index = alphabet.find(str[-1])

    if (first_index + 1) == second_index:
        print(True)
        print(letter)
    elif(second_index == 0) and first_index == 25:
        print(True)
        print(letter)


# Read every line in the opened file
for line in repository:
    # Split the line into words
    for word in line.split():
        # only work on words whose length are greater than 2
        if len(word) > 2:
            # convert word to lowercase
            lower_cased_word = word.lower()
            # call function and pass the lower cased word as string
            checker(lower_cased_word)


