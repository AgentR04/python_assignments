import os

def delete_file():
    filename = input("Enter the file name: ")
    try:
        os.remove(filename)
        print("File deleted successfully.")
    except:
        print("Error deleting file.")