import re

regex_str = r"(\AUkraine)([ ]*,[ ]*)([a-zA-Z]+[ -]*[a-zA-Z]*)([ ]*,[ ]*)([a-zA-Z]+[ -]*[a-zA-Z]*)( )([0-9]{1,6})([ ]*,[ ]*)([0-9]{5})"


def check_address(dictionary):
    result = list()
    for key, value in dictionary.items():
        match = re.findall(regex_str, value)
        if len(match) > 0:
            result.append(f"The address of {key} is valid.")
        else:
            result.append(f"The address of {key} is invalid.")
    return result
