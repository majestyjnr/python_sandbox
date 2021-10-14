def digit_summer(the_string):
    total = 0
    for char in the_string:
        if char.isdigit():
            the_char = int(char)
            total += the_char

    return total


the_string = '121abc4d5e6'


print(digit_summer(the_string))
