def append_file():
    filename = input("Enter the file name: ")
    content = input("Enter the content to append: ")
    try:
        with open(filename, 'a') as file:
            file.write('\n' + content)
            print("Content appended successfully.")
    except:
        print("Error appending to file.")