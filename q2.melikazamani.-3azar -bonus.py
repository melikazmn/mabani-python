s1 = input()
s2 = input()

h1 = int(s1[ :s1.find(':')])
m1 = int(s1[s1.find(':')+1: s1.rindex(':'):])
h2 = int(s2[ :s1.find(':')])
m2 = int(s2[s1.find(':')+1: s2.rindex(':')])
c1 = int(s1[s1.rindex(':') +1: ])
c2 = int(s2[s2.rindex(':')+1: ])

m = m1 + m2
h = h1 + h2
c = c1 + c2
if c >= 60:
    c = c - 60
    m +=1
if 0<c<10:
    c = '0'+str(c)
if c == 0:
    c = '00'
if m >= 60:
    m = m - 60
    h += 1
if 0<m<10:
    m = '0'+str(m)
if m == 0:
    m = '00'
    
if h >= 24:
    h = h -24
if 0<h<10 :
    h = '0'+str(h)
if h == 0:
    h = '00'
    
x =  str(h)+':'+str(m)+':'+str(c)  
print(x)
    