def contains(all_string, substrings):
    result = list()
    all_string = str.lower(all_string)
    for item in substrings:
        subline = str.lower(item)
        if all_string.find(subline) != -1:
            result.append(subline)

    return result
