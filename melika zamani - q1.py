c = input() #namsherkat
n = input() #esm khodesh
a = input() #narmafzar

k1 = str(ord(n[0]))
for i in range(len(n)):
    if n[i] == ' ':
        k2 = str(ord(n[i+1]))
        break
#kholase nam sherkat
k3 = c[0] + c[len(c)-1] + str(len(c)-2)
#kholase narm afzar
k4 = a[0] + a[len(a)-1] + str(len(a)-2)

print(k1+k2+k3+k4)