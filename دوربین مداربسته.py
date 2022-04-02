m1= input().split()
m2= input().split()
m3= input().split()

if m1[0] != m2[0]:
    x4 = int(m2[0]) + int(m1[0]) -int(m3[0])
elif m1[0] != m3[0]:
    x4 = int(m3[0]) + int(m1[0]) -int(m2[0])
elif m2[0] != m3[0]:
    x4 = int(m2[0]) + int(m3[0]) -int(m1[0])

if m1[1] != m2[1]:
    y4 = int(m2[1]) + int(m1[1]) -int(m3[1])
elif m1[1] != m3[1]:
    y4 = int(m3[1]) + int(m1[1]) -int(m2[1])
elif m2[1] != m3[1]:
    y4 = int(m2[1]) + int(m3[1]) -int(m1[1])

print(x4,y4)

