def barnamenevis(dic):
    maxx = 1
    dict_find_max = {}
    final_dic = {}
    val = {}
    
    for i in dic.values():
        for j in i.keys():
            if j in dict_find_max:
                dict_find_max[j] += 1
            else:
                dict_find_max[j] = 1
                
    for x in dict_find_max:
        if dict_find_max[x] > maxx:
            maxx = dict_find_max[x]
            max_key = x
            
    for key in dic.keys():
        if max_key in dic[key].keys():
            
            for z in dic[key].keys():
                
                if z != max_key:
                    val[z] = (dic[key])[z]
                else:
                    k = (dic[key])[z]
                    val[z] = key
                
            final_dic[k] = val 
            val = {}
            
    return final_dic
             

dic = {
 "405": {"owner": "Ahmad Ahmadian", "brand": "peg", "model": "7324"},
 "206": {"owner": "Mohammad Mohammadian", "color": "white", "model":
"213"},
 "504": {"brand": "bugg", "tires_type": 342},
 "207": {
 "is_sd": True,
 "checker": "Jaber Jabbarian",
 "color": "black",
 "model": "AT23",
 },
}

print(barnamenevis(dic))