
# def get_operand(stack):
#     #
#     return stack.pop(), stack.pop()
#
#
# def addition(stack):
#     x, y = get_operand(stack)
#     stack.append(x + y)
#
#
# def subtraction(stack):
#     x, y = get_operand(stack)
#     stack.append(x - y)
#
#
# def multiplication(stack):
#     x, y = get_operand(stack)
#     stack.append(x * y)
#
#
# def division(stack):
#     x, y = get_operand(stack)
#     stack.append(x / y)
#
#
# operators = {
#     "+": addition,
#     "-": subtraction,
#     "*": multiplication,
#     "/": division
#     # addition : "+" ,
#     # subtraction : "-",
#     # multiplication: "*",
#     # division: "/"
# }
#
# stack, values = [], input('Type your expression here:\t').strip().split()
#
# for value in values:
#     if value in operators:
#         operators[value](stack)
#     else:
#         stack.append(float(value))
#
# print(stack[0])

# 30 1 - 9 + 2*


operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x - y
}


def calculate(input):
    # splits the input into tokens
    tokens = input.split()
    # print(tokens)
    stack = []


    for token in tokens:
        # print(token)
        # print(stack)
        if token in operators:

            # The pop method removes the item from the list and returns it
            arg2 = stack.pop()
            arg1 = stack.pop()
            # print(arg1)
            # print('Pause')
            # print(arg2)

            # The token here is the operator in context.
            # The argument1 and argument2 are the being operated on
            result = operators[token](arg1, arg2)  # arg1 = x , arg2 = y
            stack.append(result)

        else:
            stack.append(int(token))

    return ''.join(map(str, stack))


print(calculate('30 1 - 9 + 2 *'))


