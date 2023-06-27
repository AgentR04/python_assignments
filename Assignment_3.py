def calculator():
    print("Arithmetic Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")
    print("7. Floor Division (//)")

    choice = input("Enter the operator (1-7): ")

    if choice == '1':
        add = num1+num2
        print("Result:", add)
        
    elif choice == '2':
        sub = num1-num2
        print("Result:", sub)
        
    elif choice == '3':
        mul = num1*num2
        print("Result:", mul)
        
    elif choice == '4':
        div= num1/num2
        if num2 != 0:
            print("Result:", div)
        else:
            print("Cannot divide by zero!")
            
    elif choice == '5':
        mod= num1%num2
        print("Result:", mod)
        
    elif choice == '6':
        expo= num1**num2
        print("Result:", expo)
        
    elif choice == '7':
        floor_div = num1//num2
        print("Result:", floor_div)
        
    else:
        print("Invalid choice!")

calculator()
calculator()