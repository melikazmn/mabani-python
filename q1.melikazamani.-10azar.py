def is_divisible(n , m):
    if n % m == 0 :
        return True
    else :
        return False
    
def valid_rotations(n):
    global count
    z = str(n)
    for i in range(len(z)):
        z = z[i:] + z[:i]
        n = int(z)
        if is_divisible(n , 4) == True:
            count +=1
        
        
count = 0
n = int(input())
valid_rotations(n)
print(count)
