daneshamoozha = int(input())
tedad_dars = int(input())
lst = []
dic = {}
summ = 0

for i in range(daneshamoozha):
    idd = input().split()
    dic['id'] = idd[1]
    for j in range(tedad_dars):
        dars_nomre = input().split()
        dars = dars_nomre[0]
        dic[dars[0:len(dars)-1]] = dars_nomre[1]
    lst.append(dic)
    dic = {}

avdars = input()

for z in lst:
    summ += float(z[avdars])
    
av = summ/daneshamoozha
print(av)








        