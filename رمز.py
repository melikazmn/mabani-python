k = input()
ramz = input()
count = 0 

for i in range(int(k)):
    charkhe = input()
    if charkhe.find(ramz[i]) <= (charkhe[::-1].find(ramz[i])+1):
        count += charkhe.find(ramz[i])
        
    else:
        count += charkhe[::-1].find(ramz[i]) +1
print(count)

'''

for i in range(int(k)):
    charkhe = input()
    if charkhe.find(ramz[i]) <= 9//2:
        count += charkhe.find(ramz[i])
        
    else:
        count += 9 - charkhe.find(ramz[i])
print(count)
'''