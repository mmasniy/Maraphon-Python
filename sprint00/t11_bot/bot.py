if __name__ == '__main__':
    first = input('Enter your first string: ')
    second = input('Enter your second string: ')

    if (not first.strip() and not second.strip()) or not first.strip() or not second.strip():
        print('One of the strings is empty.')
    else:
        command = input('Enter your command: ')

        if command == 'find':
            if second in first:
                print('True')
            else:
                print('False')
        elif command == 'concat':
            print('Your string is: ' + first + ' ' + second)
        elif command == 'beatbox':
            try:
                a = int(input('Enter your first beatbox number: '))
                b = int(input('Enter your second beatbox number: '))
                print(first * a + second * b)
            except:
                print("usage: first and second beatbox numbers must be integer or float, but string")
        else:
            print('usage: command find | concat | beatbox')