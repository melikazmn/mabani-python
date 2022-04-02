s = input('enter something:)  ')
n = input('enter kalame zesht:/  ')
kalame = ''

for i in range(len(n)):
    if s.find(n[i]) > -1 :
        kalame = kalame + s[s.find(n[i])]
        s = s[s.find(n[i])+1 : : ]
    elif s.find(n[i]) == -1 :
        kalame != n
        
if kalame == n:
    print('YES')
else :
    print('NO')