def replace_operator(arg1, arg2, operator):
    if arg1 == arg2:
        return str(arg1) + ' == ' + str(arg2)
    if operator == '==':
        if arg1 >= arg2:
            return str(arg1) + ' >= ' + str(arg2)
        else:
            return str(arg1) + ' <= ' + str(arg2)
    elif operator == '>':
        return str(arg1) + ' < ' + str(arg2)
    elif operator == '<':
        return str(arg1) + ' > ' + str(arg2)
    elif operator == '<=':
        return str(arg1) + ' >= ' + str(arg2)
    elif operator == '>=':
        return str(arg1) + ' <= ' + str(arg2)


def validator(expression):
    arguments = expression.split()
    try:
        arg1 = float(arguments[0])
        arg2 = float(arguments[2])
        if arguments[1] not in ['>', '<', '>=', '<=', '==']:
            raise ValueError
    except (ValueError, IndexError):
        return False
    else:
        if eval(expression):
            return True
        else:
            return replace_operator(arg1, arg2, arguments[1])


"""
if __name__ == "__main__":
    print(validator('4 < 6'))
    print(validator('4 > 6'))
    print(validator('4 > '))
    print(validator('4  6'))
    print(validator('4 . 6'))
    print(validator('4 == 6'))
    print(validator('4 >= 6'))
    print(validator('4 > 4'))
"""
