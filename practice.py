n = input()
s = ''

for i in range(len(n)):
    if 96<ord(n[i])<123:
        s = s + chr(123-(ord(n[i])-96))
    elif 64<ord(n[i])<91:
        s = s + chr(91-(ord(n[i])-64))
    else:
        s = s + n[i]
        
def inverse(x):
    x = str(x)
    for i in range(len(x)):
        x = x[len(x)-1:len(x)] + x[ :len(x)-1]
    return x
      
print(inverse(s))
        