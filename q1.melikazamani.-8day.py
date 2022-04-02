n = int(input())
lst = []
ghabli = 'zoj'

for i in range(1,n+1):
    lst.append(str(i))

def becharkh(lst,ghabli):
    if len(lst) == 1:
        return lst[0]
    elif len(lst)%2 == 0 and ghabli == 'zoj' :
        return becharkh(lst[1:len(lst):2],'zoj') 
    
    elif len(lst)%2 == 0 and ghabli == 'fard':
        return becharkh(lst[0:len(lst):2],'fard')
    
    elif len(lst)%2 == 1 and ghabli == 'zoj':
        return becharkh(lst[1:len(lst):2],'fard')
    
    elif len(lst)%2 == 1 and ghabli == 'fard':
        return becharkh(lst[0:len(lst):2],'zoj')

print(becharkh(lst,ghabli))