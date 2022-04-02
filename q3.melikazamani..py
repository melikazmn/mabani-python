n = int(input())
e = 0
g = 0
b = 0

for i in range(n):
    a = int(input())
    
    if a<0 and g==0:
        e=e-a
    elif g>0 and a<0 :
        g = g+a
    elif g >= 0 and a>0:
        g+=a
    
print(e)    