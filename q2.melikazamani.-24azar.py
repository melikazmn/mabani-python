def reverse(s):
    s = s[ : :-1]
    return s

def compare(strig_ali,strig_salib):
    while  len(strig_salib) > 0 and   len(strig_ali) > 0 :
        if strig_salib[0] > strig_ali[0]:
            strig_ali = strig_ali[1:]
            strig_ali = reverse(strig_ali)
            strig_salib = reverse(strig_salib)
            
        elif strig_salib[0] < strig_ali[0]:
            strig_salib = strig_salib[1:]
            strig_ali = reverse(strig_ali)
            strig_salib = reverse(strig_salib)
            
        elif strig_salib[0] == strig_ali[0]:
            strig_ali = strig_ali[1:]
            strig_salib = strig_salib[1:]
            strig_ali = reverse(strig_ali)
            strig_salib = reverse(strig_salib)
    
    if len(strig_ali)>0:
       return strig_ali[ : :-1] 
                
    elif len(strig_salib)>0:
        return strig_salib[ : :-1] 
    
    else:
       return 'Both strings are empty!'
    
print(compare('ali','reza'))
