print('---- Simple calculator ----')
print("Let's add some numbers")
a = input('Input your first value: ')
b = input('Input your operator: ')
if b not in '+-*/':
    print("usage: the operator must be '*' or '+' or '-' or '/'")
    print('---- Simple calculator ----')
    quit()
else:
    c = input('Input your second value: ')
    # try:
    a = int(a)
    c = int(c)
    # except:
    #     print("usage: this script sequentially reads two integer, but not string")
    #     print('---- Simple calculator ----')
    #     exit()
    d = int()
    if b == '+':
        d = a + c
    elif b == '-':
        d = a - c
    elif b == '*':
        d = a * c
    elif b == '/':
        d = a / c
    print(f'{a} {b} {c} = {d}')
    print('---- Simple calculator ----')
