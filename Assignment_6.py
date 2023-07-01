# Create a function named ds with parameters roll_no and name.
def ds(roll_no,name):
    
# 2) Add those parameters in the following data structures:
# list, tuple, sets and dictionaries
    list=[roll_no,name]
    tuple=(roll_no,name)
    set={roll_no,name}
    dict={
     "roll no": roll_no, 
     "names": name
      }

    print(list)
    print(tuple)
    print(set)
    print(dict)
    
# 3) After adding values
# change the values during runtime
    roll_no = int(input("enter updated roll no:"))
    name = input("enter updated name:")
    
    list= [roll_no,name]
    tuple = (roll_no,name)
    set = {roll_no,name}
    dict = {
        "roll_no":roll_no,
        "name":name
           }
    
    print(list)
    print(tuple)
    print(set)
    print(dict)
     
# 4)Delete these data structures
    del list
    del tuple
    del set
    del dict
  
#giving default values using function arugments   
ds(13,"rutu")