# A module is a file containing a set of functions to include in your application
# There are core python modules. Thus modules that you can install using the pip package manager

# Importing a Core Python Module
import datetime


today = datetime.date.today()

print(today)


# Importing a custom module

#First Way of Importing
import data

# Second Way of Importing
from data import printName

data.printName('Developer')
printName('Developer Majesty')