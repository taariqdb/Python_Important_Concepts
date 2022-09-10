'''#Tuple is data type in python and it's immutable
#Some basic example of tuples:
Tup1=(1,2,3,4,5)
Tup2=(-1,-2,-3,-4,-5)
Tup3=(1.1,2.2,3.3,4.4,5.5)
Tup4=('Taariq','Dawood','Buhari')
Tup5=("H","I","E","V","E","R","Y","O","N","E")
Tup6=('Taariq',17,9,1998)
print(Tup1)
print(Tup2)
print(Tup3)
print(Tup4)
print(Tup5)
print(Tup6)
#Program to explain difference b/w tuple and ordinary data type
tup1=(10,)
print(type(tup1))#<class 'tuple'>
tup2=(10)
print(type(tup2))#<class 'int'>
#Program to illustrat the use of divmod() function
quo,rem = divmod(100,3)
print("Quotient=",quo)
print("Remainder=",rem)
#Accesing the values of tuples
Tup1=(1,10,12,11,9,8,7,6,5,4,3,2)
print("Tup1[0]:",Tup1[0])
print("Tup1[0:]:",Tup1[0:])
print("Tup1[2:6]:",Tup1[2:6])
print("Tup1[:9]:",Tup1[:9])
print("Tup[:]:",Tup1[:])
#Updating Tuple
Tup1=(1,2,3,4,5)
Tup2=(6,7,8,9,10)
Tup3=Tup1+Tup2
print(Tup3)
#Deleting Tuple
Tup1=(1,2,3,4,5)
del Tup1[3] #TypeError: 'tuple' object doesn't support item deletion
print(Tup1)
#Deleting tuple
Tup1=(1,2,3)
print(Tup1)
del Tup1 #NameError: name 'Tup1' is not defined
print(Tup1)
#Basic operation of Tuples
#Length
Tup=(1,2,3,4,5,6,7,8)
print(len(Tup))
#maximum
print(max(Tup))
#mininum
print(min(Tup))
#Repetiton
s=("Taariq is Back",)
print(s*3)
#Concation
tup = Tup+s
print(tup)
#Membership
print(5 in Tup)
print(10 not in Tup)
#itearator
for i in Tup:
    print(i, end=' ')
#Conversion of tuple
A = tuple("Hello")
print(f'\n{A}')
B = tuple([1,2,3,4])
print(f"\n{B}")
#Tuple assignment
#Different type of assing tuples
(Tup1,Tup2,Tup3) = (100,200,300)
print(Tup1)
print(Tup2)
print(Tup3)
Tup = (100,300,400)
(tup1,tup2,tup3)= Tup
print(tup1,tup2,tup3)
(tup1,tup2,tup3) =(100,200)
print(tup1,tup2,tup3)#ValueError: not enough values to unpack (expected 3, got 2)
#Tuple for returning multiple values
def min_max(values):
    x=min(values)
    y=max(values)
    return (x,y)

Tup=(1,2,3,4,5,10,6,7,8,9)
(min_vals,max_vals)=min_max(Tup)
print("Mininum value:",min_vals)
print("Maximun value:",max_vals)
#Nested tuple
n_tup = ((1,"Taariq","King"),(2,"Dawood","Raja"),(3,"Buhair","Knight"))
for i in n_tup:
    print(i)
#index function in tuple
Tup1=(5,4,3,1,2,9,8,6,7,10)
print(Tup1.index(2))
Tup2=("Taariq","Dawood","Mohan","Santa","Logesh")
print(Tup2.index("Dawood"))
print(Tup2.index("Uma"))#ValueError: tuple.index(x): x not in tuple
#Counting in tuple
Tup1=(1,2,3,4,2,4,2,5,6,7,8)
n=int(input("Enter the number:"))
print(f'How many time {n} apperas  {Tup1.count(n)} in {Tup1}')
#List comphresion in Tuple
def square(T):
    return ([i**2 for i in T])

Tup1 = (1,2,3,4,5)
print("before squaring the tuple:",Tup1)
print("After squaring the tuple:",square(Tup1))
#Variable length argument tuple
def display(*args):
    print(args)

Tup=(1,2,3,4,5,6,7,8,9,10)
display(Tup)
Tup=(100,3)
quo,rem = divmod(Tup)
print("Qutoient:",quo, "Remainder:",rem)#TypeError: divmod expected 2 arguments, got 1
Tup=(100,3)
quo,rem=divmod(*Tup)
print("Qutoient:",quo, "Remainder:",rem)
#Zip function in tuple
Tup=(1,2,3,4,5)
Lis=['A','B','C','D','E']
print(tuple(zip(Tup,Lis)))
Tup=(1,2,3)
Lis=['A','B','C','D','E']
print(tuple(zip(Tup,Lis)))
#Write a program using for loop with tuple
Tup=((1,"Taariq"),(2,"Dawood"),(3,"Buhari"))
for i,char in Tup:
    print(i,char)
tup=("Taariq","Dawood","Buhari")
for index,char in enumerate(tup):
    print(index,char)
#Program to sort the tuple value
tup=(2,3,4,5,1,)
print(sorted(tup))
#Program to illustrate string formatting with tuples
Tup=('Taariq',1,'Business')
print('%s is No.%d in All '%(Tup[0],Tup[1]))
print('%s is No.%d in All %s'%(Tup))
#Write aa program thathas a nested list to store toppers details.Edit the details and reprint the details
Toppers =(("Taariq","CSE",75.5),("Mohan","CSE",77),("Santhosh","CSE",80))
choice = input("Do you want to update the details.Please enter yes or no:")
new_toppers=()
if choice=='yes':
    name=input("Enter your name:")
    new_name=input("Enter your new name:")
    course = input("Enter the course name:")
    agg = input("Enter your aggregrate:")
    i=0
    while i<len(Toppers):
        if Toppers[i][0] == name:
            new_toppers +=(new_name,course,agg)
        else:
            new_toppers +=Toppers[i]
        i+=1
else:
    new_toppers = Toppers

for i in new_toppers:
    print(i, end=" ")
#Write a program for tuple using split
addr = "taariq@gmail.com"
(user_name,domain_name) = addr.split('@')
print('user name:',user_name)
print('domain name:',domain_name)
#Write a program to make new tuple that has postive number
Tuple = (-1,1,-2,2,-3,3,-4,4,-5,5)
New_Tuple = ()
for i in Tuple:
    if i>0:
        New_Tuple +=(i,)
print(New_Tuple)
print(sum)
#Write a program to make new tuple that has positive number and sum it
Tuple=(1,-1,2,-2,3,-3,4,-4,5,-5,6,-6)
New_Tuple = ()
Sum = 0
for i in Tuple:
    if i>0:
        New_Tuple += (i,)
        Sum+=i

print(New_Tuple)
print(Sum)
def postivie(a):
    pos=()
    Sum=0
    for i in a:
        if i > 0:
            pos +=(i,)
            Sum +=i
    print(pos)
    return Sum
Tuple=(1,-1,2,-2,3,-3,4,-4,5,-5)
print(postivie(Tuple))
def postivie(*a):
    Sum=0
    for i in a:
        if i>0:
            Sum+=i

    return Sum

print(postivie(-1,1,2,3,4,5,6,-2,-3,-4-5))'''
