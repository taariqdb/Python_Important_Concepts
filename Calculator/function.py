'''def func():
    for i in range(5):
        print("Hello World")

func()

def chumma(i):
    a = 2*i
    print(a)

chumma(4)

def add(a,b):
    return a+b

a = int(input("Enter the numb1:"))
b = int(input("Enter the numb2:"))
print(add(a,b))

num1 = int(input("Enter the number global variable:"))
print("Global num1 variable=",num1)
def func(num2):
    print("Local num2 variable=",num2)
    num3 = 30
    print("Local num3 variable=",num3)
func(20)
print("Number1=",num1)
print("Number2=",func(20+5))
print("Number3=",num3)
#Using global statement:
var = "Good"
def func():
    global var1
    var1 = "Morning"
    print("In function is var", var)

func()
print("Outside function:",var)
print("Outside function + Inside function:",var + var1)
var = "Good"
def func():
    global var1
    var1 = "Good"
    print("Insider function:",var)
func()
print("Outside function:",var1)
var = "Good Morning"
def func():
    global var
    var="Morning"
    print("Insider function:",var)
func()
print("Outside function:",var)
#Program to demonstrate acess of variable in inner and outer function
def outer():
    var = 20
    def inner():
        var1 = 20
        print("Inner varibale:",var1)
        print("Outerr variable:",var)
    inner()
    print("The outer number:",var)
    print("The inner number:",var1)
outer()
#Program to demonstrate name clash variables in case of nested functions
def outer():
    var = 20
    def inner():
        var = 20
        print("The inner variable:",var)
    inner()
    print("The outer variable:",var)
outer()
#Program that demonstrate using a variable defined in global namespace
def func():
    print(s)
s = "Hello Taariq"
func()
#Program that demonstrate using a local variable with same name as that of global
def show():
    global s
    print(s)
    s = "Welcome Python Program"
    print(s)
s = "Hello Taariq"
show()
#Program that demonstrate without return funtion
def func(s):
    print(s)
x = print(func("Hi Taariq"))
print(x)
print(func("Hi TDB"))
#Program with return function
def func(s):
    return s
x = func("Hi Taariq")
print(x)
def cube(x):
    return x**3
x = 2
print(cube(x))
#Program to demonstrate flow of control after the return statement
def control_flow():
    print("This is the inner function or local function")
    print("This is local function can be printed inside def function")
    return
    print("This function will never display")

control_flow()
x="This outer function which out of the def function"
print(x)
#Program to demonstrate keyword argumment
def func(str,int_x,float_y):
    print("The string is:",str)
    print("The int_x is:",int_x)
    print("The float_y is:",float_y)
func('Taariq',23,25000.25)
#Program to demonstrate keyword argument
def func(name,age,salary):
    print("Name:",name)
    print("Age:",age)
    print("Salary:",salary)

Name = "Taariq"
Age = 23
Salary = 1000000
func(age = Age,salary = Salary,name = Name)
#Program to demonstrate default argument
def func(Student_Name,Dept="CSE"):
    print("Student Name:",Student_Name)
    print("Department:",Dept)

func(Student_Name="Taariq",Dept="Law")#Keyword arguement
func(Student_Name="Dawood")# Default argument
#program to demonstrate the error could happened
def errno(name,dept="CSE",ranks=1):
    print("NAME:",name)
    print("DEPARTMENT:",dept)
    print("RANKS:",ranks)

errno(name="Taariq",9)
def err(name,dept="CSE",ranks):
    print("Name:",name)
    print("Department:",dept)
    print("Rank:",ranks)

err(name="Taariq",1)
#Variable-Length Argument
#Program to demonstrate variable-length argument
def product(brand,*products):
    print("\n",brand,"Owner of this product")
    for items in products:
        print(items,end=" ")
product("Samsung","Galaxy S3","Galaxy S6","Galaxy Flip")
product("Apple","iPhone7","iPhone8","iPhone10","iPhone11")
product("MI","Notebook6","Notebook6Pro","Notebook10Pro")
#Another program
def ownings(person,*things):
    print("\n",person,"owns these things")
    for items in things:
        print(items,end=" ")
ownings("Taariq","Apple Iphone7+","Lenovo Ideapad gaming 3")
ownings("Mohan","Motorola","Acer aspire7")
ownings("Mom","Nothing")
#Programs that calculation two numbers using the syntax of lambda function(Private function)
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Divi")
print("5.Mod")
while(True):
    ch = int(input("Enter the number:"))
    if ch == 1:
        X = int(input("Enter the numbers:"))
        Y = int(input("Enter the numbers:"))
        sum = lambda X,Y:X+Y
        print(sum(X,Y))
    elif ch == 2:
        X = int(input("Enter the numbers:"))
        Y = int(input("Enter the numbers:"))
        sub = lambda X,Y:X-Y
        print(sub(X,Y))
    elif ch == 3:
        X = int(input("Enter the numbers:"))
        Y = int(input("Enter the numbers:"))
        mul = lambda X,Y:X*Y
        print(mul(X,Y))
    elif ch == 4:
        X = int(input("Enter the numbers:"))
        Y = int(input("Enter the numbers:"))
        div = lambda  X,Y:X/Y
        print(div(X,Y))
    elif ch == 5:
        X = int(input("Enter the numbers:"))
        Y = int(input("Enter the numbers:"))
        mod = lambda X,Y:X%Y
        print(mod(X,Y))
    else:
        print("Bye")
        break
#Program that passes lambda function as an argument to a function:
def func(f,n):
    print(f(n))
square = lambda X:X*2
cube = lambda X:X*3
func(square,4)
func(cube,4)
#Program to invoke lambda function with range:
ran = lambda:sum(range(1,11))
print(ran())
#Program to show a multi line docstring
def func():
    """The program is just to explain
    about the docstring.
    Let's Hope for best..."""
    print("Hello Taariq")
print(func.__doc__)
#Program using functions to check whether two numbers are equal or not
def check_relation(a,b):
    if a == b:
        return 0
    if a > b:
        return 1
    if a < b:
        return -1

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
res = check_relation(a,b)
if res == 0:
    print("a is equal to b")
if res == 1:
    print("a is greater than b")
if res == -1:
    print("a is lesser than b")
#Write a program to return the full name of a person
def name(firstname, lastname):
    seperator = ' '
    n = firstname+seperator+lastname
    return n
print(name("Taariq","Dawood"))
#Write a program to return the average of its arguments
def avg(a,b):
    return (a+b)/2
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
print("Average number=",avg(a,b))
#Program using functions and return statement to check whether a number is even or odd
def even_or_odd(a):
    if a%2==0:
        return 1
    else:
        return -1

a = int(input("Enter the number:"))
b = even_or_odd(a)
if b ==1:
    print("The entered number is even")
if b == -1:
    print("The entered number is odd")
#Program to calculate PNR

def PNR(p,y,s):
    if(s=='y'):
        return (p*y*12)/100
    else:
        return (p*y*10)/100

p = int(input("Enter the principal amount:"))
y = int(input("Enter the numbers of year:"))
s = input("Enter your senior citizen (Y/N):")
pnr = PNR(p,y,s)
print("Interest:",pnr)
#Write a program that uses docstrings and variable length argument to add the values passed to the function
def add(*argss):
    """Print this line"""
    sum = 0
    for  i in argss:
        sum+=i
    return sum

print(add.__doc__)
print("SUM =",add(25,35,45,55,65))
#Program to print the factorial with recursion
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
n = int(input("Enter the number:"))
print(f"The factorial of {n} is {fact(n)}")
#Program to print the factorial without recursion
num = int(input("Enter the number:"))
i = num
result = 1
while(i>=1):
    result = result * i
    i = i-1
print(f"The factorial num is{num}: {result}")
#Program to print fibonacci series with recursion
def fibonacci(n):
    if n<2:
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

n = int(input("Enter the number:"))
for i in range(n):
    print(f"Fibonacci:{fibonacci(i)}")
#program to print fibonacci series without recursion
num = int(input("Enter the numbers:"))
a = 0
b = 1
i = 2
print(a,end=" ")
print(b,end=" ")
while(i<num):
    sum = a+b
    print(sum,end=" ")
    a,b = b,sum
    i = i+1
#Function Redefinition
#Program to demonstrate function redefinition
import datetime
def showmsg(msg):
    print(msg)
showmsg("Hello")
def showmsg(msg):
    now = datetime.datetime.now()
    print(msg)
    print(str(now))
showmsg("Current Date and Time:")
import datetime
now = datetime.datetime.now()
print(f"Current Date and Time:{now}")

#Write a program that finds the greatest of three given number using functions.Pass the arguments
def greatest_num(a,b,c):
    if a>b or a>c:
        print(f"A:{a} is greater than B:{b} and C:{c}")
    elif b>a or b>c:
        print(f"B:{b} is greater than B:{a} and C:{c}")
    elif c>a or c>b:
        print(f"C:{c} is greater than A:{a} and B:{b}")
    else:
        print(f"all are equal")

A= int(input("Enter the number:"))
B= int(input("Enter the number:"))
C= int(input("Enter the number:"))
print(greatest_num(A,B,C))
import timeit

def mean(a):
    a.sort()
    n = len(a)
    return sum(a)/n
X=[1,2,3,4,5,4]
print(f"Mean of X:{mean(X)}")
print(f"the execution time of  mean is {timeit.timeit(lambda:mean(X))}")
#Write a program that uses lambda function to multiply two numbers
import timeit
multiply = lambda X,Y:X*Y
X = int(input("Enter the number:"))
Y = int(input("Enter the number:"))
print(f"The multiplication of {X},{Y}:{multiply(X,Y)}")
print(f"The execution time of multiplication of X,Y :{timeit.timeit(lambda:multiply(X,Y))}")
#Write a function that accept int b/w 1 to 12 to represent the month in number and displays the corresponding month of the year
import timeit
def display_months(n):
    if n==1:
        return "JANUARY"
    elif n==2:
        return "FEBUARY"
    elif n==3:
        return "MARCH"
    elif n==4:
        return "APRIL"
    elif n==5:
        return "MAY"
    elif n==6:
        return "JUNE"
    elif n==7:
        return "JULY"
    elif n==8:
        return "AUGUST"
    elif n==9:
        return "SEPTEMBER"
    elif n==10:
        return "OCTOBER"
    elif n==11:
        return "NOVEMBER"
    elif n==12:
        return "DECEMBER"
    else:
        return "Wrong Number"

n = int(input("Enter the number:"))
print(f"{n} Month :{display_months(n)}")
print(f"The execution time of this program:{timeit.timeit(lambda:display_months(n))}")
#Write def program to print pattern
def pattern(n):
    for i in range(n):
        for j in range(n):
            if i ==0 or i == n-1:
                print("*",end=" ")
            elif j ==0 or j == n-2:
                print("!",end=" ")
            else:
                print(" ",end=" ")
        print()
n = int(input("Enter the number:"))
pattern(n)
#Another def progam to print pattern
def pattern(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1:
                print("*",end=" ")
            elif j==0 or j==n-1:
                print("!",end=" ")
            else:
                print(" ",end=" ")
        print()
n = int(input("Enter the number:"))
pattern(n)
def pattern(n):
    for i in range(n):
        for j in range(n):
            if i==j or i+j == n-1:
                print("!",end=" ")
            elif i==0 or i==n-1 or j==0 or j==n-1:
                print("*",end=" ")
            else:
                print(' ',end=" ")
        print()
n = int(input("Enter the number:"))
pattern(n)
def pattern(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("*",end=" ")
            elif i==j or i+j==n-1:
                print("!",end=" ")
            else:
                print(" ",end=" ")
        print()
    return
n = int(input("Enter the number:"))
pattern(n)
def pattern(n):
    for i in range(n):
        for j in range(n):
            if i+j==n-1:
                print("!",end=" ")
            elif i==0 or i==n-1 or j==0 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

n = int(input("Enter the number:"))
pattern(n)
def pattern(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                print("*",end=" ")
            elif i==n-1 or j==0 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

n = int(input("Enter the number:"))
pattern(n)
def pattern(n):
    for i in range(n):
        for j in range(n):
            if i+j==n-1:
                print("*",end=" ")
            elif i==n-1 or j==n-1 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

n = int(input("Enter the number:"))
pattern(n)
#Write a program to print a fibonacci series with recursion
def fib(n):
    if(n<2):
        return 1
    else:
        return (fib(n-1)+fib(n-2))

n = int(input("Enter the number:"))
for i in range(n):
    print(f"Fibonacci{i}:{fib(i)}")
#Write a program to reverse a string using recursion
def reverse(a):
    if len(a) == 0:
        return a
    else:
        return a[::-1]

a = "Taariq"

print(f"The orginal letter:{a}")
print(f"After recursion:{reverse(a)}")
#Write a program to reverse a string using without recursion
a = "Taariq Dawood Buhari"

print(f"The original letter:{a}")
print(f"The reverse letter:{a[::-1]}")
#Write a fibonacci proogram without recursion
n = int(input("Enter the number:"))
if n<2:
    print(1)
else:
    a=0
    b=1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(2,n):
        sum = a+b
        print(sum,end=" ")
        a,b=b,sum
        i+=1
#Write a status progam M for married ,S- seperated,D-divorced and UM-unmarried along with docstring function
def status(n):
    """In case an appropriate letter is passed .Pleased enter the correct character"""
print("'M','S','D','UM' ")
while(1):
    n = input("Enter the status:")
    if n == "M":
        print("Married")
        break
    elif n == "S":
        print("Seperated")
        break
    elif n == "D":
        print("Divorced")
        break
    elif n == "UM":
        print("Unmarried")
        break
    else:
        print(status.__doc__)
#Write function that displays "Hello name",for any given name passed to it
def name(a):
    return a
a = input("Enter your name:")

print(f"Hello {name(a)}")'''
