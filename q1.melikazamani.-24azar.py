ostad = ''
lst_ostadha = []

while ostad != ['end']:
    ostad = input().split()
    if ostad == ['end']:
        break
    lst_ostadha.append(ostad)
    
age = int(input())
average = int(input())

final_lst = []
for i in range(len(lst_ostadha)):
    if int(lst_ostadha[i][1]) < age and float(lst_ostadha[i][2]) > average:
       final_lst.append(lst_ostadha[i][0])
       
for j in  final_lst:
    print(j)