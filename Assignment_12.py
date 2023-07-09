import Assignment_12_pack.file_create as c
import Assignment_12_pack.file_read as r
import Assignment_12_pack.file_write as w
import Assignment_12_pack.file_append as a
import Assignment_12_pack.file_delete as d

def menu():
    print("File Handling Menu")
    print("1. Create a new file")
    print("2. Read a file")
    print("3. Write to a file")
    print("4. Append to a file")
    print("5. Delete a file")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    return choice

while True:
    choice = menu()
    if choice == '1':
        c.create_file()
    elif choice == '2':
        r.read_file()
    elif choice == '3':
        w.write_file()
    elif choice == '4':
        a.append_file()
    elif choice == '5':
        d.delete_file()
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")

