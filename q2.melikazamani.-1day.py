def kulatz(n):
    if n == 1:
        return str(n)
    if n%2 == 0:
        return  str(n)+' ' + str(kulatz(n//2))  
    if n!=1 and n%2 == 1:
       return str(n)+ ' ' + str(kulatz((3*n)+1)) 
    
n = int(input())    
print(kulatz(n))