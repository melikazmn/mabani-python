barkod = []
count = 1
    
for i in range(9):
    l = input()
    barkod.append(l)
    
def check(barkod):
    for i in [0,2,6,8]:
        if barkod[i][0:3].find('0')>-1 or barkod[i][6:9].find('0')>-1:
            return True
    for j in [1,7]:
        if barkod[j][0] == '0' or barkod[j][2] == '0' or barkod[j][8] == '0' or barkod[j][6] == '0':
            return True
        if barkod[j][1] == '1' or barkod[j][7] == '1':
            return True
    return False

        
if check(barkod) == True:
    print('0')
    
else:    
    for x in range(3):
        line =  barkod[x][3:6]
        if line.find('2') >-1:
            count = count*(2**(line.count('2')))
            
    for j in range(3,6):
        if barkod[j].count('2') >0:
            count = count*(2**(barkod[j].count('2')))
            
    for z in range(6,9):
        line =  barkod[z][3:6]
        if line.find('2') >-1:
            count = count*(2**(line.count('2')))
            
    print(count)