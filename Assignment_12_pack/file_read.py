def read_file():
    filename = input("Enter the file name: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except:
        print("Error reading file.")