n = int(input())

for i in range(1,n+1):
    if i == n:
        res = ' '*(i-1) + str(i) + ' '*(i-1)
    else:
        res = ' '*(i-1) + str(i) + ' '*((n-i)*2 - 1) + str(i) + ' '*(i-1)
    print(res)
    
for j in range(2,n+1):
    x = n - j + 1
    res = ' '*(x-1) + str(x) + ' '*((j-1)*2 - 1) + str(x) + ' '*(x-1)
    print(res)