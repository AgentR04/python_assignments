
# 1) Create a function with a default parameter "file" storing the file path
def fileOperation(File="Assignment7.txt"):
    
# Note: Use try...except block with suitable exception class
    try:
# 2) Open the "file" in append mode
        File=open(File,"a+t")
        
# 3) Use writelines() method to add your roll number, name, and class
        File.writelines(["Roll no. : 13 \n",
                         "Name : Rutu \n",
                         "Class : CO \n"])
        
# 4) Use readines() method to print your data in the prompt
        File.seek(0)
        print(File.readlines())
        
    except FileNotFoundError:
        print(f"File not found.")
        
    finally:
        print("Data printed on prompt.")
        
fileOperation()