# Question 1
from datetime import datetime

repository = open('date_file.txt')

# Initialize an empty dictionary
dictionary = {}

for date in repository:
    # clear whitespaces from dates in file
    stripped_date = date.strip()
    # the strptime can be used to convert a string to a datetime object (Note: the dates from the file are strings)
    # strptime accepts(theString, theDateObject)
    # %d = The day of the month
    # %b = The month in an abbreviated format
    # %y = Year without the century
    x = datetime.strptime(stripped_date, '%d-%b-%y')

    # NB: The key of our dictionary is going to be the old format from the file
    key = stripped_date

    # NB: The value of the key is going to be the new required date format
    # the strftime is used for formatting date and time (We therefore need the date in this format : ('%m-%d-%Y'))
    # where
    # %m = the month
    # %b = the day of the month
    # %Y = Year with the century
    val = x.strftime('%m-%d-%Y')

    # Add each iteration into the dictionary
    # Refer to line 27 the dictionary folder I sent you to have a fair idea of how to add an item to a dictionary
    dictionary[key] = val


print(dictionary)
