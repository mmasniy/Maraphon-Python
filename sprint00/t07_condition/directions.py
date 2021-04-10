inputUsers = input("There are 3 signs in front of you. Which one would you like to read? ")

if inputUsers == 'right':
    print('The right sign says: "DEAD PEOPLE ONLY"')
elif inputUsers == 'left':
    print('The left sign says: "BEWARE!"')
elif inputUsers == 'middle':
    print('The middle sign says: "CERTAIN DEATH"')
else:
    print(f'There is no {inputUsers} sign')