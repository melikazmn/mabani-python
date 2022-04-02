n = int(input())
s = int(input())
count = 0

for i in range(n-1):
    halat_ghabl = s
    s = int(input())
    if s != halat_ghabl:
        count += 1

print(count)