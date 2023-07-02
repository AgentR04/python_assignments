# 1) Create 2 classes for single inheritance named respectively A(base class) and B(derived class)
#base class A
class A:
    
# 2) Create 3 data members in class A: a(private), b(protected) and c(public) initialise their values in a parameterized constructor 
    def __init__(self,a,b,c):
        self.__a=a #private
        self._b=b #protected
        self.c=c #public
        
# 3) Create a method known as display in both the classes, to display the values of a,b and c
    def display(self):
        print("This is base class A")
        print(f"a = {self.__a}")
        print(f"b = {self._b}")
        print(f"c = {self.c}")
  
# 1) Create 2 classes for single inheritance named respectively A(base class) and B(derived class)
#derived class B
class B(A):
    
# 3) Create a method known as display in both the classes, to display the values of a,b and c
    def display(self):
        print("This is derived class B")
        
# 4) While accessing the private member an exception should be raised and a personalized message should be displayed and the exception should be handled properly so that the rest of the code can get executed
        try:
            print(f"a = {self.__a}")
        except AttributeError:
            print(f"Private member 'a' cannot be accessed in derived class.")

        print(f"b = {self._b}")
        print(f"c = {self.c}")
        super().display()
        print()
        
b=B(10,20,30)
b.display()