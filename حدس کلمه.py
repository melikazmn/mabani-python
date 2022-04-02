name = input()
name = name.lower()
life = 3
s = ''

while life > 0:
    guess = input()
    if guess.lower() not in name:
        life -= 1
        print('wrong.',life,'left.')
    else :
        print('right')
        name = name.replace(guess.lower(),'')
        if name == '' :
            print('Done!')
            break
        
if life == 0:
    print('Failed!')
