block_color = input().split()
R = int(block_color[0]) #black
B = int(block_color[1])  #yellow

zard = (R//2)-2

for WB in range(1,zard):
    LB = zard - WB
    L = LB + 2
    W = WB + 2
    masahat = L*W
    if LB > 0 and WB > 0 and masahat == R+B:
        break
          
print(L,W)