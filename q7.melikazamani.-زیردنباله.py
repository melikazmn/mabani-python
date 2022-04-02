n = input().split()
s = n[0]
k = int(n[1])


def zirdonbale(s,k):
    lst = []
    avalin  = ''
    
    if k == 0:
        return ['']
    
    if k == 1:
        for i in s:
            lst.append(i)
        return lst
    
    for j in range(len(s)-k+1):
        avalin += s[j]
        for x in zirdonbale(s[j+1::],k-1):
            lst.append(s[j] + x)
    
    return lst

for z in zirdonbale(s,k):
    print(z)
