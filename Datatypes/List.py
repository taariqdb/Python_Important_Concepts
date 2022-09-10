'''#List DataType
List1 = [1,2,3,4,5]
List2 = ['A','B','C','D','E']
List3 = ["Hi","Taariq","How","is","your","life","going"]
List4 = [1,'A','a','SNS&TDB']
print(List1)
print(List2)
print(List3)
print(List4)
#Access Values in List
#List[start:stop:step] #This basic sequences
#Program to demonstrtae slic opertaion
num=[]
n = int(input("Enter the range:"))
for i in range(0,n):
    X = int(input(f"Enter the number{i}:"))
    num.append(X)
print(num)
print('num[1]:',num[1])
print('num[0:]:',num[0:])
print('num[2:6]:',num[2:6])
print('num[::2]',num[::2])
print('num[::3]:',num[::3])
print('num[1::2]',num[1::2])
print('num[1::3]:',num[1::3])
print('num[2::3]:',num[2::3])
#Program to illustrate updating values in a list
list = [1,2,3,4,5,6,7,8]
print(list)
list[4]=500
print("After insertion of List:",list)
list.append(9)
print("After appending the List:",list)
del list[4]
print("After deleting the list:",list)
del list[:]
print("After the deleting the list:",list)# This will delete the whole value in the list but not del the variable list
del list
print(list)
#Program to insert one list into another list
num = [1,2,3,4,8,9,10]
print(num)
num[3]=[4,5,6,7]
print("After updating the list:",num)
#loop using nested
num =[1,2,3,'a',[5,6,7],8]
i = 0
while i < len(num):
    print(f"List{i}={num[i]}")
    i+=1
num = [1,2,3,4,5]
i = 0
for i in range(len(num)):
    print(f'List{i} = {num[i]}')
    i+=1
#Cloning list
List1 = [1,2,3,4,5,6,7,8]
List2 = List1
List3 = List1[2:6]
print(List1)
print(List2)
print(List3)
#Aliasing problem
List1 = [1,2,3,4,5]
List2 = [1,2,3,4,5]
List3 = List2
print("List1 == List2:",List1 == List2)
print("List1 is List2:",List1 is List2)
print("List2 == List3:",List2==List3)
print("List2 is List3:",List2 is List3)
print("List1 == List3:",List1==List3)
print("List1 is List3:",List1 is List3)
#List Parameters
def func(List1):
    for i in range(len(List1)):
        List1[i] = List1[i]*2

List = [1,2,3,4,5]
print("Before using func:",List)
func(List)
print("After using func:",List)
#Basic List Operator
#Write a program to print the length of the program
List=[1,2,3,4,5,6,7,8,9,10]
print(len(List))
#Write a program to concatenation of the program
List1=[1,2,3,4,5]
List2=[6,7,8,9,10]
print(List1+List2)
#Write a program using list with membership operator
print(3 in List1)
print('3' not in List)
#Write a program using max and min in list
print(max(List))
print(min(List))
#Write a program to sum all the list elements
print(sum(List))
#Write a program using all
print(all(List))
lis=[0,1,2,3,4]
print(all(lis))
#Write a program using any
print(any(lis))
l=[]
print(any(l))
#Write a program using list function
a = list("Taariq")
print(a)
#Write a program using sort function
num=[3,4,5,6,9,10,2,7]
print(sorted(num))
#List Methods
#Write a program using append
a=[1,2,3,4,5,6,7,8,9]
a.append(10)
print(a)
#Write a program using count
print(a.count(3))
#Write a program using index
print(a.index(6))
#Write a program using insert
a.insert(0,-1)
print(a)
#Write a program using pop
a.pop()
print(a)
#Write a program using remove
a.remove(-1)
print(a)
#Write a program using reverse
a.reverse()
print(a)
#Write a program to sort
b = [9,8,6,5,7,4,2,3,1]
print("before sorting:",b)
b.sort()
print("after sorting:",b)
a.extend(b)
print(a)
#Write a program to delete items using empty list[]
a=['P','r','o','g','r','a','m']
a[2:6]=[]
print(a)
#Array
#Write a program to traverse a array
import array as arr
Arr = arr.array('i',[8,2,0,4,7,3,1,6])
for X in Arr:#Traverse
    print(X,end=' ')
#Write a program to insertion of array
import array as arr
Arr = arr.array('i',[8,2,0,4,7,3,1,6])
Arr.insert(2,3)
for X in Arr:
    print(X,end=' ')
#Write a program to deletion of array
import array as arr
Arr = arr.array('i',[8,2,0,4,7,3,1,6])
Arr.remove(4)
for x in Arr:
    print(x,end=' ')
#Write a program to search of array
import array as arr
Arr = arr.array('i',[8,2,0,4,7,3,1,6])
print(f'The search of index 1:{Arr.index(1)}')
Arr[2]=10
for x in Arr:
    print(x,end=' ')
#Advanced Listing process
#zip function
Tup=(1,2,3,4,5)
Lis=['A','B','C','D','E']
print(list(zip(Tup,Lis)))
#Write a program to print list of cubes numbers
cubes = []
n = int(input("Enter the number:"))
for i in range(n):
    cubes.append(i**3)

print("Cubes Number:",cubes)
#List comprehensions
n = int(input("Enter the range:"))
cubes = [i**3 for i in range(n)]
print("Cubes numbers:",cubes)
#Write program combine two different list
X = [(x,y) for x in [10,20,30] for y in [30,40,50] if x!=y]
print(X)
#Write a program using enumerate in list
num_list = [1,2,3,4,5]
for index,i in enumerate(num_list):
    print(i,"is at index:",index)
#Write a program using iterator in list
num_list = [1,2,3,4,5]
it = iter(num_list)
for i in range(len(num_list)):
    print("Element at index:",i,'=',next(it))


# Write a program using filter in list
def checks(x):
    if x % 2 == 0:
        return 1


evens = list(filter(checks, range(2, 22)))
print(evens)


def oddc(y):
    if y % 2 != 0:
        return 1


odd = list(filter(oddc,range(1,21)))
print(odd)
#Write a program using map function
def add(x,y):
    return x+y

l1 =[1,2,3,4,5]
l2 =[6,7,8,9,10]
l3 =list(map(add,l1,l2))
print("The sum of l1 and l2:",l3)

#Write a program that adds 3 to every value in list using map
def add_x(x):
    x+=3
    return x
num_list=[1,2,3,4,5]
print("Before add_x:",num_list)
v = list(map(add_x,num_list))
print("After add_x:",v)
#Write program using reduce
import functools
def add(x,y):
    return x+y
num_list=[1,2,3,4,5]
print("The sum of num_list:=",functools.reduce(add,num_list))
#Write a program which divisible by 2 and 4 and append in a list without using filter and range should 1-20
div=[]
for i in range(1,20):
	if i%2==0 or i%4==0:
		div.append(i)

print(div)
#Write a program using with and without map and filter function to list of squares of number from 1-10.Then use the list for in construct to sum the
#elements in the list generated
def square(x): #Without map
    sq=[]
    for i in x:
        sq.append(i**2)
    return sq
List=[]
for j in range(1,11):
    List.append(j)
print(square(List))
def square_with_map(x):
    return x**2
s=[]
for i in range(1,11):
    s.append(i)
square=list(map(square_with_map,s))
print(square)X
def squarewithfilter(x):
   return x**2

square=list(filter(squarewithfilter,range(1,11)))
print(square)

#Write a pogram to remove the odd number in range 1 to 10
num_list =[]
for i in range(1,11):
    num_list.append(i)
print(num_list)
for index,i in enumerate(num_list):
    if(i%2!=0):
        del num_list[index]


print('After deleting odd number:',num_list)
#Write a program to delete the even from range 1 to 10
List=[]
for i in range(1,11):
    List.append(i)
print(List)
for index,i in enumerate(List):
    if(i%2==0):
        del List[index]

print("After Deleting even number:",List)
#Write a program to print index at which a particular value exists.If the value exist at multiple location in the list print all
#the indices,also count the number of times that  values is repeated in the list
List=[1,2,3,4,5,6,4,7,8,9,9,10]
num = int(input("Enter the number to search:"))
i=0
count=0
for i in range(len(List)):
    if num == List[i]:
        print("The number founded in",num,":",i)
        count += 1
    i += 1
print(num,"apperas",count,"in the list")
#Write a program to remove all duplicates from a lists
num_list=[1,2,3,4,5,6,7,8,8,7,5,4,3,2,1]
print("The orignal list:",num_list)
i=0
while i<len(num_list):
    num = num_list[i]
    for j in range(i+1,len(num_list)):
        val = num_list[j]
        if num == val:
            num_list.pop(j)
    i+=1
print("After duplicating values:",num_list)
#Program to reverse a list from specified range
num_list=[]
m = int(input("Enter the starting value:"))
n = int(input("Enter the ending value:"))
o = int(input("Enter the step value:"))
for i in range(m,n,o):
    num_list.append(i)

print("before reversing the list:",num_list)
num_list.reverse()
print("After reversing  the list:",num_list)
#Write a program to sort even and odd in different column using random int
import random
num_list=[]
for i in range(10):
    value = random.randint(1,50)
    num_list.append(value)
print("The original list:",num_list)
even=[]
odd=[]
for j in range(10):
    if num_list[j]%2==0:
        even.append(num_list[j])
    else:
        odd.append(num_list[j])
print("Even list:",even)
print("Odd List:",odd)
#Write a program to create a list of first 20 odd numbers using the shorcut method
odd = [i*2+1 for i in range(20)]
print(odd)
#Write a program that has a list of both positive and negative numbers.Create another list using filter() that has only positive values
def is_positive(x):
    if x>=0:
        return x

def is_negative(x):
    if x<=0:
        return x
num=[1,2,3,4,5,-1,-2,-3,-4,-5]
positive = list(filter(is_positive,num))
print("positive number:",positive)
negative=list(filter(is_negative,num))
print("Negative number:",negative)
#Write a program that converts a string of all uppercase characters into stirngs of all lowercase characters using map() function
def lower(str):
    return str.lower()

List =["PLEASE","SAVE","ME","GOD"]
l = list(map(lower,List))
print(l)
#Write a program to find the largest value in a list using reduce() function
import functools
List=[9,3,4,5,8,9,10,11,23]
print(functools.reduce(max,List))
#Write a program that has list of fucntion that scales a number by a factor of 2,3 and 4.Call each fucntion in the list on a given
#number
L= [lambda x:x*2,lambda x:x*3,lambda x:x*4]
for i in L:
    print(i(5), end=" ")
print("\nThe value of 25 will be passed to every lamnda function:",(L[0](25)),(L[1](25)),(L[2](25)))
#Write a matrix program using List
A =[[10,11,12],[13,14,15],[16,17,18]]
B = [[19,20,21],[22,23,24],[25,26,27]]
C =[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(A)):
        C[i][j]=A[i][j]+B[i][j]

for result in C:
    print(result)
#Write a program for median
List = []
n = int(input("Enter the range:"))
for i in range(n):
    print("Enter the number",i+1,"=")
    num = int(input())
    List.append(num)
List = sorted(List)
i = len(List)

if i%2==0:
    median1 = List[i//2]
    median2 = List[i//2 -1]
    median = (median1 + median2)/2
else:
    median = List[i//2]

print("The List elements:",List)
print("Median of the List:",median)
#Write a program to calculate distance between two points
import math
p1=[]
p2=[]
x1=int(input("Enter the x1 value:"))
y1=int(input("Enter the y1 value:"))
x2=int(input("Enter the x2 value:"))
y2=int(input("Enter the y2 value:"))
p1.append(x1)
p1.append(x2)
p2.append(y1)
p2.append(y2)
print("P1 elements:",p1)
print("P2 elements:",p2)
distance = math.sqrt(((p1[0]-p2[0])**2) +((p1[1]-p2[1])**2))
print("The distance:",distance)
#Write a selection sort program ascending order:
def selection_sort(A):
    for i in range(len(A)):
        index =i
        for j in range(i+1,len(A)):
            if A[index] > A[j]:
                index= j
        A[i],A[index]=A[index],A[i]
    return A

List=[-200,200,100,300,400,96,35,500]
print("Before sorting:",List)
print("After sorting:",selection_sort(List))
#Write a selection sort for descending order program
def selection_sort(A):
    for i in range(len(A)):
        index = i
        for j in range(i+1,len(A)):
            if A[index] < A[j]:
                index = j
        A[i],A[index] = A[index],A[i]
    return A

List=[100,200,300,400,500]
print("Before sorting:",List)
print("After sorting:",selection_sort(List))
#Write a program linear search
num=[]
i=0
n=int(input("Enter the range:"))
for i in range(n):
    s = int(input(f"Enter the number {i}:"))
    num.append(s)
print("Array:",num)
val = int(input("Enter the number to be search:"))
i = 0
found = 0
while i<n:
    if val == num[i]:
        print("The number is founded at this position:",i)
        found = 1
        break
    i+=1
if found==0:
    print("The enter number is not in list")
#Write a program for binary search
num=[]
i=0
n= int(input("Enter the range:"))
for i in range(n):
    s=int(input(f"Enter the number{i}:"))
    num.append(s)
print("Array:",num)
val = int(input("Enter the number to be search:"))
beg = 0
end = n-1
found = 0
while beg<=end:
    mid = int((beg+end)/2)
    if num[mid]==val:
        print(f"The number {val} founded at this position = {mid}")
        found=1
        break
    elif num[mid] > val:
        end = mid -1
    elif num[mid] < val:
        beg = mid +1


if found == 0:
    print("The number is not found")'''