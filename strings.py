# Strings are traditionaly a sequence of characters

# Below are some string formatting and method

myName = 'Developer Majesty'
workPlace = 'Maverick Edifice Limited'
name= 'king'

# Concatenate
print('Hello there, My name is ' + myName + '. I am a Software Engineer at ' + workPlace + '.' )

# Arguments by position
print('Hello there, My name is {myName} I am a Software Engineer at {workPlace}.'.format(myName=myName, workPlace=workPlace))

# F-String (This is only available in python 3.6)
print(f'Hello there, My name is {myName} I am a Software Engineer at {workPlace}.')


# Python String Methods
print(name.capitalize())                                    

print(name.upper())                                         

print(name.lower())                                            

print(name.isalpha())                                       

print(name.isdigit())                                       

print(myName.replace('Developer', 'Chief Programmer'))      

