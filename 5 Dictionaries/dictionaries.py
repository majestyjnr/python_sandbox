# A dictionary is a collection which is unordered, changeable and indexed. No duplicate is allowed

# Creating a dictionary
staff = {
    'name': 'Developer Majesty',
    'proffession': 'Software Engineer',
    'company': 'Maverick Edifice Limited',
}

# Get Value
print(staff['name']) 
print(staff.get('company'))

# Get Keys
print(staff.keys())

# Get Dictionary items
print(staff.items())

# Add Key/Value
staff['email'] = 'developermajesty@gmail.com'

# Copy dictionary and assign it
staff1 = staff.copy()

# Get length of a dictionary
print(len(staff))

# Print Entire Dictionary
print(staff)  