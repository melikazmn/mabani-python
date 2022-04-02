def entegham(s , k):
    for i in range(len(s)):
        a = s[i :k+ i:]
        b = s[k+i: : ]
        if b.find(a) >= 0:  
            b = b.replace(b[b.find(a): k + b.find(a): ],'')
            s = s[ :i+ k:] + b
            break   
    print(s)
    
s = input('matn entegham ro benevis   ')
k = int(input('tedad caracter kharabkari ro benevis  '))
entegham(s , k)