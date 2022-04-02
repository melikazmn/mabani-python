def reshte(s):
    k = 1
    while k <= len(s):
        for i in range(len(s) - k+1):
            print(s[i:i+k:])
        k += 1
        
s = input('enter something!  ')
reshte(s)
    