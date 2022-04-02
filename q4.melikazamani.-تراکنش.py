tarakonesh = {}
name = input().split()
finallst = []
minn = 0

for i in name:
    tarakonesh[i] = 0

n = int(input())
for i in range(n):
    bedehkar = input().split()
    
    if int(bedehkar[2]) > 0:
        tarakonesh[bedehkar[1]] += int(bedehkar[2])
        tarakonesh[bedehkar[0]] += -int(bedehkar[2])
        
        
    else:
        tarakonesh[bedehkar[1]] += int(bedehkar[2])
        tarakonesh[bedehkar[0]] += -int(bedehkar[2])


for j in tarakonesh:
    if tarakonesh[j] < 0:
        finallst.append(j)
        finallst.append(tarakonesh[j])
if finallst == [] :
    print('')
    
else:
    while len(finallst) > 0 :
        minn = min(finallst[1::2])
        print(finallst[finallst.index(minn)-1])
        del finallst[ finallst.index(minn)-1]
        del finallst[ finallst.index(minn)]
