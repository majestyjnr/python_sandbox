# A loop iterates over a sequence

# While loops executes a set of statements as long as the condition is true

names = ['Solomon', 'Prince', 'Henry', 'Daniel', 'Samuel', 'Charles', 'Dog', 'Tiger', 'Leopard']

# Simple For Loop

for person in names:
    print(f'Current Person is:  {person}')

# Break
for person in names:
    if person == 'Dog':
        break
    print(f'Current Person is:  {person}')

# Continue
for person in names:
    if person == 'Dog':
        continue
    print(f'Current Person is:  {person}')

# Range
for index in range(len(names)):
    print(names[index])


# While Loop

counter = 0

while counter <= 10:
    print(f'Users visiting the site: {counter}')
    counter += 1
