def is_sorted(lst):

    for i in range(len(lst)):
        for j in lst[i+1:]:
            if lst[i] <= j:
                soudi = True
            else:
                soudi = False
                break
    
    if soudi == True:
        return 1
    
    else:
        for i in range(len(lst)):
            for j in lst[i+1:]:
                if lst[i] >= j:
                    nozuli = True
                else:
                    nozuli = False
                    return 0
                    
        if nozuli == True:
            return -1

                