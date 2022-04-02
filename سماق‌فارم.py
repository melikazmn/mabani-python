n = int(input())
p = input().split()
l = []
for i in p:
    l.append(int(i))

def somagh(l):
    i = [max(l),min(l)]
    for m in i:
        ind = l.index(m)
        
        if ind == len(l) - 1 and l[ind-1] > m: #dare payan
            if l[:ind] != (sorted(l[:ind]))[::-1]:
                 res =  'No'
            else:     
                res ='Yes'
        
        elif ind == len(l) - 1 and l[ind-1] < m:#ghole payan
            if l[:ind] != sorted(l[:ind]):
                res = 'No'
            else:
                res = 'Yes'
        
        elif ind == 0 and l[ind+1] > m:#dare aval
            if l[ind+1:] != sorted(l[ind+1:]):
                res = 'No'
            else:
                res = 'Yes'
        elif ind == 0 and l[ind+1] < m:#ghole aval
            if l[ind+1:] != sorted(l[ind+1:])[::-1]:
                 res = 'No'
            else:
                res = 'Yes'
        
        elif l[ind+1] > m : #dare
            if l[ind+1:] != sorted(l[ind+1:]):
                res = 'No'
            elif l[:ind] != (sorted(l[:ind]))[::-1]:
                 res = 'No'
            else:
                res = 'Yes'
        
        elif l[ind+1] < m :#ghole
            if l[ind+1:] != sorted(l[ind+1:])[::-1]:
                 res = 'No'
                 
            elif l[:ind] != sorted(l[:ind]):
                res = 'No'
            else:
                res = 'Yes'
                
        if res == 'Yes':
            return 'Yes'
        
    return res
        
print(somagh(l))
