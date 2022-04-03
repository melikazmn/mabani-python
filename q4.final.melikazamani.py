def String_mult(stg,n):
    lst = []
    for i in stg:
        lst += [int(i)*n]
    
    return lst

stg = input()
n = int(input())
print (String_mult(stg,n))