'''
If/Else conditions are used to determine whether something is true or false
Comparison Operators are normally used. They are (==, !=, >, <, >=, <= )
'''

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