lst = input().split()

while len(lst) != 1:
    res = []
    for i in range(len(lst)-1):
        res.append(int(lst[i])+int(lst[i+1]))
    lst = res

print(str(lst[0]))