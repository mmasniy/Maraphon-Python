def read_file(file_name):
    try:
        with open(file_name, "rt") as f:
            print(f'File "{file_name}" has the following message:')
            print(f.read())
    except IOError:
        print(f'Failed to read file "{file_name}".')
