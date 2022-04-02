def reshte(n):
    if n == 1:
        return n
    return str(reshte(n-1))+ ' '+ str(n)

def reshte_barax(n):
    if n == 1:
        return 1
    return str(n) + ' ' + str(reshte_barax(n-1)) 

n = int(input())
print(reshte(n))
print(reshte_barax(n))