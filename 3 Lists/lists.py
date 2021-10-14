# A list is a versatlie data type used to store a collection of similar data items.

# Creating a List
numbers = [1, 2, 3, 4, 5, 6]
countries = ['Ghana', 'USA', 'India', 'France', 'Nigeria', 'Belgium', 'Norepublic', 'China']


# Getting the length of a list
print(len(countries))

# Appends to a list
countries.append('Canada')
print(countries)

# Removes from a list
print(countries.remove('Norepublic'))
print(countries)

# changing a value
countries[6] = 'NULLRepublic'
print(countries)

# Inserts into a list
countries.insert(2, 'Israel')
print(countries)

# Reverses a list
countries.reverse()
print(countries)

# Sorting list according to alphabetical order
countries.sort()
print(countries)

# print(numbers)
# print(countries)                                # printing the numbers List
print(countries[0] + ' is my country')            # printing out the first country in the list
