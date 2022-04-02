def paskal_soorat(n):
    if n-1 == 1 or n-1 == 0:
        return 1
    else:
        return (n-1)*paskal_soorat(n-1)
 
def paskal_makhraj1(k):
    if k == 1 or k == 1:
        return 1
    else:
        return (k)*paskal_makhraj1(k-1)

def paskal_makhraj2(x):
    if x == 1 or x == 0:
        return 1
    else:
        return (x)*paskal_makhraj2(x-1)


n = int(input())
k = int(input())
if n == k:
    print(1)
else:
    res = (paskal_soorat(n)//(paskal_makhraj1(k)*paskal_makhraj2(n-1-k)))+(paskal_soorat(n)//(paskal_makhraj1(k-1)*paskal_makhraj2(n-k)))
    print(res)


