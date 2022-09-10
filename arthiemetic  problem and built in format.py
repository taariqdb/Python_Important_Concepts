# Data types :Float
# Arithmetic overflow problem:
a = float(2.7e200) * float(4.3e200)
print(a) #o/p:inf(infinity)

#arthimetic underflow problem:

b = float(3.0e-400) / float(5.0e200)
print(b) # o/p:0.0

#Built-in format():
#without using format:
c = float(16/3)
print(c)

#datatype:int
d = int(16/3)
print(d)

#using format:
d = format(float(16/3), '.3f') #.1f is used to get one decimal point for example 5.3 or if we used .2f we get 5.33
print(d)

e = format(123456789,',')
print(e)

#Zero division error
'''f = 12/0
print(f)'''

#dividing two integer
print(5 * 3.0)
print(19 + 3.5)

#quotient and remainder

print(78 // 5) # diviion floor operator

print(78 % 5) #modulo operator

#exponentiation

print( 5**2)
