repository = open('words.txt')
counter = 0
for word in repository:
    if len(word) >= 2 and word[0] == word[-2]:
        counter += 1
print(f'The total number of words that met the criteria are: {counter}')
