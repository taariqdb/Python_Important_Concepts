# boolean:
from typing import List

boolean_var = True
print(boolean_var)
print(20 == 30)
print("Python" == "Python")
print(20 != 20)
print(90 <= 90)

# list:
print([1, "ABC", 'D', 4.5])
list1 = ['a', 'bc', 78, 1.23]
list2 = ['d', 78]
print(list1)
print(list2)
print(list1[0])  # prints the first elements of the list1
print(list2[0])  # prints the second elements of the list2
print(list1[1:3])  # Prints elements starting from 2nd till 3rd
print(list2[1:3])  # Prints elements starting from 2nd till 3rd
print(list1[2:])  # Prints elements starting from 3rd element
print(list2[2:])  # Prints elements starting from 3rd element
print(list1 * 2)  # Repeats the list1
print(list2 * 2)  # Repeats teh list2
print(list1 + list2)  # concatenates two lists

# Strings
print('Hello')
print("Hello")
print('''Hello''')

# String literal concatenation:
print('Beatuiful Weather' '....' 'Seems it would rain')

# unicode string:
print(u"Sample unicode string.")

# Escape Sequences:
# print('What's your name?') # this gives syntax error to avoid this
print('What\'s your name ?')
print("The person replies, \"My name is Dawood\"")
print("Today is 15th August.\nIndia became independent on this day")  # this \n is used to print lines in next sequences
print("\a")  # bell ring
print("Hello \f World")  # prints form feed character
print("Hello\nWorld")  # prints newline character
print("Hello\tWorld")  # prints a tab
print("\056")  # prints octal value
print("\x87")  # prints hex value
print(R'What\'s your name?')
# String Formatting:
print('I\"ll rise', format('-', '-<10'), 'again')
print('I\"ll rise', format('-', '->10'), 'again')

# variables and identifiers
A = 20
B = 30
print(id(A))
print(id(B))

# Program to display data of different types using variables and literal constants
name = "TAARIQ DAWOOD BUHARI SA"
age = 24
address = "Fakir Shahib Street, Royapuram,Ch-13"
Phone_no = 8056266759

print("customer name :" + str(name))
print("customer age:" + str(age))
print("customer address:" + str(address))
print("customer phone no:" + str(Phone_no))

# program to reassign values to a variable

rocky = "Violence Violence Violence.."
print(rocky)
rocky = "I Don't Like It"
print(rocky)
rocky = "I Avoid,But Violence Likes Me"
print(rocky)
rocky = "I,can't avoid"
print(rocky)

# Multiple Assignment:
tdb = taariq = Dawood = Buhari = "Fire"
print(tdb)
print(taariq)
print(Dawood)
print(Buhari)

# Multiple Statements on Single Line
Tdb = "Mass";
taariq = "Gethu";
dawood = "Swag";
print(Tdb);
print(taariq);
print(dawood)

# input statement :
name = input("Enter your name:")
age = input("Enter your age:")
print("Customer\'s name :" + name + " And age of the customer is :" + age)

# Tuple Statement:

Tup = ('a', 'bc', '78', 1.23)
Tup2 = ('d', 78)
print(Tup);
print(Tup2);
print(Tup[0]);
print(Tup2[0]);
print(Tup[0:]);
print(Tup2[0:]);
print(Tup[2:]);
print(Tup2[1])

# Dictionary Statement:
dict = {"Name": ["Taariq", "Dawood", "Buhari"], "Age": [23, 23, 25]};
print(dict["Name"]);
print(dict["Age"]);
print(dict["Name"][-1]);
print(dict["Age"][-1])


# Arthimetric operator:
class Maths:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def modulus(self):
        return self.a % self.b

    def floor_division(self):
        return self.a // self.b

    def exponential(self):
        return self.a ** self.b


arthimetic = Maths(10, 20);
print(arthimetic.addition());
print(arthimetic.subtraction());
print(arthimetic.multiplication());
print(arthimetic.division());
print(arthimetic.modulus());
print(arthimetic.floor_division());
print(arthimetic.exponential())


# comparison operators:
class Comparison_Operator:

    def __init__(self, c, d):
        self.c = c
        self.d = d

    def if_both_equal(self):
        return self.c == self.d

    def if_not_equal(self):
        return self.c != self.d

    def if_c_is_greater(self):
        return self.c > self.d

    def if_c_is_lesser(self):
        return self.c < self.d

    def if_c_is_greater_or_equal(self):
        return self.c >= self.d

    def if_c_is_lesser_or_equal(self):
        return self.c <= self.d


comparasion_op = Comparison_Operator(100, 200);
print(comparasion_op.if_both_equal());
print(comparasion_op.if_not_equal());
print(comparasion_op.if_c_is_greater());
print(comparasion_op.if_c_is_lesser());
print(comparasion_op.if_c_is_greater_or_equal());
print(comparasion_op.if_c_is_lesser_or_equal())


# assignement operator

