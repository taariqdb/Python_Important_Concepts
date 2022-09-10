'''#Program to handle the divide by zero exception
num = int(input("Enter the numerator:"))
deno = int(input("Enter the denominator:"))
try:
    quo = num/deno
    print("Qutoient:",quo)
except ZeroDivisionError:
    print("Denominator cannot be zero")
#Program with multiple except blocks
try:
    num = int(input("Enter the number:"))
    print(num**2)
except KeyboardInterrupt:
    print("\nProgram terminated due to keyboard interrupt")
except ValueError:
    print("Please enter proper value...program terminated")

print('bye')
#Program with multiple exceptions in a single block
try:
    num = int(input("Enter the number:"))
    deno = int(input("Enter the denominator:"))
    quo = num/deno
    print("Quotient:",quo)
except(KeyboardInterrupt,ZeroDivisionError,ValueError,TypeError):
    print("\nPlease enter proper value .... Program terminated")
print('bye')
#Program to demonstrate the use of except:block
try:
    file = pen("file.txt")
    str = file.readline()
    print(str)
except IOError:
    print("Error occured due to IOerror")
except ValueError:
    print("Error occured due to value error")
except:
    print("Error occured due to someother problem")
#Program to demonstrate else block
try:
    file = open('file.txt')
    str = file.readline()
    print(str)
except:
    print("Error occured due to some mistake in the code")
else:
    print("Program executed successfully")
#Program to demonstrate else block
try:
    file = open('file.txt')
    str = f.readline()
    print(str)
except:
    print("Error occured due to some mistake in the code")
else:
    print('Program is successfully executed')
#Raising exceptions
#Program to deliberately raise an exception
try:
    num=10
    print(num)
    raise  ValueError
except:
    print("Exception occured... due to programming")
#Program to re-raise an exception
try:
    raise NameError
except:
    print("Re-raising the exception")
    raise
#Program to understand the process of instantianting an exception
try:
    raise Exception("Hello","Taariq")
except Exception as ErrObj:
    print(type(ErrObj))
    print(ErrObj.args)
    print(ErrObj)
    arg1,arg2= ErrObj.args
    print("Argument1=",arg1)
    print("Argument2=",arg2)
#Program to raise exception with arguments
try:
    raise Exception("Hello","Taariq")
except ValueError:
    print("Program terminated")
#Handling exceptions in invoked functions
#Program to handle exceptions from an invoked function
def divide(num,denom):
    try:
        quo = num/denom
        print(quo)
    except ZeroDivisionError:
        print("Program terminated due to Zero Division Error")

num = int(input("Enter the numerator:"))
denom = int(input("Enter the denominator:"))
divide(num,denom)
#Program to handle exception in the calling function
def divide(num,denom):
    return num/denom

try:
    n = int(input("Enter the numerator:"))
    d = int(input("Enter the denominator:"))
    divide(n,d)
except ZeroDivisionError:
    print("Program terminated due to zero division error")
#Try and final block
#Program with finally block that leaves the exception unhandled
try:
    print("Raising exception")
    raise ValueError
finally:
    print("Performing clean up finally")
#Program to illustrate the use of try and except and finally block all together
try:
    print("Raise exceptions")
    raise ValueError
except:
    print("Finally caught exception")
finally:
    print("Performing clean up finally")
#Program to demonstrate I/O Error
try:
    with open('file1.txt','w') as file:
        file.write("\n Hi Taariq How are you?")
except IOError:
    print("Error working with file")
else:
    print("The successfully printed")
#2 example to demonstarte IO Error:
try:
    with open('file1.txt','r') as file:
        file.write("\n Hi Taariq How are you?")
except IOError:
    print("Error working with file")
else:
    print("The successfully printed")
#Program to demonstrate value error
try:
    num=int(input("Enter the number:"))
    if num>=0:
        print(num)
    else:
        raise  ValueError("Negative number is not allowed")

except ValueError as e:
    print(e)
#Program StopIteration
def dis(n):
    while True:
        try:
            n+=1
            if n==21:
                raise StopIteration
        except StopIteration:
            break
        else:
            print(n,end=' ')
i=0
dis(i)
#Local,Global and built-in namespace
def max(numbers): #global namespace
    print("User Defined Function Max....")
    large = -1    #local namespace
    for i in numbers:
        if i>large:
            large=i
    return large
numbers=[9,8-1,2,5]
print(max(numbers))
print(sum(numbers)) #built-in namespace'''

