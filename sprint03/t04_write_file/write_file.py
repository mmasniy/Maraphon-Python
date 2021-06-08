def write_file(file_name, message='None'):
    if file_name[-4:] != ".txt":
        print(f'Please enter the filename in the format "filename.txt".\n'
              f'Failed to write to file "{file_name}".')
    else:
        with open(file_name, "wt") as f:
            f.write(message)

        with open(file_name, "rt") as f:
            contains = f.read()
            if contains == message:
                print(f'Your message has been written to file "{file_name}".')
                print(f'File "{file_name}" now contains the following text:')
                print(contains)
            else:
                print('Something went wrong...')

