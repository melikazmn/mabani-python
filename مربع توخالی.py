a = int(input())
b = int(input())

if a <= b:
    print("Wrong order!")

elif (a - b) % 2 != 0:
    print("Wrong difference!")

else:
    z = (a - b) // 2
    for i in range(z):
        print((a - 1) * "* " + "*")
    for j in range(b):
        print(z * "* " + (2 * (a - (2 * z)) - 1) * " " + z * " *")
    for p in range(z):
        print((a - 1) * "* " + "*")
