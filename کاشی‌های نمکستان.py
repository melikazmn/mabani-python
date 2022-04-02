lmn = input().split()
m = int(lmn[0])
n = int(lmn[1])
masahat = m*n
res = []
max = 0
import math
a = int((math.sqrt(masahat)//1)+1)

while masahat != 0:
    for i in range(1,a):
        if i**2 <= masahat and i <=m  and i<=n:
            if max < i:
                max = i
    res .append(max)
    masahat = masahat -max**2
    max = 0
    
print(res)    


    