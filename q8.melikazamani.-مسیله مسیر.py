abad = input().split()
u = int(abad[0])
r = int(abad[1])

def masir(r,u):
    lst = []
    
    if r == 0:
        return [u*'U']
    
    if u == 0: 
        return [r*'R']
    
    res1 = ['R' + i for i in  masir(r-1,u)]
    res2 = ['U' + j for j in  masir(r,u-1)]
    lst = res1 + res2

    return lst

for x in masir(r,u):
    print(x)



