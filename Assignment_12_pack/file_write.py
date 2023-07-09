def write_file():
    filename = input("Enter the file name: ")
    content = input("Enter the content to write: ")
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print("Content written successfully.")
    except:
        print("Error writing to file.")
