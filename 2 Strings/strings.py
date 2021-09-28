# Strings are traditionaly a sequence of characters

# Below are some string formatting and method

myName = 'Developer Majesty'
name = "majesty"
sentence = "The boy is very foolish"
workPlace = 'Maverick Edifice Limited'


# Concatenate
print('Hello there, My name is ' + myName + '. I am a Software Engineer at ' + workPlace + '.')

# Arguments by position
print('Hello there, My name is {myName} I am a Software Engineer at {workPlace}.'.format(myName=myName, workPlace=workPlace))

# F-String (This is only available in python 3.6)
print(f'Hello there, My name is {myName} I am a Software Engineer at {workPlace}.')


# Python String Methods

print(name.capitalize())                                    # It capitalizes a String

print(name.upper())                                         # It coverts a string to uppercase

print(name.lower())                                         # It coverts a string to lowercase

print(name.isalpha())                                       # It checks to see whether a string is made up of alphapbets or not. If yes, it prints true, if no it prints false

print(name.isdigit())                                       # It checks to see whether a string is made up of digits or not. If yes, it prints true, if no it prints false

print(name.replace('majesty', 'Chief Programmer'))      # It replaces the first(old) String with the second(new) String.

print(sentence.replace("foolish" , "f**lish"))

comment = input('type a comment: ')

