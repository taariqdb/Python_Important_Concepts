import math
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    divi = a/b
    rem = a%b
    print("Division is",divi)
    print("Remainder is",rem)

def sqrt(a):
    return math.sqrt(a)

def cos(a):
    return math.cos(a)

def sin(a):
    return math.sin(a)

def cosh(a):
    return math.cosh(a)

def sinh(a):
    return math.sinh(a)

while(True):
    print("Select From the Given Option")
    print("\n\t1-Addition")
    print("\n\t2-Subtraction")
    print("\n\t3-Multiplication")
    print("\n\t4-Division")
    print("\n\t5-Square Root")
    print("\n\t6-cos")
    print("\n\t7-sin")
    print("\n\t8-cosh")
    print("\n\t9-sinh")
    choice = int(input("Enter the your choice:"))

    if(choice == 1):
        num1= int(input("Enter the number:"))
        num2= int(input("Enter the number:"))
        print(f'{num1}+{num2}= {add(num1,num2)}')
    elif(choice == 2):
        num1= int(input("Enter the number:"))
        num2= int(input("Enter the number:"))
        print(f'{num1}-{num2}= {sub(num1,num2)}')
    elif(choice == 3):
        num1= int(input("Enter the number:"))
        num2= int(input("Enter the number:"))
        print(f'{num1}*{num2}= {mul(num1,num2)}')
    elif(choice == 4):
        num1 = int(input("Enter the number:"))
        num2 = int(input("Enter the number:"))
        div(num1,num2)
    elif(choice == 5):
        num1 = int(input("Enter the numbber:"))
        print(f'square root{num1}  = {sqrt(num1)}')
    elif(choice == 6):
        num1 = int(input("Enter the number:"))
        print(f'cos {num1} = {cos(num1)}')
    elif(choice == 7):
        num1 = int(input("Enter the number:"))
        print(f'sin {num1} = {sin(num1)}')
    elif(choice == 8):
        num1 = int(input("Enter the number:"))
        print(f'cosh {num1} = {cosh(num1)}')
    elif(choice == 9):
        num1 = int(input("Enter the number:"))
        print(f'sinh {num1} = {sinh(num1)}')
    else:
        print("bye")
        break
