n = int(input())
b = ''
count = 0
tedad = 0

for i in range(n):
    a = input()
    count = 0
    for s in range(len(a)):
        if a[s] in b :
            s += 1
        else:
            count += 1
            b = b + a[s]
    if tedad > count:
        khoroji = tedad
    else:
        khoroji = count
    tedad = khoroji
    b = ''
print(khoroji)
        