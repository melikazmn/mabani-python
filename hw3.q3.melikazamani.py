def if_snake_case(s):
    if s.find('_') >= 0:
        a = s.replace('_','')
        if a.islower() == True:
            return 'true'
        else :
            return 'false'
    else:
        return 'false'
    
def if_pascal_case(s):
    if s.find('_') >= 0 :
        return 'false'
    elif s.isupper() == True or s.islower == True:
        return 'false'
    else:
        return 'true'
        
def pas_be_snake(s):
    res = ''
    i = 1
    while i < len(s):
        if s[i].isupper() == True:
            res = res + s[ :i].lower() + '_' +s[i].lower()
            s = s[i+1: ]
            i = 0
        else:
            i +=1
    res = res + s
    return res
            
def snake_be_pas(s):
    i = 0
    res = ''
    while i < len(s): 
        if s[i] == '_':
            res = res + s[0].upper() + s[1:i]
            s = s[i+1: ]
            i = 0
        else:
            i += 1
    res = res + s[0].upper() + s[1: ]
    return res
   
    
s = input()
if if_pascal_case(s) == 'true':
   print(pas_be_snake(s))
elif if_snake_case(s) == 'true':
   print(snake_be_pas(s))
else :
    print('invalid input')