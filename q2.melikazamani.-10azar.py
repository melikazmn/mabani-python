from math import sqrt

def moadele(a,b,c,n):
    delta = b**2 - 4*a*c
    if delta < 0:
        print('no real roots')
    elif a == 0 :
        rishe = -c/b
        print(rishe)
    elif delta == 0 and a != 0:
        rishe = (-b + sqrt(delta))/2*a
        print(rishe)
    elif delta > 0 and a != 0:
        rishe1 = (-b + sqrt(delta))/(2*a)
        rishe2 = (-b - sqrt(delta))/(2*a)
        if rishe1 > rishe2 :
            rishebozorg = rishe1
            rishekoochik = rishe2
        else :
            rishebozorg = rishe2
            rishekoochik = rishe1
        if n == 0 :
            rishe = rishekoochik
        elif n == 1:
            rishe = rishebozorg
        print(rishe)
    
        
a = float(input('a  '))
b = float(input('b  '))
c = float(input('c  '))
n = float(input('n  '))
moadele(a,b,c,n)