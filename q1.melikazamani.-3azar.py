n = int(input())
x = 0
y = 0
while n>0:
    a = input()
    x = int(a[a.find('(')+1 : a.find(',')]) + x
    y = int(a[a.find(' ')+1 :a.find(')') ]) + y
    n = n-1
z = 'point('+ str(x)+', '+str(y)+')'
print(z)