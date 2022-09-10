'''#Program to open a file and print its attribute values
file = open('file.txt','wb')
print("Name of the file:",file.name)
print("File is closed:",file.closed)
print("File is opened:",file.mode,"mode")
#Program to access a file after it is closed
file = open('file.txt','wb')
print('Name of the file:',file.name)
print('File is closed.',file.closed)
print("Now the file will be closed")
file.close()
print("File is closed.",file.closed)
#Program for file read
file=open('file.txt','rb')
print(file.read())
#Program for file write
file = open('file.txt','w')
file.write("I'll win my life")
file.close()
print("Data is written in the file")
#Program to write to a file using the writeless() method
file = open('file.txt','w')
lines=['Hello Taariq,','Welcome To Python World','Enjoy Learning']
file.writelines(lines)
file.close()
print("Data is written in the file")
#Program to append in file
file = open('file.txt','a')
file.write("\nHave you enjoyed learning python?")
file.close()
print("Data is updated")
#Program to read
file = open('file.txt','r')
print(file.read())
file.close()
#Program to readline
file=open('file.txt','r')
print("First Line:",file.readline())
print("Second Line:",file.readline())
print("Third Line:",file.readline())
file.close()
#Program to readlines
file = open('file.txt','r')
print(file.readlines())
file.close()
#Program to use open with list
file = open('file.txt','r')
print(list(file))
file.close()
#Program to use for loop
file = open('file.txt','r')
for line in file:
    print(line)
file.close()
#Using WITH keyword
with open('file.txt','r') as file:
    for line in file:
        print(line)
file.close()
#Program read using WITH keyword
with open('file.txt','r') as file:
    print(file.read())
file.close()
#Program to split word
with open('file.txt','r') as file:
    line = file.read()
    word = line.split()
    print(word)
with open('file.txt','r') as file:
    line = file.read()
    word = line.split(',')
    print(word)
#Addtional file methods
#fileno()
file = open('file.txt','w')
print(file.fileno())#Return the file number of the file (which is an integer descriptor)
#flush
file = open('file.txt','w')
print(file.flush())# Flushes write buffer of the file stream
#isatty()
file = open('file.txt','w')
file.write("Hello")
print(file.isatty())
#readline()
file = open('file.txt','r')
print(file.readline(10))
#Truncate(n)
file = open('file.txt','w')
file.write('Welcome to the world of programming........')
file.truncate(5)
file = open('file.txt','r')
print(file.read())
#rstrip
file = open('file.txt')
line = file.readline()
print(line.rstrip())
#File position
file= open('file.txt','r')
print("Tell the position of file before using tell function:",file.tell())
file.read(10)
print("Tell the position of the file:",file.tell())
print(file.read())
file.close()
#Write a program that copies first 10 bytes of a binary file into another
with open('file.txt','rb') as file:
    with open('file2.txt','wb') as file2:
        read = file.read(10)
        file2.write(read)
print('File closed')
#Write a program to copy python script and paste it to another notepad(text file)
with open('List.py','rb') as file1:
    with open('file2.txt','wb') as file2:
        while True:
            buf = file1.readline()
            if len(buf)!=0:
                if buf[0]=='#':
                    continue
                else:
                    file2.write(buf)
            else:
                break
print("First copied")
#Write a program that accepts filename as an input from the user .Open the file and count the number of times a character appears in the file
filename = input("Enter the filename:")
with open(filename) as file:
    text = file.read()
    letter = input("Enter the character which you wanted to count:")
    count = 0
    for char in text:
        if char == letter:
            count+=1

print(f'{letter} appeared {count} in this file')
#Write a program to count vowel letter and constants letter
filename = input("Enter the file name:")
with open(filename) as file:
    vowels = 0
    constants = 0
    text = file.read()
    for char in text:
        if char in 'aeiou':
            vowels+=1
        else:
            constants+=1

print(f"Number of vowels={vowels}")
print(f"Number of constants={constants}")
print(f"The length of file={len(text)}")
print(f"The percentage of vowel={((vowels*100)/len(text))}")
print(f"The percentage of constants={((constants*100)/len(text))}")
#command line arguments
import sys
with open(sys.argv[0]) as filename:
    for line in filename:
        print(line)
#Renaming and deleting file
import os
os.rename('file2.txt','script.txt')
print('File renamed')
os.remove('script.txt')
print('File is deleted')
#Directory methods
import os
os.mkdir('New')
print("Directory is created")
#Change driectory chdir()
import os
os.chdir('New')
print("Directory is changed")
# To check the current directory
import os
print(os.getcwd())
#To remove dir
import os
os.rmdir('New')
#To create multiple directory
import os
os.makedirs('D:\\Python-notes\\Datatypes\\Dir1\\Dir2\\Dir3\\Dir4')
#os.path.join
import os
print(os.path.join('c:','students','kingisback.docx'))
#o/p:c:students\kingisback.docx
#Program to print the absoulte path of a file using os.path.join
import os
path = 'D:\Python-notes\Datatypes'
filename = 'file.txt'
abs_path = os.path.join(path,filename)
print("path name:",abs_path)
file = open(abs_path,'r')
print(file.read())
file.close()
#Methods from the os module
#os.path.abspath
import os
print(os.path.abspath("Datatypes\\file.txt"))
#os.path.isabs(path)method:
import os
print("os.path.isabs('Datypes\\file.txt')=",os.path.isabs('Dataypes\\file.txt'))
print("os.path.isabs('D:\\Python-notes\\Datypes\\file.txt')=",os.path.isabs('D:\\Python-notes\\Dataypes\\file.txt'))
#os.path.relpath(path,start)method
import os
print("os.path.relpath('D:\\Python-notes\\Datypes\\file.txt')=",os.path.relpath('D:\\Python-notes\\Datypes\\file.txt'))
#os.path.dirname(path)method
import os
print("os.path.dirname('D:\\Python-notes\\Datypes\\file.txt')=",os.path.dirname('D:\\Python-notes\\Datypes\\file.txt'))
#os.path.basename(path)method
print("os.path.basename('D:\\Python-notes\\Datypes\\file.txt')=",os.path.basename('D:\\Python-notes\\Datypes\\file.txt'))
#spilt path
import os
print("os.path.split('D:\\Python-notes\\Datypes\\file.txt')=",os.path.split('D:\\Python-notes\\Datypes\\file.txt'))
#os.path.getsize(path) and os.listdir(path)
import os
print("os.path.getsize('os.path.split('D:\\Python-notes\\Datypes\\file.txt')=",os.path.getsize('D:\\Python-notes\Datatypes\\file.txt'))
print("os.listdir(os.path.split('D:\\Python-notes)=",os.listdir('D:\\Python-notes'))
#os.path.exist,os.path.isfile,os.path.isdir()
import os
print("os.path.exist(D:\\Python-notes\Datatypes)=",os.path.exists('D:\\Python-notes\Datatypes'))
print("os.path.isfile(D:\\Python-notes\Datatypes\\file.txt)=",os.path.isfile('D:\\Python-notes\Datatypes\\file.txt'))
print("os.path.isdir(D:\\Python-notes\Datatypes\\)=",os.path.isdir('D:\\Python-notes\Datatypes'))
#Write a program that fetches data from a specified url and points it on screen
import urllib.request
x= urllib.request.urlopen('https://www.google.com/')
print(x.read())'''







