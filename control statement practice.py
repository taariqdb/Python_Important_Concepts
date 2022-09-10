'''#write a program to input two numbers and check whether they are equal or not
num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
if(num1 == num2):
    print("equal")
else:
    print("not equal")
#write a program that prompts users to enter a character (O,A,B,C,F).Then using if-elif-else to display Outstanding,Very Good,Good
#Average and Fail respectively
while(1):
    char = input("Enter O,A,B,C,F:")
    if (char == 'O') or (char =='o'):
        print("Outstanding")
        break
    elif (char == 'A') or (char == 'a'):
        print("Very Good")
        break
    elif (char == 'B') or (char == 'b'):
        print("Good")
        break
    elif (char == 'C') or (char == 'c'):
        print('Average')
        break
    elif (char == 'F') or (char == 'f'):
        print("Fail")
        break
    else:
        print("Please enter these character only O,A,B,C,F")
#write a prgram that determines whether a digit,uppercase,or a lowercase character was entered
a = input("Enter the value:")

if(a.islower()):
    print("The enter value is lower case")
elif(a.isupper()):
    print("The enter value is upper case")
elif(a.isdigit()):
    print("The enter value is digit")
else:
    print('nothing')
#Write a program that prompts user to enter a number.If the number is equal to 99 print("Congratulations").If the number is equal
#If the number is less than 99, print-enter again and aim higher-else print enter again a lower number.The program should run until
#the user guesses the correct thhe number that is 99
while(1):
    num = int(input("Enter the number:"))
    if num == 99:
        print("Congratulations")
        break
    elif num <99:
        print("Enter again")
    else:
        print("Number is high enter again")
#write a program to display first 10 natural number using for loop
for i in range(1,11):
    print(i,end=" ")
#write a program to display the average of first 10 natural number using for loop
s = 0
n = int(input("Enter the number:"))
for i in range(1,n+1):
    s = s+i
avg = s/i
print("Average:",avg)
#write a program to sum the series 1^2/1+ 2^2/2+n^2/n
n = int(input("Enter the number:"))
s = 0
for i in range(1,n+1):
    a = (i**2)/i
    s = s+a
print("The sum of series:",{s}
#Write a program that prompts the user to enter string.The program calculates and displays the length of the string until the users
#enter "QUIT"
st = 0
while(1):
    a = input("\nEnter the characters:")
    if (a=="QUIT") or (a=="quit") or (a =="Quit"):
        print("bye")
        break
    else:
        print(len(a),end=" ")
        st = st+1

print("The count of strings",st)
a = "OXFORD UNIVERSTIY PRESS"
print(a.lower())
print(a.upper())
print(a.title())
print(a[0].lower()+a[1:6],""+a[7].lower()+a[8:18],""+a[18].lower()+a[19:])
#Wirte  a program to print hallow *square pattern
n = int(input("Enter the numbers:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
n = int(input("Enter the numbers:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end= " ")
        elif i == j or i+j == n-1:
            print("$",end=" ")
        else:
            print(" ",end=' ')

    print()
n = int(input("Enter the numbers:"))
for i in range(n):
    for j in range(n):
        if i == j or i+j == n-1:
            print("$",end=" ")
        elif i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''
n = int(input("Enter the numbers:"))
for i in range(n):
    for j in range(n):
        if i==j :
            print("$", end=" ")
        elif i == 0 or i == n-1 or j==0 or j == n-1:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()