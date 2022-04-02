
tedad_s = int(input())
ticket_m = int(input())
price_ticket_m = int(input())
price_one_way = int(input())

minn = price_one_way *tedad_s

for i in range(tedad_s//ticket_m + 2):
    if i == tedad_s//ticket_m + 1:
        price = i*price_ticket_m
        if price < minn:
            minn = price
        
    else:
        tedad_one_way = tedad_s - i*ticket_m
        price = tedad_one_way*price_one_way + i*price_ticket_m
        if price < minn:
            minn = price
        
print(minn)
       
