# Define any 3 variables with given marks or user-defined marks and calculate average. Display the average in following format:
# The average of n1,n2 and n3 is ___

# take inputs separately
n1= int(input("Enter first number:"))
n2= int(input("Enter second number:"))
n3= int(input("Enter third number:"))

print(n1,n2,n3)

average =  (n1+n2+n3) / 3

print ("the average of n1, n2 and n3 is",average)


# taking three inputs in one line
numbers = input("Enter three marks separated by spaces: ")

n1, n2, n3 = numbers.split()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

average = (n1 + n2 + n3) / 3

print ("the average of n1, n2 and n3 is",average)