# A tuple is a collection that is ordered and unchangeable

# Creating a tuple
countries = ('Ghana', 'USA', 'India', 'France', 'Nigeria', 'India', 'Belgium', 'Norepublic', 'China')

num = 100
print(countries[0])         # Get a value
print(countries)            # Prints the tuple countries
print(type(num))
print(type(countries))      # Prints the type of countries
print(len(countries))       # Prints the length of the tuple countries


# A set is a collection that is unordered or unindexed. No duplicate is allowed

# Creating a SET
countriesSet = {'Ghana', 'USA', 'India', 'France', 'Nigeria', 'Belgium', 'Norepublic', 'China'}

print(countriesSet)

print('USA' in countries)   # Check if in set. Display True if found, false in not found
