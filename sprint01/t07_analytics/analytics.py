def print_str_analytics(string_for_analytics):
    printable = alphabet = decimal = lower = upper = white = 0
    for ch in string_for_analytics:
        if ch.isprintable():
            printable += 1
        if ch.isalpha():
            alphabet += 1
        if ch.isdigit():
            decimal += 1
        if ch.islower():
            lower += 1
        if ch.upper():
            upper += 1
        if ch.isspace():
            white += 1

    output = '|' + '-' * 48 + '|'

    print(f'{output}\n'
          f'|' + ' ' * 16 + 'String analytics' + ' ' * 16 + '|\n'
          f'{output}\n'
          f"| '{string_for_analytics}'\n"
          f'{output}\n'
          f'| Number of printable characters is: {printable}\n'
          f'| Number of alphanumeric characters is: {alphabet + decimal}\n'
          f'| Number of alphabetic characters is: {alphabet}\n'
          f'| Number of decimal characters is: {decimal}\n'
          f'| Number of lowercase letters is: {lower}\n'
          f'| Number of uppercase letters is: {upper}\n'
          f'| Number of whitespace characters is: {white}\n'
          f'{output}')
