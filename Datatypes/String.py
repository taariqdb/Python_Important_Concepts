'''#Program to demonstrate string traversal using indexing
message = "Hello Taariq"
index = 0
for i in message:
    print(f"Message[{index}] = {i}")
    index+=1
#Program to demonstrate an expression used as an in indexing of a string
str = "Hello Taariq.Welcome to the python world"
i = 2
print(str[i])
print(str[i*2+4])
#Concatenating,Appending and multiplying strings
#Program to concatenate two strings using+ operator
str1 = "Hello"
str2 = "Taariq"
print(str1 + str2)
#Program to append a string using +=operator
str = "Hello"
name = input("Enter your name:")
str += name
str += ".Welcome to python programming"
print(str)
#Program to repeat a string using * operator
str = "Taariq is the Beast"
print(str * 3)
str1 = "Hello"
var = 17
print(str1+str(var))
#String immutable
#Program to demonstrate string immutable
str1 = "Taariq"
str2 = "Dawood"
str3 = "Buhari"
print("Str1 is:",str1)
print("Str1 id is:",id(str1))
print("Str2 is:",str2)
print("Str2 is:",id(str2))
print("Str3 is:",str3)
print("Str3 is:",id(str3))
str1+= str2+ str3
print("Str1 is:",str1)
print("Str1 is:",id(str1))
str4 = str1
print("Str4 is :",str4)
print("Str4 is:",id(str4))
#String-Formatting operator
Name = input("Enter your name:")
Age = int(input("Enter your age:"))
print("%s my age is %d"%(Name,Age))
print("%d %f %s"%(3,3.33,"DB"))
#Program to display the number without formatting operator
print("i*1\ti*2\ti*3\ti*4\ti*5\ti*6\ti*7\ti*8\ti*9\ti*10")
for i in range(1,10):
    print(i*1,'\t',i*2,'\t',i*3,'\t',i*4,'\t',i*5,'\t',i*6,'\t',i*7,'\t',i*8,'\t',i*9,'\t',i*10)
    i+=1
#Program with formatting operator
print("%s %s %s %s %s %s %s %s %s %s"%("i*1","i*2","i*3","i*4","i*5","i*6","i*7","i*8","i*9","i*10"))
for i in range(1,10):
    print("%d %d %d %d %d %d %d %d %d %d" % (i*1, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9,i*10))
    i+=1
#Built-In string methods and function
str1 = "hello"
print(str1.capitalize()) # Capitalize the letter
print(str1.center(15,'*'))# Center
message = "helloTaariqhelloTaariqhelloDawoodhelloBuhari"
print(message.count(str1,0,len(message)))#Count the specific word in str
print(message.startswith("he",0,len(message)))#Starts with check the starting letter
print(message.endswith("Buhari",0,len(message)))# endswith check the ending letter
print(message.find("Taariq",0,len(message)))#find the given string
print(message.rfind("aariq",0,len(message)))#rfind the search string the from the start of the string
print(message.rindex("hello",0,len(message)))#rindex search string form the end of the string to begining of the string
print(message.index("Mom",0,len(message)))#find the index positon of the string
str2 ="JamesBond007"
print(str2.isalpha())#isalpha to check it contian alphates
print(str2.isalnum())#isalnum to check it contain alphates and number
a = "007"
print(a.isdigit())#isdigit to check it contain number
b = "lower"
print(b.islower())#islower to check it contain lowercase letter
B = "UPPER"
print(B.isupper())#isupper to check it contain uppercase letter
C = " "
print(C.isspace())#isspace to check it contain space in letter
print(len(str2))#len is to count the length of letter
print(b.ljust(10,"-"))#ljust is to left-justified to total width columns
print(B.rjust(10,"-"))#rjust is to right-justified to total width columns
str1 = "1234"
print(str1.zfill(10))#zfill is to return string left padded with zeros
str2 ="Taariq"
print(str2.lower())#Convert the string to lower
print(str2.upper())#Convert the string to upper
strip = " Taariq Dawood Buhari "
print(strip.lstrip())#Remove the leading whitespace in the string
print(strip.rstrip())#Remove the trailing whitespace in the string
print(strip.strip())#Remove the leading and trailing whitespace in the string
print(max(strip))#Return highest character in string
print(min(str1))#Return the lowest character in string
print(str2.replace("T","t"))#Replace is to replace character or string in string
title = "The story about to end"
print(title.title())#Retur the string with Title format
print(strip.swapcase())
split ="Taariq,Dawood,Buhari"#Swapcase will convert lower to upper and upper to lowercase letter
print(split.split(','))#Return the list of substring seperated by the specified delimiter
print('-'.join(['Taariq', 'Dawood', 'Buhari']))#It is just the opposite of split
print(str2.isidentifier())#Return True if the string is a valid identifier
print(list(enumerate(title)))#Return an enumerate object that list the index and value of all the characters in the string as pairs

#Program to demonstrate format
str1 = ("{}, {} and {}".format('Taariq','Dawood','Buhari'))
print("The default sequence of arguments is :" + str1)
str1 = ("{1}, {0} and {2}".format('Taariq','Dawood','Buhari'))
print("The default sequence of arguments is :" + str1)
str1 = ("{a}, {c} and {b}".format(a='Taariq',b='Dawood',c='Buhari'))
print("The default sequence of arguments is :" + str1)
#Program to demonstrate the slice operatiion
S = "Python"
print(S[1])
print(S[4])
print(S[1:])
print(S[2:5])
print(S[:])
print(S[:4])
#Program to demonstrate the negative slice operatiion
print(S[-1])
print(S[-6])
print(S[-6:])
print(S[-6:-2])
print(S[:-1])
#Program to use slice operation with stride
S = "Taariq Dawood Buhari"
print(S[2:10]) # with no stride
print(S[2:10:1])#with 1 stride it will be the same as no stride
print(S[2:10:2])#Stride with 2
print(S[1:10:3])#Stride with 3
print(S[1:14:4]) #Stride with 4
#Program to demonstrate slice operation with just last (positive) argument
print(S[::3])
#Program to demonstrate slice operation with just last (negative) argument
print(S[::-1])# this will reverse the string
print(S[::-3])
#Program  ord() and chr()
#ord function return ASCII code chr fucntion returns ASCII character
A = "a"
B = 97
print(ord(A))
print(chr(B))
print(ord("A"))
print(chr(65))
#Program membership operator(in and not in) in string
S = "Taariq Dawood Buhari"
if "aar" in S:
    print("found")
else:
    print("Not founded")
S = "Salam Rocky Bhai"
D = "KGF"
if D not in S:
    print(f"Salam Rocky Bhai is a song from {D} movie")
else:
    print(f"{D} is founded")
mean = lambda X: sum(X)/len(X)
X = [10,20,30,40,50]
print(mean(X))
a = "ai" in "aeiou"
b = "ai" not in "aeiou"
print(a)
print(b)
#Program to demonstrate string along with comparing strings
print("Abc"=="Abc")
print("Abc"=="ABc")
print("Abc">"ABc")
print("Abc"!="ABc")
print("Names"=="Name")
print("Names"<"Name")
print("Names">="Name")
print("ABc"<="ABc")
#Progam to demonstrate string along with loop or iterating string
S= "Taariq Dawood Buhari CEO of Z-ALis"
for i in S:
    print(i,end="")
S= "CEO of Z-ALis is Taariq Dawood Buhari"
index = 0
while index<len(S):
    letter = S[index]
    print(letter,end="")
    index+=1
#Program to character to iterate
def copy(str):
    new_str=" "
    for i in str:
        new_str+=i
    return new_str
str=input("Enter the string:")
print(f"The copied string is {copy(str)} ")
#Program to iterate index of character
def copy(str):
    new_str=" "
    for i in range(len(str)):
        new_str+=str[i]
    return new_str

str=input("Enter the character:")
print(f"The copied string:{str}")
#Program to print string in loop
for i in range(1,7):
    ch="A"
    print()
    for j in range(1,i+1):
        print(ch,end="")
        ch=chr(ord(ch)+1)
#Write a program to validate a pan card number
while(1):
    name  = input("Enter your name:")
    if name.isalpha() == False:
        print("Wrong creditinal,Sorry for the incovience")
        break
    else:
        pan_card = input("Enter the pan number:")
        assert len(pan_card) == 10
        if pan_card.isalnum() == False:
            print("Wrong creditential,Sorry for the incovience")
            break
        elif pan_card.isdigit() == True:
            print("Wrong creditential,Sorry for the incovience")
            break
        elif pan_card.isalpha() == True:
            print("Wrong creditential,Sorry for the incovience")
            break
    print(f"Please check your name:{name} and your pan is {pan_card}")
    break
#Write a program that encrypts a message by adding key value to every character.(Caesar Cipher)
#Hint:Say if key= 4,then add 4 to every character
msg = "CodeRed"
index = 0
while index < len(msg):
    code = msg[index]
    print(chr(ord(code)+4), end='')
    index += 1
#Write a program to generate Abecedarian series
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = "ate"
for word in a:
    print(word+b,end=',')
#Write a program to remove vowel letters
def remove_vowels(s):
    new_str = ""
    for i in s:
        if i in "aeiouAEIOU":
            pass
        else:
            new_str +=i
    print(f"The string without vowels letter:{new_str}")

ch = input("Enter the string:")
remove_vowels(ch)
#Write a program to parse an email id to print from which  email server it was sent and when.
info = "From taariq@gmail.com Thu Aug 25 11:07"
start = info.find('@')+1 # extarct character after @symbol
end = info.find('.com')+4# extract till m, find returns index of m
mailserver = info[start:end]#extract characters
start = end + 1 #Ignore the whitespace
end = len(info)-1 #Extract till the last character
date_time = info[start:end]
print(f"The email server:{mailserver}")
print(f"mail sent on:{date_time}")
#Write a program for string module
S = "Welcome to the world of python"
print("UPPERCASE -",S.upper())
print("LOWERCASE -",S.lower())
print("Title - ",S.title())
print("Count -",S.count('o'))
print("Find -",S.find('of'))
print("Replace -",S.replace("python","R"))
import string
ch = "A"
print(ch in string.ascii_uppercase)
#Write program using pyperclip framework which has copy and paste function
import pyperclip
pyperclip.copy("Hi da erruma")
print(pyperclip.paste())
#Regular expression
import re
s = "Hello Taariq.Welcome to the world of python programming"
x= re.search("^Hello",s) #Matches at the begining of the line
y= re.search("programming$",s)# Matches at the end of the line
if x:
    print("X:Match")
else:
    print("X:Not Match")
if y :
    print("Y:Match")
else:
    print("Y:No Match")
import re
Msg = "Hello Taariq.Welcome to the world of python"
x= re.findall("T..riq",Msg)#Matches any single character expect the newline character.
print(x)
m = "Taariq Dawood Buhari CEO of ZALis"
x = re.findall('[a-z]',m)# []A set of character it will match lowercase letter form a-z
print(x)
vowel_letter = "Hi Taariq .Welcome to Code Red"
x = re.findall('[^aeiou]',vowel_letter) #Matches any single character but not in bracket[]
print(x)
m = "Taariq Dawood Buhari CEO of ZALis"
x = re.findall('[a-z]*',m)# []A set of character it will match zero or more occurence of lowercase characters
print(x)
m = "Taariq Dawood Buhari CEO of ZALis"
x = re.findall('[a-z]+',m)# []A set of character it will match one or more occurence of lowercase characters
print(x)
m = "Hi students?"
x = re.findall('student.?',m)# Matches 0 ir 1 regular expression
print(x)
m = "Taariq Dawood Buhari Founder of ZALis"
x = re.findall('T.{2}riq',m)#match exactly n numbers of occurrences of regular expression
y = re.findall('F.{1}under',m)#match exactly n numbers of occurrences of regular expression
print(x)
print(y)
m="Taariq Dawood Buhari Founder of ZALis"
x = re.findall('T.{1,}riq',m)#Matches n or more occurences of regular expression
n = "23455556"
y = re.findall('2345{1,4}6',n)
print(y)
print(x)
m = "Python is easy programing"
x = re.findall("easy|tough",m)
print(x)
if x:
    print("Match")
else:
    print("Not Match")
X = "Myself Taariq Dawood Buhari"
x = re.findall("\w",X) #\w matches any charcters
print(x)
if x:
    print("Match")
else:
    print("Not Match")
X = "Myself Taariq Dawood Buhari"
x = re.findall("\W",X)#matches when it does not contain any string
print(x)
if x:
    print("Match")
else:
    print("Not Match")
X = "Myself Taariq Dawood Buhari"
x = re.findall("\s",X)#matches when it does not contain any string print whitespace
print(x)
if x:
    print("Match")
else:
    print("Not Match")
X = "Myself Taariq Dawood Buhari"
x = re.findall("\S",X)#matches when it does contain any string and remove whitespace
print(x)
if x:
    print("Match")
else:
    print("Not Match")
X = "Hi Taariq code red pass:1234"
x = re.findall('\d',X)#match only digits
print(x)
if x:
    print("Match")
else:
    print("Not Match")
X = "Hi Taariq code red pass:1234"
x = re.findall('\D',X)#matches string does not contain digits
print(x)
if x:
    print("Match")
else:
    print("Not Match")
X = "Hi Taariq code red pass:1234"
x = re.findall('\AHi',X)#matches Begining of the character
print(x)
if x:
    print("Match")
else:
    print("Not Match")
X = "Hi Taariq code red pass:1234"
x = re.findall('1234\Z',X)#matches end of the character
print(x)
if x:
    print("Match")
else:
    print("Not Match")
X = "Hi Taariq code red pass:1234"
x = re.findall('\bed',X)#matches word boundaries when outside brackets.Matches backspace when inside brackets
print(x)
if x:
    print("Match")
else:
    print("Not Match")
X = "Hi Taariq code red pass:1234"
x = re.findall(r'ed\b',X)#matches word boundaries when outside brackets.Matches backspace when inside brackets
if x:
    print("Match")
else:
    print("Not Match")
X = "Hi Taariq code red pass:1234"
x = re.findall(r'\Bed',X)#matches non-word boundaries
print(x)
if x:
    print("Match")
else:
    print("Not Match")
X = "Hi Taariq code red pass:1234"
x = re.findall(r'ed\B',X)#matches non-word boundaries
print(x)
if x:
    print("Match")
else:
    print("Not Match")
#Character classes
#Write a program that checks string has atleast one vowel
import re
pattern =r'[aeiou]'
if re.search(pattern,"Taariq"):
    print("Match Taariq")
if re.search(pattern,"bcdfgh"):
    print("Match bcdfgh")

#Write program using metacharacters*
import re
pattern = "hi(Taariq)*"
if re.search(pattern,"hi Taariq"):
    print("Match Hi Taariq")
if re.search(pattern,"hi"):
    print("Match Hi")
#Write a program using metacharacters+
import re
pattern = r"Hi(Taariq)+"
if re.search(pattern,"HiTaariq"):
    print("Hi Taariq")
if re.search(pattern,"Hi"):
    print("Hi")
#Write a program using Metacharacters ?
import re
pattern = r'Hi(Taariq)?'
if re.search(pattern,"HiTaariq"):
    print("Hi Taariq")
if re.search(pattern,"Hi"):
    print("Hi")
#Write a program using metacharacters $
import re
pattern = r"2{1,4}$"
if re.match(pattern,"2"):
    print("Match 2")
if re.match(pattern,"22"):
    print("Match 22")
if re.match(pattern,"222"):
    print("Match 222")
if re.match(pattern,"2222"):
    print("Match 2222")
if re.match(pattern,"22222"): # this will be not printed it has five 2
    print("Match 22222")
#Group
#Program to demonstrat group
import re
pattern = r'gr(ea)*t'
if re.search(pattern,'great'):
    print("Match great")
if re.search(pattern,'greaaaaaaaaaaaat'):
    print("Match greaaaaaaaaaat")
if re.search(pattern,"greaeaeaeaeaeaeat"):
    print("Match greaeaeaeaeaeaeat")
#Program to demonstrate various group in reg expression
import re
pattern = r"Py(th)on (is) go(od) Pro(gr)ammi(ng) language"
match = re.match(pattern,"Python is good Programming language")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.group(4))
    print(match.group(5))
    print(match.groups())
#Write a program to extract email address
import re
pattern = r"[\w.-]+@[\w.-]+"
s = "Please send your feedback to taariqdb@gmail.com"
match = re.search(pattern,s)
if match:
    print("Email to :",match.group())
else:
    print("Nothing")
#Write a program to validate a phone number b/w 7-9
import re
List = ['7904492347','6381981026','8939629504','5412345678']
for i in List:
    res = re.findall(r'[6-9]{1}[0-9]{9}',i)
    if res:
        print(res,end=" ")
#Wrirte program for pluraize the word
import re
def pluarize(noun):
    if re.search('[sxz]$',noun):
        return re.sub('$','es',noun)
    elif re.search('[SXZ]$',noun):
        return re.sub('$','ES',noun)
    elif re.search('[^aeioudgkprt]h$',noun):
        return re.sub('$','es',noun)
    elif re.search('[^AEIOUDGKPRT]H$',noun):
        return re.sub('$','ES',noun)
    elif re.search('[^aeiou]$y',noun):
        return re.sub('$','ies',noun)
    elif re.search('[^AEIOU]$Y',noun):
        return re.sub('$','IES',noun)
    else:
        return noun +'s'
List = ["Bush","Fox","Toy","Cap"]
for i in List:
    print(i,'-',pluarize(i))'''
