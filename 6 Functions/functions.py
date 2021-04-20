# A function is a block of code that runs when called

# Create a function {To define a function in Python, we use the def keyword}
def displayDetais(name, proffession):
    print(f'My name is {name}. I am a {proffession}')

displayDetais('Solomon', 'Software Engineer')

# Return Values
def getTotal(firstNum, secondNum, thirdNum):
    sum = firstNum + secondNum + thirdNum
    return sum

print(getTotal(12, 5, 3))