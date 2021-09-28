# A function is a block of code that runs when called

# Create a function {To define a function in Python, we use the def keyword}


def display_details(name, profession):
    print(f'My name is {name}. I am a {profession}')


display_details('Solomon', 'Software Engineer')


# Return Values
def get_total(first_num, second_num, third_num):
    total = first_num + second_num + third_num
    return total


print(get_total(12, 5, 3))