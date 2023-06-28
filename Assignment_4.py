# type casting
a="a"
ascii=ord(a)
print(ascii)
print(chr(ascii))

a=1
print(a)
a=1.0
print(a)
a="str"
print(a)

a=1
print(a)
print(float(a))
print(type(str(a)))

#conditional statements
a=int(input("Enter a num: "))
if a%2==0:
    print("even")
else:
    print("odd")

#elif
a=int(input("Enter a num 1: "))
b=int(input("Enter a num 2: "))
if a>b:
    print(a," is greater than ",b)
elif a<b:
    print(b," is greater than ",a)
else:
    print(a," is same as ",b)

#nested if
a=int(input("Enter a num 1: "))
if a>=0:
    if a==0:
        print("Zero")
    else:
        print(a," is a +ve number")
else:
    print(a," is a -ve number")

# for loops
for i in range(1,11):
    if i%2==0:
        print(i," is even")
    else:
        print(i," is odd")

#while loop
i=1
while i<=10:
    if i%2==0:
        print(i," is even")
    else:
        print(i," is odd")
    i+=1

#do while using while loop
i=True
while i==True:
    print(i)
    n=input("Enter 1 if you want to continue")
    if n=="1":
        i=True
    else:
        i=False

#loop manipulation
#break
for i in "siddhi":
    if i=="d":
        break
    else:
        print(i)

i=1
while i<=10:
    if i==5:
        break
    else:
        print(i)

#continue
for i in "siddhi":
    if i=="d":
        continue
    else:
        print(i)

i=1
while i<=10:
    if i==5:
        continue
    else:
        print(i)

#pass
for i in "siddhi":
    if i=="d":
        pass
    else:
        print(i)

i=1
while i<=10:
    if i==5:
        pass
    else:
        print(i)

#for with else loop
for i in "siddhi":
    if i=="d":
        break
    else:
        print(i)
else:
    print("This has break")

for i in "siddhi":
    if i=="d":
        pass
    else:
        print(i)
else:
    print("This has pass")


for i in "siddhi":
    if i=="d":
        continue
    else:
        print(i)
else:
    print("This has continue")

#while with else loop
i=1
while i<=10:
    if i==5:
        break
    else:
        print(i)
else:
    print("This has break")

i=1
while i<=10:
    if i==5:
        continue
    else:
        print(i)
else:
    print("This has continue")

i=1
while i<=10:
    if i==5:
        pass
    else:
        print(i)
else:
    print("This has pass")
    
# Demonstrate the use of loop manipulation statements.
# (break, pass, continue, for with else and while with else)