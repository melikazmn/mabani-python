s = ''
for i in range(4):
    name = input('please enter your name  ')
    d = input()
    if d == 'U' :
        i += 1
    elif d == 'R':
        s = s + ' ' + name
    elif d == 'L':
        s = name + ' ' + s
        
s = s.replace('  ',' ')
s = s[s.find(' ')+1: :]
s = s[ :s.find(' ') :]

print(s)
