# Take input from the  in a listuser and store it
li = []
for i in range(5):
    numbers = int(input("Enter number: "))
    li.append(numbers)

#Calculate the sum of all the elements in the list
sum = sum(li)
print("Sum of all elements:", sum)

#Find the smallest number
smallest = min(li)
print("Smallest number:", smallest)

#Find the largest number
largest = max(li)
print("Largest number:", largest)

#Display the list in ascending order
ascending = sorted(li)
print("Ascending order:", ascending)

#Display the list in descending order
descending = sorted(li, reverse=True)
print("Descending order:", descending)

#Convert the list into a tuple
tuple = tuple(li)
print("List converted to tuple:", tuple)

#Delete the list
del li
print("List deleted.")
