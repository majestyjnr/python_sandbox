# A Variable is anything that represents a value

'''
RULES
Variabes are case sensitive (isRead and ISREAD are different values altogether)
Variables can have a number but must not start with a number eg: name1 is valid, but 1name is invalid
'''

name = 'Developer Majesty'  # String
x = 2                       # Int
y = 2.5                     # Float
isRead = True               # Boolean

# Multiple Assignments
newName, a, b, isSeen = ('Champion Majesty', 100, 3.5, False)

# Casting
z = str(2)

print(type(z))              # prints the type of the variable z
print(name)                 # prints the variable name
print(newName, isSeen)