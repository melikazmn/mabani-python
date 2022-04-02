n = int(input())
if n%2 == 0:
     k = n//2
else:
    k = n//2 + 1
    
count = 0
summ = 0

def kashikari_sorat(n):
    global k
    if n == 1:
        return 1
    return (n)*kashikari_sorat(n-1)

def kashikari_makhraj(count):
    if count == 0:
        return 1 
    return kashikari_makhraj(count-1)*(count)

for i in range(k,n+1):
    summ += (kashikari_sorat(n) // (kashikari_makhraj(count)*kashikari_makhraj(n-count))) 
    n = n-1
    count += 1

print(summ)