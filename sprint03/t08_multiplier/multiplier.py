from functools import reduce


def multiplier(list_numbers):
    if not any(isinstance(i, (int, float)) for i in list_numbers)\
            or not isinstance(list_numbers, list):
        raise ValueError("The given data is invalid.")
    return reduce(lambda a, b: a * b, list_numbers)