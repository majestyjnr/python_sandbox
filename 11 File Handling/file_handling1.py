# Question 1
from datetime import datetime

repository = open('date_file.txt')

dictionary = {}
for date in repository:
    stripped_date = date.strip()
    x = datetime.strptime(stripped_date, '%d-%b-%y')
    (key) = stripped_date
    (val) = x.strftime('%m-%d-%Y')
    dictionary[key] = val

print(dictionary)
