n = int(input())
s = input()+' '
i = 0
z = 0
f = 0

while s !='':
    if s[i]==' ':
        a = int(s[0:i])
        s=s[i+1:]
        if a%2==0:
            z+=1
        else:
            f+=1
        if f==1 and z>1:
            print(a)
            break
        elif z==1 and f>1:
            print(a)
            break
    else:
        i+=1
    
        
    