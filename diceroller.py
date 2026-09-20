import random
while True:
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    a=(input('enter the number that how many dice you want to roll: ')).lower()
    if a=='q':
        print('thank you!')
        break
    elif a=='2':
        print('you rolled: ', dice1, dice2)
    elif a=='1':
        print('you rolled: ', dice1)
    else:
        print('incorrect input')