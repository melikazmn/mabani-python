def Mult(lst):
    i = len(lst) - 1
    res = ''
    
    while i >= 0:
        if i>0:
            lst[i-1] += lst[i]//10
            res = str(lst[i]%10) + res
            
        else :
            res = str(lst[i]) + res
            
        i = i - 1
            
    return res
    
lst = [1,6,14,18,9]
print(Mult(lst))