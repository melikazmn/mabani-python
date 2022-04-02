#n = int(input())
#x = 1
#{1,2,3}
#print('{}')
#for i in range(1,n+1):
#    print('{',i,'}')
    
#while x<=n:
 #   for i in range(x+1,n+1):
  #      print('{',x,i,'}')
    #    
   # x +=1
n = int(input())
max1 = n
max2 = 0
if n>=10:
    fail = 0
else:
    fail = 1
sum = n
i = 1
while n!= -1:
    n = int(input())
    if n == -1:
        break
    sum = sum + n
    i = i + 1
    if n<10:
        fail +=1
    if n>max1:
        max2 = max1
        max1 = n
    elif max2<n<max1:
        max2 = n
        
print(sum/i)
print('max1:',max1)
print('max2:',max2)
print(fail)