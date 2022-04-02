n = int(input())
z = str(n)
max = 0
s = ''
count = 0
while n != 6174:
    s = ''
    for x in range(len(z)):
        for i in range(len(str(n))):
            a = n%10
            if a>=max :
                max = a
            n = n//10
        s = s + str(max)
        z = z[0:z.find(str(max))]+z[z.find(str(max))+1: ]
        if z == '':
            break
        n = int(z)
        max = 0
    if len(s)<4:
        s = (4-len(s))*'0'+ s
        
    nozoli = s
    soudi = s[ : :-1]
    n = int(nozoli)-int(soudi)
    z = str(n)
    count+=1
    
print(count)