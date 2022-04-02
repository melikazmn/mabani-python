n = input()
z = int(n)
max = 0

def hazf_tekrar(n):
    s = ''
    for i in range(len(n)):
        if n.count(n[i]) == n[i]:
            i += 1
        if n.count(n[i]) > 1 and n.count(n[i]) != n[i]:
            s = n[i] + n.count(n[i])
            n = n.replace(n[i],'')
        print(s)
    return s

def soudi(s):
    for j in range(len(s)):
        for x in range(z):
            a = z % 10
            if a >= max:
                max = a
            z = z//10
        soudi = str(max) + soudi
        print(soudi)
    return soudi

def nahaye(soudi):
    global n
    global s
    s = hazf_tekrar(n)
    n = int(soudi(s)) 
    for y in range(n):
        if n.count(n[i]) == n[i]:
            i += 1
        else :
            hazf_tekrar(n)
            soudi(s)
    print(soudi)

nahaye(soudi)