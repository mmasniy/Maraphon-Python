def contains(all_string, substrings):
    result = list()
    all_string = str.lower(all_string)
    for item in substrings:
        sub_line = str.lower(item)
        if all_string.find(sub_line) != -1:
            result.append(item)

    return result
