'''a=0
while(a<=10):
    print(a,end=",")
    a=a+1
i = int(input("\nEnter the number for i :"))
s = int(input("Enter the number for s :"))
n = int(input("Enter the number for n:"))
while(i<=n):
    s = s+i
    i = i+1
    print("The sum of values:", s)
# program to check positive,negative, zeros number
positive = negative = zeros = 0
print("Enter -1 to quit")
while(1):
    num = int(input("Enter the number:"))
    if (num == -1):
        break
    elif(num == 0):
        zeros = zeros+1
    elif(num > 0):
        positive = positive+1
    else:
        negative = negative+1

print("The count of zeros: ", zeros)
print("The count of positive numbers: ", positive)
print("The count of negative numbers: ", negative)
#write a program to calculate the sum of digits
num = int(input("Enter the number:"))
while(num!=0):
    temp =num % 10
    print(temp,end=',')
    num = int(num/10)
#write a program in count number from 10 to 0
n = int(input("Enter the number:"))
while n>=0:
    print(n,end=',')
    n= n- 1

#for loop
# simple for loop program

for i in range(0,10):
    print(i ,end=",")
for i in range(0,10,2): # 0 is starting number , 10 is ending number ,2 is position number
    print(i, end=",")
#Counter controlled loop  (Pre-test)
i = 0
while(i<=10):
    print(i, end=",")
    i = i+1
#Condition controlled loop
i = 1
while(i > 0):
    print(i,end=",")
    i = i+1
    if(i == 15):
        break
#simple for loop program
n = int(input("Enter the number:"))
s = 0
for i in range(1,n+1):
    s = s+i
    print(i, end=",")
print(f"\nThe sum of numbers:{s}")
print(f"\nThe count of numbers:{i}")
avg = s/i
print(f"\nThe average of numbers:{avg}")
#multiplication of numbers
n = int(input("enter the number:"))
print(f"The multiplication of {n} tables")
for i in range(0,13):
    if (n > 0):
        print(f"{n}X{i} = {n*i}")
    else:
        print("byee")
#Write a program to find odd or even
m= int(input("Enter the number of m:"))
n = int(input("Enter the number of n:"))
for i in range(m,n):
    if (i%2==0):
        print(f"{i}:The number is even")
    else:
        print(f"{i}:The number is odd")
#Write a program for factorial
num = int(input("Enter the number:"))
if num == 0:
    Fact = 1
    print(f"{num}: Factorial is {Fact}")
Fact = 1
for i in range(1,num+1):
    Fact = Fact * i
print(f"{num}: Factorial is {Fact}")
#Write a program with sum of series with power of 4
n = int(input("Enter the number:"))
s = 0
for i in range(1,n+1):
    a = i**4
    s = s+a
print(f"The sum of {n} is {s}")
#Write a program for sum of series with 1/n^n
n = int(input("Enter the numbers:"))
s = 0
for i in range(1,n+1):
    a = 1/(i**i)
    s = s+a
print(f"The sum of {n} is {s}")
#Write a program for sum of series with 1/n^2
n = int(input("Enter the numbers:"))
s = 0
for i in range(1,n+1):
    a = 1/(i**2)
    s = s+a
print("The sum of",n,"is",format(s,'.3f'))
#Write a program for sum of series which is even 2^2,4^2
n = int(input("Enter the number:"))
s = 0
for i in range(1,n+1):
    if (i%2==0):
        a = i**2
    else:
        a = 0
    s = s+a
print(f'The sum of {n} is {s}')
#nested loops
for i in range(1,6):
    print("Pass",i,"- ",end=" ")
    for j in range(1,6):
        print(j,end=" ")
    print()
#simple #* nested loop
for i in range(5):
    print("\n#",end ='')
    for j in range(5):
        print("*",end =" ")
#simple nested loop to print *with range(1,6)
for i in range(1,6):
    print()
    for j in range(i):
        print("*",end = " ")
#simple nested loop to print 1 to 6 with range(1,6)
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(j,end = " ")
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(i,end=" ")
count = 0
for i in range(1,5):
    print()
    for j in range(1,i+1):
        print(count,end=" ")
        count = count+1
N = 5
for i in range(1,N+1):
    for k in range(N,i,-1):
        print(" ",end=' ')
    for j in range(1,i+1):
        print(i,end = " ")
    print()
N = 5
for i in range(1,N+1):
    for k in range(N,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end= " ")
    for l in range(i-1,0,-1):
        print(l, end= " ")
    print()
N = 5
for i in range(1,N+1):
    for k in range(N,i,-1):
        print("",end=" ")
    for j in range(1,i+1):
        print(i, end = " ")
    print()
for i in range(10,-11,-1):
    print(i,end=",")
#Break statement
i = int(input("Enter the number:"))
while i<=10:
    print(i,end=" ")
    if(i==5):
        break
    i = i+1

print("\nDoNe")
#Continue Statement
for i in range(1,10):
    if i == 6:
        continue #It will skip particular value
    print(i, end=",")
print("\nDone")
#Calculate square root
import math
while(1):
    num = int(input("Enter the number:"))
    if num==1000:
        print("Bye")
        break
    elif num < 0:
        print("This negative number cannot be calculates")
    else:
        print("This positive number so the square root is:", math.sqrt(num))
#Pass statement
for i in range(1,10):
    if i == 6:
        pass #This pass statement will allow the mention value
    print(i, end = " ")
print('\nDone')
#else statement with loop
i = int(input("Enter the number:"))
while (i<0):
    print(i)
    i = i-1
else:
    print(f'{i}:It cannot loop bcaz it\'s not negative number')
#Distance program
X1 = int(input("Enter the X1 coordinates:"))
Y1 = int(input("Enter the Y1 coordinates:"))
X2 = int(input("Enter the X2 coordinates:"))
Y2 = int(input("Enter the Y2 coordinates:"))
distance = ((X2-X1)**2+(Y2-Y1)**2)**0.5
print(f"Distance = {distance}")'''
#correlation practice

import math
def correlation(X,Y):
    #Length of X
    n = len(X)
    X_mean = sum(X)/n
    Y_mean = sum(Y)/n
    varX = [x-X_mean for x in X]
    varY = [y-Y_mean for y in Y]
    xy = [a*b for a,b in list(zip(varX,varY))]
    r = sum(xy)/n-1
    X_square = [(x-X_mean)**2 for x in X]
    Y_square = [(y-Y_mean)**2 for y in Y]
    X_square_root = math.sqrt(sum(X_square)/n-1)
    Y_square_root = math.sqrt(sum(Y_square)/n-1)
    return r/(X_square_root*Y_square_root)

X=[]
Y=[]
n = int(input("Enter the range:"))
for i in range(0,n):
    a = int(input(f"X({i}):"))
    X.append(a)
for j in range(0,n):
    b = int(input(f"Y({j})"))
    Y.append(b)


print(f"Correlation of X and Y: {correlation(X,Y)}")