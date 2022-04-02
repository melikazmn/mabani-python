def sezar(a,k):
    s = ''
    while k>25:
        k = k - 26
    while k<-25:
        k = k + 26
    if k>0:
        for i in range(len(a)):
            if 65+k> int(ord(a[i])) >64:
                t =  91 - (-ord(a[i]) + 65 + k )
                s = s + chr(t) 
            elif a[i] == ' ':
                s = s + ' '
            else:
                t = ord(a[i]) - k
                s = s + chr(t) 
        return s
    else :
        k = -k
        for i in range(len(a)):
            if 91> int(ord(a[i])) >90 - k:
                t =  ( 65 + k ) - (91 - ord(a[i]))
                s = s + chr(t) 
            elif a[i] == ' ':
                s = s + ' '
            else:
                t = ord(a[i]) + k
                s = s + chr(t)
        return s
    
def salad(a,k):
    k = -k
    sezar(a,k)
    return sezar(a,k)
  
r = input()
k = int(input())
n = int(input())
if n == 0:
    print(sezar(r,k))
else:
    print(salad(r,k))