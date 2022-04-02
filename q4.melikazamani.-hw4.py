vorodi = input().split()
matris1 = []
matris2 = []
count1 = count2 = new_deraye = 0
deraye_ha = []

for i in range(int(vorodi[0])):
    satr1 = input().split() 
    matris1.append(satr1)

for j in range(int(vorodi[1])):
    satr2 = input().split()
    matris2.append(satr2)

for z in range(int(vorodi[0])):
    for x in range(int(vorodi[2])):
        for y in range(int(vorodi[1])):
            new_deraye += int(matris1[count1][y])*int(matris2[y][count2])
        deraye_ha.append(str(new_deraye))
        new_deraye = 0
        count2 += 1
    count1 += 1
    count2 = 0
    print(' '.join(deraye_ha))
    deraye_ha = []
 

