s = input('mashin hesab :/  ')
x = input('x : ')
y = input('y : ')
s = s.replace('X',x)
s = s.replace('Y',y)
res = 0
res1 = 0
res2 = 0
res3 = 0
flag = True

def alamat(s):                        #dorost kardan alamata
    if '--' in s :            
        s = s.replace('--','+')
    if '-+'in s:
        s = s.replce('-+','-')
    if '+-' in s :
        s = s.replace('+-','-')
    return s 
        

if '//0'in s or '//-0' in s :  
    print('no')
else:        
    s = alamat(s)    
    while s.find('*') > -1 and flag:    
        i = 0
        while len(s)>0 and i<len(s) :            #zarb *
            if s[i] == '*':
                j = k = i
                r = z = ''
                while s[k -1:k:].isdigit() and k>0:              #adad ghabl az zrb = z
                    z = s[k -1] + z
                    k -= 1
                z = int(z)                        #alamt adad ghabl zarb
                if k>0 and s[k-1] == '-' :    
                        z = -z
                        
                if s[j+1] == '-':        #alamat adad bad zarb
                    j += 1
                    r = '-'
                while j<len(s)-1  and s[j+1].isdigit() :  #adad bad az alamat zarb = r
                    r = r + s[j+1]
                    j += 1
                r = int(r)
                res = res + z*r
                if s[k-1] == '-' and k>0 :
                    s = s.replace(s[k-1:j+1],str(res))
                else:
                    s = s.replace(s[k:j+1],str(res))
                i = 0
                res = 0
                s = alamat(s)
                if '//0'in s or '//-0' in s:
                    print('no')
                    flag = False
            else :
                i += 1
                
 

    while s.find('//') > -1 and flag:
        i = 0     
        while len(s)>0 and i<len(s) :   #taghsim //
            if s[i:i+2] == '//':
                j = k = i
                r = z = ''
                while s[k -1:k:].isdigit() and k>0: #adad ghabl az taghsim = z
                    z = s[k -1] + z
                    k -= 1
                z = int(z)            #alamt adad ghabl taghsim
                if k>0 and s[k-1] == '-' :    
                        z = -z
                        
                if s[j+2] == '-':        #alamat adad bad taghsim
                    j += 1
                    r = '-'
                while j<len(s)-2  and s[j+2].isdigit():  #adad bad az taghsim = r
                    r = r + s[j+2]
                    j += 1
                r = int(r)
                res1 = res1 + z//r
                if s[k-1] == '-':
                    s = s.replace(s[k-1:j+2],str(res1))
                else:
                    s = s.replace(s[k:j+2],str(res1))
                i = 0
                res1 = 0
                s = alamat(s)
            else:
                i += 1


    while s.find('+') > -1 and flag:
        i = 0
        while len(s)>0 and i<len(s) :    #jam +
            if s[i] == '+':
                j = k = i
                r = z = ''
                while s[k -1:k:].isdigit() and k>0: #adad ghabl az jam = z
                    z = s[k -1] + z
                    k -= 1
                z = int(z)
                if k>0 and s[k-1] == '-' :    
                        z = -z
                while  j<len(s)-1 and s[j+1].isdigit() :  #adad bad az alamat jam = r
                    r = r + s[j+1]
                    j += 1
                r = int(r)
                res2 = res2 + (z + r)
                if s[k-1] == '-':
                    s = s.replace(s[k-1:j+1],str(res2))
                else:
                    s = s.replace(s[k:j+1],str(res2))
                i = 0
                res2 = 0
                s = alamat(s)
            else :
                i += 1
 

    while s.find('-') > -1 and flag:
        i = 0
        if s[1: ].isdigit() :
                break
        while len(s)>0 and i<len(s) :    #menha -
            if s[1: ].isdigit() :
                break
            if s[i] == '-':
                j = k = i
                r = z = ''
                while s[k -1:k:].isdigit() and k>0: #adad ghabl az menha = z
                    z = s[k -1] + z
                    k -= 1
                z = int(z)            #alamt adad ghabl menha
                if k>1 and s[k-1] == '-' :    
                        z = -z
                while j<len(s)-1  and s[j+1].isdigit() :  #adad bad az alamat menha = r
                    r = r + s[j+1]
                    j += 1
                r = int(r)
                res3 = res3 + (z - r)
                if s[k-1] == '-':
                    s = s.replace(s[k-1:j+1],str(res3))
                else:
                    s = s.replace(s[k:j+1],str(res3))
                i = 0
                res3 = 0
                s = alamat(s)
            else :
                i += 1
    if flag:
        print(s) 