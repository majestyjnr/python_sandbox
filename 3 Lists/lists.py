# A list is a versatlie data type used to store a collection of simalr data items.

# Creating a List
numbers = [1, 2, 3, 4, 5, 6]
countries = ['Ghana', 'USA', 'India', 'France', 'Nigeria', 'Belgium', 'Norepublic', 'China']

# Getting the length of a list
print(len(countries))

# Appends to a list
print(countries.append('Canada'))

# Removes from a list
print(countries.remove('Norepublic'))

# changing a value
countries[6] = 'NULLRepublic'

# Inserts into a list
print(countries.insert(2, 'Israel'))

# Reverses a list
print(countries.reverse())

# Sorting list according to alphabetical order
print(countries.sort())

print(numbers)         
print(countries)                                # printing the numbers List
print(countries[0] + ' is my country')          # printing out the first country in the list