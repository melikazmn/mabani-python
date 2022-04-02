n = int(input()) #tedad safar
m = int(input()) #bilit m safare
pm = int(input()) #gheimat m safare
p1 = int(input()) #gheimat tak safare
i = n
    
min = n*p1
while i>=0:
    a =(i//m)*pm + (n-((i//m)*m))*p1
    if a<min :
        min = a
    i = i-1
    
print(min)
    