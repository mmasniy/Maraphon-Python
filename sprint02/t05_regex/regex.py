import re

regex_str = r"(^Ukraine,)([a-zA-Z-\s])+,([a-zA-Z-\s])+\d{1,6},\s*\d{5}$"


def check_address(dictionary):
    result = list()
    for key, value in dictionary.items():
        match = re.findall(regex_str, value)
        if len(match) > 0:
            result.append(f"The address of {key} is valid.")
        else:
            result.append(f"The address of {key} is invalid.")
    return result
