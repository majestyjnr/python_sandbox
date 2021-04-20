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

# Add Key/Value
staff['email'] = 'developermajesty@gmail.com'


# Print Entire Dictionary
print(staff)  