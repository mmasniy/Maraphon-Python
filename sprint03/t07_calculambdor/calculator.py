operations = dict({
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "div": lambda a, b: a / b,
    "mul": lambda a, b: a * b,
    "pow": lambda a, b: a ** b
})


def calculator(name, a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError('Invalid numbers. Second and third arguments must be numerical.')
    if name not in operations.keys():
        raise ValueError('Invalid operation. Available operations: add, sub, mul, div, pow.')
    return operations.get(name)(a, b)


# print(calculator("add", 1, 2))
# print(calculator("sub", 1, 2))
# print(calculator("div", 1, 2))
# print(calculator("mul", 1, 2))
# print(calculator("pow", 1, 2))
# try:
#     print(calculator("ad", 1, 2))
# except ValueError:
#     print("Good")
#
#     try:
#         print(calculator("add", "1", 2))
#     except ValueError:
#         print("Good")