
def feshorde(s):
    alpha = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    count = 1
    res = ''
    
    for i in range(len(s)):

        if i < len(s)-1 and s[i] in alpha and s[i] == s[i+1]:
            count += 1
        elif i == len(s) - 1 and s[i] != s[i-1] and s[i] in alpha:
            res += s[i] + str(1)     
        elif s[i] in alpha :
            res += s[i] + str(count)
            count = 1
            
    return res

s = input()
if s != '':
    while s != '':
        print(feshorde(s))
        s = input()
        
        
        
        