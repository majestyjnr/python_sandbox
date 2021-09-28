""""
If/Else conditions are used to determine whether something is true or false
Comparison Operators can be used. They are (==, !=, >, <, >=, <= )
Logical Operators can be used. They are (and, or, not)
Membership Operators can be used. They are (not, not in)

NB: f(Formatted String literal) It embeds expressions into string literals
"""

a = 10
b = 20

# If Statement
if(b > a):
    print(f'{b} is greater than {a}')

# If/Else Statement
if(a == b):
    print(f'{a} is equal to {b}')
else:
    print(f'{a} is not equal to {b}')

# elif
if(a == b):
    print(f'{a} is equal to {b}')
elif(a > b):
    print(f'{a} is greater than {b}')
elif(b > a):
    print(f'{b} is greater than {a}')

# Nested If
if(b > a):
    if(b <= 50):
       print(f'{b} is greater than {a} and less than or equal to 50')


# Using the Logical Operators


# Using the 'and' operator, both conditions have to be truetement to run for the conditional sta
if(b > a and b <= 50):
    print(f'{b} is greater than {a} and less than or equal to 50')

# Using the 'or' operator, just one of the conditions ahve to run for this to be true
if(b > a or b <= 50):
    print(f'{b} is greater than {a} or less than or equal to 50')

# not or !
if not(a == b):
    print(f'{a} is not equal to {b}')


# Using the Membership Operator


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# In
if(a in numbers):
    print(f'{a} can be found in numbers')

# Not in
if(b not in numbers):
    print(f'{b} cannot be found in numbers')