example = 'my name is solomon'
example2 = 'MY NAME IS SOLOMON'
number = '0505954432'
trimmer ='We know you '


# capitalize()	    Converts the first character to upper case
print(example.capitalize())


# casefold()	    Converts string into lower case
print(example2.casefold())

test = 'solomon'
# center()	        Returns a centered string
data = test.center(30, 'e')     # Prints the word Solomon taking up 30 characters with Solomon in the center/middle
print(data)

# count()	        Returns the number of times a specified value occurs in a string
print(example.count('m'))

# encode()	        Returns an encoded version of the string
print(example.encode())


# endswith()	    Returns true if the string ends with the specified value
print(example.endswith('n'))
print(example.endswith('e'))

# find()	        Searches the string for a specified value and returns the position of where it was found
print(example.find('s'))

tester = 'My name is {} '
# format()	        Formats specified values in a string
print(tester.format("Solomon Aidoo Jnr"))

# index()	        Searches the string for a specified value and returns the position of where it was found
print(example.index('a'))

# isalnum()	        Returns True if all characters in the string are alphanumeric
print(example.isalnum())

text = 'yes'
# isalpha()	        Returns True if all characters in the string are in the alphabet
print(text.isalpha())

text = 'yes'
# isdecimal()	    Returns True if all characters in the string are decimals
print(text.isdecimal())


# isdigit()	        Returns True if all characters in the string are digits
print(example.isdigit())

# isidentifier()	Returns True if the string is an identifier
print(example.isidentifier())

# islower()	        Returns True if all characters in the string are lower case
print(example2.islower())


# isnumeric()	    Returns True if all characters in the string are numeric
print(number.isnumeric())

# isprintable()	    Returns True if all characters in the string are printable
print(example2.isprintable())

# isspace()	        Returns True if all characters in the string are whitespaces
print(example.isspace())

# istitle()	        Returns True if the string follows the rules of a title
print(example.istitle())

# isupper()	        Returns True if all characters in the string are upper case
print(example2.isupper())

# join()	        Joins the elements of an iterable to the end of the string || Join all items in a tuple into a string, using a hash tag as separator:
names = ('Solomon', 'Aidoo', 'Junior')
new = ' '.join(names)
print(new)


# ljust()	        Returns a left justified version of the string || Returns a 20 characters long, left justified version of the word "banana":
view = test.ljust(20)
print(view, 'Yes')

# lower()	        Converts a string into lower case
print(tester.lower())

# replace()	        Returns a string where a specified value is replaced with a specified value
replacer = 'The guy is foolish'
new = replacer.replace("foolish", "f**lish")
print(new)


# rfind()	        Searches the string for a specified value and returns the last position of where it was found
data1 = example.rfind("name")
print(data1)

# rindex()	        Searches the string for a specified value and returns the last position of where it was found
data1 = example.rindex("name")
print(data1)

# rsplit()	        Splits the string at the specified separator, and returns a list
text = "Python, JavaScript, Java, C++"
new = text.rsplit(", ")
print(new)


# rstrip()	        Returns a right trim version of the string
text = "     abigail     "
x = text.rstrip()
print("I'll give it to", x, "today")


# split()	        Splits the string at the specified separator, and returns a list
x = example.split()
print(x)

# splitlines()	    Splits the string at line breaks and returns a list
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

# startswith()	    Returns true if the string starts with the specified value
print(example.startswith('m'))


# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
print(example.swapcase())
print(example2.swapcase())


# title()	        Converts the first character of each word to upper case
print(example2.title())

# upper()	        Converts a string into upper case
print(example.upper())


# zfill()	        Fills the string with a specified number of 0 values at the beginning
text = "50"
x = text.zfill(10)
print(x)

