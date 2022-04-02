n = int(input()) 
if n == 0:
    print('')
else:
    print(1)
    lst_ghabli = ['1']
    lst_satr = ['1']
    for i in range(n-1):
        for j in range(i):
            if j < len(lst_satr):
                lst_satr.append(str(int(lst_ghabli[j])+int(lst_ghabli[j+1])))  
        
        lst_satr.append('1')
        print(' '.join(lst_satr))
        lst_ghabli = []
        for z in lst_satr:
            lst_ghabli.append(z) 
        lst_satr = ['1']