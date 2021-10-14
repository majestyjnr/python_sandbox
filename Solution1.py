
character = input('Please enter the word to be examined: ')

distinct_letters = []

for letter in character:
    if letter not in distinct_letters:
        distinct_letters += [letter]
        print(f"There are {character.count(letter)} {letter}'s in  {character}")


