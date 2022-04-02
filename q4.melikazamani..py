k = input()
count = 3
t = 0

while count>0:
    h = input()
    if 64<ord(h[0])<91:
        h = chr(ord(h[0])+32)
    if h in k:
        print('right')
        t+=1
        if t == len(k):
            break
        
    else:
        count = count -1
        print('wrong',count)
        
if count == 0:
    print('failed!''done!')
else:
    print('done!')