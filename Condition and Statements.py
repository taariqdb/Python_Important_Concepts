#if statement
#Program for vote age eligible:

age = int(input("Enter the age:"))
if age >= 18:
    print("Your age is eligible for voting")

#Program for post increment using if condition:

x = 10
if x > 0:
    x += 1
print(x)

#Program for charcter checking whether string,number,space:

y = input("Enter the character:")
if y.isalpha():
    print("The given character is string")

if y.isnumeric():
    print("The given character is integer")

if y.isspace():
    print("The given character is blank")

#if-else statement program :
#Program for vote age eligible:

age = int(input("Enter the age :"))

if age >= 18:
    print("Your are eligible for voting")

else:
    print("your are not eligible for voting")

#Program to find large number:
a = int(input("Enter the number A:"))
b = int(input("Enter the number B:"))

if (a>b):
    print("A has the larger value")

else:
    print("B  has the larger value")
# anothr type to find larger number:
a = int(input("Enter the number for A:"))
b = int(input("Enter the number fo B:"))

if (a>b):
    large = a

else:
    large = b

print("large = ",large)

#program to find even number and odd number

a = int(input("Enter the number:"))

if (a%2 == 0):
    print("number is even")
else:
    print("number is odd")

#program for converting lower case letter to upper case letter
ch = input("Enter the character:")

if (ch >='A' and ch <='Z'):
    ch = ch.lower()
    print("The upper case letter converted into lower case letter : " + ch)

else:
    ch = ch.upper()
    print("The lower case letter converted into upper case letter : " + ch)

'''A company decides to give bonus to all its employees on Diwali. A 5% bonus on salary is given to male workers and 10% bonus on 
salary to the female workers.Write a program to enter the salary of the employee and sex of the employee.If the salary of the 
employee is less than 10,000 rupees then the employee gets an extra 2% bonus on salary. Calculate the bonus that has to be given 
to the employee and display the salary that the employee will get'''

ch = input("Enter your gender('m' or 'f') :")
salary = int(input("Enter your salary amount :"))

if ch == 'f':
    bonus = (10/100) * salary
else:
    bonus = (5/100) * salary

amount_to_be_paid = bonus + salary
print("Salary :",salary)
print("Bonus :",bonus)
print("Amount to be paid:", amount_to_be_paid)

#Nested-If statements
#program that prompts the user to enter a number and then print its interval
num = int(input("Enter any number from 0-40: "))
if num>=0 and num<10:
    print("Number is in interval range between 0-10")
if num>=10 and num<20:
    print("Number is in interval range between 10-20")
if num>=20 and num<30:
    print("Number is in interval range between 20-30")
if num>=30 and num<40:
    print("Number is in interval range between 30-40")

#if-elif statements
#program to check postive or negative number
num = int(input("Enter the number: "))

if num == 0:
    print("The number is equal to Zero")
elif num > 0:
    print("The number is positive")

else:
    print("The number is negative")

#Program to check vowel letter or not

ch = input("Enter the character :")

if(ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
    print(ch,"is vowel letter")
elif(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
    print(ch,"is vowel letter")
else:
    print(ch,"is not vowel letter")

#Program to find the greatest number from three numbers:
num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
num3 = int(input("Enter the number:"))

if num1>num2:
    if num1>num3:
        print(num1,"is greater than",num2,"and",num3)
    else:
        print(num3,"is greater than",num1,"and",num2)
elif num2>num3:
    print(num2,"is greater than",num1,"and",num3)
else:
    print(num1,num2,num3,"all are equal")

#program based number to find days 0-7:
num = int(input("Enter the Days 0-7 :"))

if num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednessday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")

else:
    print("entered a wrong number")

'''Program to enter the marks of a student in four subjects.Then calculate the total and aggregat, and display the grade obtained
by the student. If the student scores an aggregate greater than 75%, the the grade is Distinction.If aggregate is 60>= and <75,
then the grade is First Division. If aggregate is 50>= and <60,then the grade is Second division. If aggregate is 40>= and 50<,then
the grade is Third Division. Else the grade is Fail.'''

marks1= int(input("Enter the marks in mathematics: "))
marks2 = int(input("Enter the marks in science:"))
marks3 = int(input("Enter the marks in social science:"))
marks4 = int(input("Enter the marks in computers:"))

total = marks1 + marks2 +marks3 +marks4
avg = float(total)/4
print("total = ",total,"\t Average =",avg)

if (avg >=75):
    print("Distniction")

elif (avg>=60 and avg<70):
    print("First Divison")

elif (avg>=50 and avg<60):
    print("Second Division")

elif (avg>=40 and avg<50):
    print("Third Division")

else:
    print("Fail")

#program for qudratic equation:

a = int(input("Enter the values of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

D = (b*b) - (4*a*c)
deno = 2*a

if(D>0):
    print("REAL ROOTS")
    root1 = (-b + D**0.5)/deno
    root2 = (-b - D**0.5)/deno
    print("Root1 = ", root1,"\tRoot2 = ",root2)

elif(D==0):
    print("Equal Roots")
    root1 = -b/deno
    print("Root1 and Root2 = ",root2)

else:
    print("Imaginary Roots")