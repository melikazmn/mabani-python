lmn = input().split()
n = int(lmn[0])
m = int(lmn[1])
satr = []
res = ''
count= 0

for i in range(m):
    vorodi = input()
    satr.append(vorodi)

for z in range(n):
    for j in range(m):
        if satr[j][z] == 'W':
            count += 1
    if count%2 == 0:
        res += 'B'
    else:
        res += 'F'
    count = 0
   
print(res)