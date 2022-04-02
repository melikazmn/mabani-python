n = int(input())
l_nima = []
l_sina = []

for i in range(n):
    nimas_list = input()
    l_nima.append(nimas_list)
    
for j in range(n-1):
    sinas_list = input()
    l_sina.append(sinas_list)
    
for p in range(len(l_nima)-1):
    if l_nima[p] in l_sina:
       l_nima.remove(p) 
    
print(l_nima[0])
        