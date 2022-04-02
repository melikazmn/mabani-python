pirahan = input().split()
shalvar = input().split()
kafsh = input().split()
res = []

if pirahan == [] or shalvar == [] or kafsh == [] :
    print('')
else:
    for i in range(len(pirahan)):
        for j in range(len(shalvar)):
            for z in range(len(kafsh)):
                res = [pirahan[i],shalvar[j],kafsh[z]]
                print(' '.join(res))
