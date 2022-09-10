"""#Dictionary or Dict is dataype in python and it's mutuable key should be in immutable datatype and value should be in mutuable if need to change the value in future otherwise is upto our decison bt key should be in immutable data type
#Simple program for dict
A=dict()
print(A)#Empty dict
A = {'Name':['Taariq','Mohan','Santhos'],'DEPT':['CSE','CSE','CSE'],'MARKS':[100,100,100]}
print(A)#Print whole dict
#Accesing Dict elements
print(A['Name'])
print(A['DEPT'])
print(A['MARKS'])
B = dict([('Name',('Taariq','Mohan','Santhosh')),('Dept',('CSE','CSE','CSE')),('Marks',(100,100,100))])
print(B)
print(B['Name'])
print(B['Dept'])
print(B['Marks'])
#For loop in dict
Dict = {x:2*x for x in range(1,11)}
print(Dict)
#Addying and modifying the dict
A={'Name':['Taariq','Mohan','Santhos'],'DEPT':['CSE','CSE','CSE']}
print(A)
A['MARKS']=[100,100,100] # Adding elements in dict
print(A)
#Deleting Items
A={'Name':['Taariq','Mohan','Santhos'],'DEPT':['CSE','CSE','CSE']}
print(A)
A['MARKS']=[100,100,100]
A['Name'].remove('Mohan')
print(A)
del A['Name']
print(A)
A.clear()
print(A)
del A
print(A)
A={'Name':['Taariq','Mohan','Santhos'],'DEPT':['CSE','CSE','CSE']}
print(A)
A['MARKS']=[100,100,100]
print(A)
A.pop('MARKS')
print(A)
A.popitem()#After random popping
print(A)
B = dict([('Name',('Taariq','Mohan','Santhosh')),('Dept',('CSE','CSE','CSE')),('Marks',(100,100,100))])
if 'Marks' in B:
    print(B['Marks'])
#Sorting
print(sorted(B.keys()))
#Using for loop in dict
B = dict([('Name',('Taariq','Mohan','Santhosh')),('Dept',('CSE','CSE','CSE')),('Marks',(100,100,100))])
print("Key :",end=' ')
for key in B:
    print(key,end=' ')
print("\nValues :",end=' ')
for val in B.values():
    print(val,end=' ')
print("\nItem :",end=' ')
for item in B.items():
    print(item,end=' ')
#nested dictionaries
A = {'Taariq':{'Maths':100,'Python':100,'SQL':98},
     'Mohan':{'Maths':100,'Python':97,'SQL':100},
     'Santhosh':{'Maths':99,'Python':100,'SQL':100}}
print(A)
for key,vals in A.items():
    print(key,vals)
#Built in Dictionary functions and Methods
B = dict([('Name',('Taariq','Mohan','Santhosh')),('Dept',('CSE','CSE','CSE')),('Marks',(100,100,100))])
print(len(B))
print(str(B))
print(B.clear())
print(B)
B = dict([('Name',('Taariq','Mohan','Santhosh')),('Dept',('CSE','CSE','CSE')),('Marks',(100,100,100))])
C = B.copy()
print(C)
C['Performance']=['Great','Great','Great']
print(B)
print(C)
Subjects=['DBMS','Python','Java']
Marks=100
D= dict.fromkeys(Subjects,Marks)
print(D)
B = dict([('Name',('Taariq','Mohan','Santhosh')),('Dept',('CSE','CSE','CSE')),('Marks',(100,100,100))])
#Get(key)
print(B.get('Name'))
#hash_key(key)
print('Marks' in B)
#Items()
print(B.items())
#Keys()
print(B.keys())
#Setdefault
B.setdefault('Performance',[0,0,0])
print(B['Name'],'Perfomances scores:',B.get('Performance'))
B = dict([('Name',('Taariq','Mohan','Santhosh')),('Dept',('CSE','CSE','CSE')),('Marks',(100,100,100))])
C = {'Name':['Taariq','Mohan','Santhosh','Logesh'],'Dept':['CSE','CSE','CSE','CSE'],'Marks':[100,100,100,100]}
B.update(C)
print(B)
print(B.values())
for i,j in C.items():
    print(i,j)
print("Performance" not in C)
print("Performance" in B)
#String formating
S ={"Taariq":"Topper","Mohan":"Topper"}
for i,j in S.items():
    print("%s is %s in class"%(i,j))
#Write a program that creates a two dictionaries one is meters to centimeter and other m to cm
meter_to_centimeter = {x:x*100 for x in range(1,11)}
temp = meter_to_centimeter.values()
centimeter_to_meter = {x:x/100 for x in temp}
print("Meter to centimeter:",meter_to_centimeter)
print("Centimeter to meter:",centimeter_to_meter)
#Write a program english to tamil and tamil to hindi
E_T = {'Book':"Puthagam","Teacher":"Vaathi","Friend":"Nanban","Queen":"Rani"}
T_E ={"Puthagam":"Pustak","Vaathi":"Shikshak","Nanban":"Mitr","Rani":"Rani"}
for i in E_T:
    print(f"{i} in tamil {E_T[i]} and in hinid {T_E[E_T[i]]}")
#Write state code program and use set default
State_code={'TamilNadu':'TN','Maharashtra':'M','Kerala':'KL','Delhi':'DL'}
State_code.setdefault('Karanatak','Sorry no idea')
for i in State_code.items():
    print(i)
#Write a program that creates a dictionary of cubes of odd numbers in the range 1-10
odd = {x:x**3 for x in range(11) if x%2!=0}
print(odd)
#Write a program for inverted
A={'Name':'Taariq','Qualification':'BE','DEPT':'CSE'}
ineverted={}
for key,val in A.items():
    ineverted[val] = key

print("A:",A)
print("Inverted:",ineverted)
#Write a program that print a histogram of frequiences of characters occuring in message
msg="HelloTaariqDawoodBuhari!!"
Dict=dict()
for word in msg:
    if word not in Dict:
        Dict[word]=1
    else:
        Dict[word]+=1
print(Dict)
for key,val in Dict.items():
    print(key,"\t","*"*val)
#Write a program use to enter file name
filename = input("Enter the filename along with its position:")
file = open(filename,'r')
count = dict()
for line in file:
    word = line.split()
    for words in word:
        if words not in count:
            count[words]=1
        else:
            count[words]+=1
print(count)
for key,val in count.items():
    print(key,"\t","*"*val)
#Write a program using zip
Key = ["Name","Age","Education","Martial Status"]
Values = ["Taariq",23,"BE CSE","Unmarried"]
d= zip(Key,Values)
Dict = dict(d)
print(Dict)
#Write a selection sort
def selection_sort(A):
    for i in range(len(A)):
        pos = i
        for j in range(i+1,len(A)):
            if(A[pos]>A[j]):
                pos = j
        A[i],A[pos]=A[pos],A[i]
    return A
A = [3,4,5,2,1]
print("Selection sort:",selection_sort(A))
#Write a selection sort for descending
def selection_sort(A):
    for i in range(len(A)):
        pos = i
        for j in range(i+1,len(A)):
            if(A[pos]<A[j]):
                pos = j
        A[i],A[pos]=A[pos],A[i]
    return A
A=[1,2,4,5,3]
print("Selection Sort descending order:",selection_sort(A))
#Write a program to print Histrogram
import random
L=[]
for i in range(10):
    val = random.randint(1,20)
    L.append(val)
print(L)
for i in L:
    print('\n')
    count = i
    j=0
    while(j<count):
        print("*",end='')
        j+=1"""
