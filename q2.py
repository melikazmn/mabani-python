n = int(input('enter a number: '))
i = n-1
a = 2

print(n*'*')
while i>0:
    z = (i//2)*'*' + (n-i)*' ' + (i//2)*'*'
    print(z)
    i = i-2
    
while a<=(n-1)/2:
    p = (a)*'*' + (n-2*a)*' ' + (a)*'*'
    print(p)
    a = a+1
    
print(n*'*')