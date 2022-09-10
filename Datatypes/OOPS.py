'''#Program to access class variable using class object
class ABC:
    var = 10
obj = ABC()
print(obj.var)
#Program to access class members using the class objects
class ABC:
    var = 10
    def display(self):
        print("In class methods....")
obj = ABC()
print(obj.var)
obj.display()
#Program illustrating the use of __init__() method(constructor method)
class ABC:
    def __init__(self,vals):
        print("In class methods")
        self.vals = vals
        print("The values is:",vals)
obj = ABC(10)
#Program to differentiate between class and object variable
class ABC:
    clas_var=0 # class variable
    def __init__(self,vals):
        ABC.clas_var +=1
        self.vals= vals #object variable
        print("The value is:",vals)
        print("The class position is:",ABC.clas_var)

obj1 = ABC(10)
obj2 = ABC(20)
obj3 = ABC(30)
#Program to modifying type attribute
class EvenOrOdd:
    Even = []
    Odd = []
    def __init__(self,vals):
        self.vals = vals
        if vals%2==0:
            EvenOrOdd.Even.append(vals)
        else:
            EvenOrOdd.Odd.append(vals)
N1=EvenOrOdd(10)
N2=EvenOrOdd(13)
N3=EvenOrOdd(14)
N4=EvenOrOdd(15)
print("Odd Number:",EvenOrOdd.Odd)
print("Even Number:",EvenOrOdd.Even)
#Program to demonstrate del method
class ABC:
    clas_var=0
    def __init__(self,vals):
        ABC.clas_var+=1
        self.vals=vals
        print("The values is:",vals)
        print("The class is:",ABC.clas_var)
    def __del__(self):
        ABC.clas_var-=1
        print("The value is deleted")

obj1=ABC(10)
obj2=ABC(20)
obj3=ABC(30)
del obj1
del obj2
del obj3'''


