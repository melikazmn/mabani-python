def insert(lst,x):
    newlst = []
    
    if lst == []:
        newlst.append(str(x))
    else:
        if x < int(lst[0]):
            newlst.append(str(x))
        for i in range(len(lst)):     
            newlst.append(lst[i])
            
            if i<len(lst)-1 and int(lst[i]) <= x < int(lst[i+1]):
                newlst.append(str(x))    
        
        if x >= int(lst[-1]):
            newlst.append(str(x))
    lst_in_def = newlst
    
    return lst_in_def

lst = input().split()
adad = input().split()

lst_in_def = []
for i in lst:
    lst_in_def.append(i)
    
if adad == []:
    res = lst
else:
    for i in adad:
        lst_in_def = insert(lst_in_def,int(i))
    res = lst_in_def
    
print(' '.join(lst))
print(' '.join(res))