#for with else
#break in for with else 
for i in range (1,10):
    if i==5:
        break
    else:
        print(i)
else:
    print("This has break")

#pass in for with else 
for i in (1,10):
    if i==5:
        pass
    else:
        print(i)
else:
    print("This has pass")

# continue in for with else
for i in range (1,10):
    if i==5:
        continue
    else:
        print(i)
else:
    print("This has continue")
   
#while with else 
#break in while with else   
i=4
while i<=10:
    if i==5:
        break
    else:
        print(i)
else:
    print("This has break")

#pass in while with else
i=4
while i<=10:
    if i==5:
        pass
    else:
        print(i)
else:
    print("This has pass")

#continue in while with else
i=4
while i<=10:
    if i==5:
        continue
    else:
        print(i)
else:
    print("This has continue")
