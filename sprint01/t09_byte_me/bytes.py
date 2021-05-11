def convert_to_bytes(arg_int, arg_bool, arg_str):
    arg2_bool = (False, True)["True" == arg_bool]
    print(f'-- The int value is "{arg_int}"\n'
          f'bytes: "{bytes(int(arg_int))}"')
    print(f'-- The bool value is "{arg_bool}"\n'
          f'bytes: "{bytes(arg2_bool)}"')
    print(f'-- The string value is "{arg_str}"\n'
          f'bytes: "{bytes(arg_str, "utf-8")}"')
