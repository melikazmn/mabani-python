n = int(input())
matris = []
res = 0
det =0


for i in range(n):
    satr = input().split()
    matris.append(satr)
 
def determinan(matris):
    global res
    global det

    if len(matris) == 2:
        return int(matris[0][0])*int(matris[1][1]) - int(matris[0][1])*int(matris[1][0])
    
    for i in range(len(matris[0])):
        if len(matris) > 3:
            res = 0
            
        matris2 = []
        mat = matris[1:]
        
        for j in mat:
            matris2.append(j[0:i]+j[i+1: :])
        
        res += ((-1)**(i))*int(matris[0][i])*determinan(matris2)
    det = res
    if i == len(matris) - 1:
        return det
    return res
    
print(determinan(matris))