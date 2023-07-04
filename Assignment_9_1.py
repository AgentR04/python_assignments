import math as m

class MathematicalOperations(Exception):
    def addition(self):
        
        print("ADDITION")
        num1 = int(input("enter a number:"))
        num2= int(input("enter a number:"))
        res = num1+num2
        print(f"the addition of {num1} and {num2} is {res}")

    def subtraction(self):
        print("SUBTRACTION")
        num1 = int(input("enter a number:"))
        num2= int(input("enter a number:"))
        res = num1-num2
        print(f"the subtraction of {num1} and {num2} is {res}")
       
    def multiplication(self):
        print("MULTIPLICATION")
        num1 = int(input("enter a number:"))
        num2= int(input("enter a number:"))
        res = num1*num2
        print(f"the multiplication of {num1} and {num2} is {res}")

    def division(self):
        print("DIVISION")
        num1 = int(input("enter a number:"))
        num2= int(input("enter a number:"))
        if num1 == 0 or num2 == 0:
           raise ZeroDivisionError
        else:
          quo = num1/num2
          print(f"the quotient of {num1} and {num2} is {quo}")
        
    def square_root(self):
        print("SQUARE ROOT")
        num = int(input("enter a number:"))
        print(f"the square root of {num} is {m.sqrt(num)}")

    def expotential(self):
        print("EXPOTENTIAL")
        num = int(input("enter a number:"))
        print(f"the exponent of {num} is {m.exp(num)}")

    def power(self):
        print("POWER OF")
        num = int(input("enter a number:"))
        expo = int(input("enter a number for exponent:"))
        print(f"the power of {num} is {m.pow(num,expo)}")
    
    def trignometry(self):
        print("SINE, COS AND TAN")
        num = int(input("enter a number:"))
        print(f"the sine of {num} is {m.sin(num)}")
        print(f"the cosine of {num} is {m.cos(num)}")
        print(f"the tan of {num} is {m.tan(num)}")
        
    def choice(self):

          print("\n This is menu driven program")
          print("1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n5) Square Root\n6) Exponential\n7) Power\n8) Trignometry\n")
          num = int(input("Enter your choice: ")) 
    
          if num == 1:
             return self.addition()
       
          elif num==2:
            return self.subtraction()
       
          elif num==3:
             return self.multiplication()
        
          elif num==4:
            try:
               return self.division()
            except ZeroDivisionError:
               print("number cannot be divided by 0")
               
          elif num==5:
             return self.square_root()
        
          elif num==6:
             return self.expotential()
        
          elif num==7:
             return self.power()
        
          elif num==8:
             return self.trignometry()
        
          else:
             print("Invalid choice. Please try again.")
    
        
a = MathematicalOperations()
a.choice()