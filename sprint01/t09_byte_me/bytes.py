def convert_to_bytes(arg_int, arg_bool, arg_str):
    print(f'-- The int value is {arg_int}\n'
          f'bytes: "{bytes(int(arg_int))}"')
    print(f'-- The bool value is {arg_bool}\n'
          f'bytes: "{bytes(bool(arg_bool))}"')
    print(f'-- The string value is {arg_str}\n'
          f'bytes: "{bytes(arg_str, "utf-8")}"')


convert_to_bytes('10', 'False', 'aaaa')
convert_to_bytes('5', 'True', 'Are you suggesting that coconuts migrate?')
convert_to_bytes('1', 'true', 'bbb')