class Assignment_Operator:
    def add(self, a=20, b=30):
        self.a = a
        self.b = b
        a += b  # a = a + b
        return a

    def sub(self, a=20, b=30):
        self.a = a
        self.b = b
        a -= b  # a = a - b
        return a

    def mul(self, a=20, b=30):
        self.a = a
        self.b = b
        a *= b  # a = a * b
        return a

    def div(self, a=20, b=30):
        self.a = a
        self.b = b
        a /= b  # a = a /b
        return a

    def fdiv(self, a=20, b=30):
        self.a = a
        self.b = b
        a //= b  # a = a//b
        return a

    def mod(self, a=20, b=30):
        self.a = a
        self.b = b
        a %= b  # a = a%b
        return a

    def exp(self, a=20, b=30):
        self.a = a
        self.b = b
        a **= b  # a = a ** b
        return a


assignment = Assignment_Operator();
print(assignment.add());
print(assignment.sub());
print(assignment.mul());
print(assignment.div());
print(assignment.fdiv());
print(assignment.mod());
print(assignment.exp())

# unary operator:
ad = 10
ae = -(ad)

print(ae)  # o/p is -10 this is unary operator


# bitwise operator
class Bitwise_operator:
    def __init__(self, a=10101010, b=0o1010101):
        self.a = a
        self.b = b

    def andop(self):
        return self.a & self.b

    def ORop(self):
        return self.a | self.b

    def XORop(self):
        return self.a ^ self.b

    def NOTop(self):
        return ~self.a


bitwise = Bitwise_operator();
print(bitwise.andop());
print(bitwise.ORop());
print(bitwise.XORop());
print(bitwise.NOTop())

# Shiftwise operator:
# Python program to show
# shift operators
a = 1101

# print bitwise right shift operator
print("a >> 1 =", a >> 1)

# print bitwise left shift operator
print("a << 1 =", a << 1)

# Logical operators

# logical and operator

a = 10
b = 10
c = -10

if a > 0 and b > 0:
    print("The numbers are greater than 0")

if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")

# logical or operator

a = 10
b = -10
c = 0
d = 20
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or d > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

# logical not operator

a = 20

if not a:
    print("Boolean value of a is True")

if not (a % 3 == 0 or a % 5 == 0):
    print("20 is not divisible by either 3 or 5")
else:
    print("20 is divisible by either 3 or 5")

# Membership operator

l1 = [10, 20, 30, 40, 50]
l2 = [30, 40, 50]
for it in l1:
    if it in l2:  # membership "in" operator
        print("l1 does not contain the element of l2")
    else:
        print("l1 consist of l2")
    break

# membership "not in" operator:
list = [10, 20, 30, 40, 50]

X = 20
Y = 60

if (X not in list):
    print("X is not in list")
else:
    print("X is in list")
if (Y not in list):
    print("Y not in list")
else:
    print("Y is in list")

# Identity Operator
# of 'is' identity operator
x = 5
if (type(x) is int):
    print("true")
else:
    print("false")

# of 'is not' identity operator
x = 5.01
if (type(x) is not int):
    print("true")
else:
    print("false")

# concatenation:
print("My name is " + "Taariq")
# Multiplication of string or reptition of string

print("Taariq " * 5)

# Slice a string:
# string operations:
str = "python is easy language"
print(str)
print(str[0])
print(str[10:14])
print(str[10:])
print(str[-1])
print(str[::-1])  # to reverse the whole string
print(str[:6])
print(str * 2)
print(str + " isn't it?")

# Type convesion:
a = int(2) + int(3)
print(a)

b = "20" + "22"
print(b)

c = float("2") + float("3")
print(c)


# function parameters and arguments:

def search(x, i):
    if i in x:
        print("Yes")
    else:
        print("No")


l1 = [10, 20, 30, 40, 50]
l2 = 10

search(l1,l2)

#write a program to convert degree fahrenheit into degree celsius
fahrenheit = float(input("Enter the temperature ="))
celsius = (0.5) *(fahrenheit-32);print("The temperature in celsius =",celsius)
#wirte a program to caluclate the total amount of money in the piggybank given the coins of Rs10 , Rs 5, Rs 2 and Rs 1
num_coins_10 = int(input("Enter the coins of 10 ="));num_coins_5 = int(input("Enter the coins of 5 ="))
num_coins_2 = int(input("Enter the coins of 2 ="));num_coins_1 = int(input("Enter the coins of 1 ="))
total_sum = num_coins_10*10 + num_coins_5*5 +num_coins_2*2 +num_coins_1*1
print("Total coins =", total_sum)
#wirte a program to calculate the bill amount for an item given its qunatity sold,value,discount and tax

qty = float(input("Enter the quantity of item sold : "))
val = float(input("Enter the value of item : "))
discount = float(input("Enter the discount percentage : "))
tax = float(input("Enter the tax : "))
amt = qty*val
discount_amt = (amt*discount)/100
sub_total = amt - discount_amt
tax_amt = (sub_total*tax)/100
total_amt = sub_total + tax_amt
print("**********BILL*************")
print("Quantity sold : \t ",qty)
print("Price per item : \t ",val)
print("\n \t \t -----------------")
print("Amount : \t\t",amt)
print("Discount : \t\t-",discount_amt)
print("  \t  \t --------------------")
print("Discount Total : \t",sub_total)
print("Tax : \t\t\t + ",tax_amt)
print("  \t \t ----------------------")
print("Total amount to be paid ", total_amt)
..................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................