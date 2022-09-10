import math
'''X=[10,20,30,40,50,60,60]
X.sort()
def mean (a):
    return sum(a)/len(a)
print(f"The mean of X is {mean(X)}")
def median(a):
    n = len(a)
    if n % 2 == 0:
        median1 = a[n//2]
        median2 = a[n//2 -1]
        median = (median1 + median2)/2
    else:
        median = a[n//2]
    return median
print(f"The median of X is {median(X)}")
from collections import Counter
def mode(a):
    n = len(a)
    c = Counter(a)
    mode = [k for k,v in c.items() if v == c.most_common(1)[0][1]]
    if len(mode) == n:
        get_mode = 0
    else:
        get_mode = mode
    return get_mode
print(f"The mode of X is:{mode(X)}")
#another type of mode without using counter
def mode1(a):
    a.sort()
    n=len(a)
    l1=[]
    i = 0
    while(i<n):
        l1.append(a.count(a[i]))
        i=i+1
    dict1 = dict(zip(a,l1))
    dict2 = [k for k,v in dict1.items() if v == max(l1)]
    if len(dict2) == n:
        n_mode = 0
    else:
        n_mode = dict2
    return n_mode
print(f"The new mode of X is :{mode1(X)}")
def deviations(a):
    n = len(a)
    mean = sum(a)/n
    d = [(x-mean)**2 for x in a]
    return d

print(f'The deviation of X is:{deviations(X)}')

def variance(a):
    n = len(a)
    mean = sum(a)/n
    d = [(x-mean)**2 for x in a]
    return sum(d)/(n-1)

print(f"The variance of X is: {variance(X)}")

def standard_deviation(a):
    n = len(a)
    mean = sum(a)/n
    d = [(x-mean)**2 for x in a]
    variance = sum(d)/(n-1)
    return math.sqrt(variance)

print(f"The standard deviation of X is: {standard_deviation(X)}")

#Correlation:
# noinspection PyTypeChecker
def correlation(a,b):
    n = len(a)
    m = len(b)
    mean_a = sum(a)/n
    mean_b = sum(b)/m
    xy = [(x-mean_a)*(y-mean_b) for x in a for y in b]
    d = sum(xy)/(n-1)
    Xd2 =[(x-mean_a)**2 for x in a]
    Yd2 =[(y-mean_b)**2 for y in b]
    sX = sum(Xd2)/(n-1)
    sY = sum(Yd2)/(n-1)
    s1 = math.sqrt(sX)
    s2 = math.sqrt(sY)
    square_root = s1*s2
    return d/square_root
X=[135,127,124,120,115,112,104,96,94,85]
Y=[121,131,112,115,99,118,106,89,92,90]
print(correlation(X,Y))
def r(X,Y):
    n = len(X)
    mean_X = sum(X)/len(X)
    print(f"Mean value of X:{mean_X}")
    mean_Y = sum(Y)/len(Y)
    print(f"Mean value of Y:{mean_Y}")
    var_X = [x-mean_X for x in X]
    var_Y = [y-mean_Y for y in Y]
    var = [a*b for a,b in list(zip(var_X,var_Y))]
    xy= sum(var)/(n-1)
    print(f"Summation of X,Y :{xy}")
    square_X = [(x-mean_X)**2 for x in X]
    square_Y = [(y-mean_Y)**2 for y in Y]
    ssx = math.sqrt(sum(square_X)/(n-1))
    print(f"square root of X^2 :{ssx}")
    ssy = math.sqrt(sum(square_Y)/(n-1))
    print(f"square root of Y^2 :{ssy}")
    return xy/(ssx*ssy)
X = []
Y = []
n = int(input("Enter the number range X:"))
for i in range(0,n):
    value = int(input(f"Enter the {i} number:"))
    X.append(value)
m = int(input("Enter the number range Y:"))
for j in range(0,m):
    valueY = int(input(f"Enter the {j} number:"))
    Y.append(valueY)

print(f"Correlation of X,Y :{r(X,Y)}")'''

