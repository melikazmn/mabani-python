s1 = input()
s2 = input()

h1 = int(s1[ :s1.find(':')])
m1 = int(s1[s1.find(':')+1: ])
h2 = int(s2[ :s1.find(':')])
m2 = int(s2[s1.find(':')+1: ])

m = m1 + m2
h = h1 + h2
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
    
print(h,':',m)
    