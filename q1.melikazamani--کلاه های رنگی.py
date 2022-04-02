n = int(input())
lstname=[]
rang = 0

for i in range(n):
    esm_famil = input().split()
    lstname.append(esm_famil[0])
    
for j in lstname:
   count = lstname.count(j)
   if rang < count :
       rang = count
    
print(rang)