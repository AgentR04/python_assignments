def create_file():
    filename = input("Enter the file name: ")
    try:
        with open(filename, 'w') as file:
            print("File created successfully.")
    except:
        print("Error creating file.")