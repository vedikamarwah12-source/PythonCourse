import random

# random number between 0 and 1
print(random.random())

#random number between a range
print(random.randint(2,8))

#random number between range as float
print(random.uniform(1,10))

#random selection
color=['cyan','magenta','sunny yellow','sky blue']
print(random.choice(color))

#random choices
print(random.choices(color,k=2))

import math

#square root
print(math.sqrt(4))

#fcf or gcd
print(math.gcd(14,28,56))

#lcm
print(math.lcm(14,28,56))

#ceil= removes decimal and adds 1
print(math.ceil(1.56))

#floor= only removes decimal
print(math.floor(1.25))

#fabs= converts to positive and gives answer in float
print(math.fabs(-4))

#copysign= copies sign of next number and converts to float
print(math.copysign(12,-3))

#pow= gives exponential power and in float
print(math.pow(2,5))

#fsum=adds all in float
num=[45,50,5]
print(math.fsum(num))

import random
while True:
    choice=random.randint(0,9)
    num=int(input('enter a number between 0 and 9: '))
    if num == choice:
        print('thats correct')
    else:
        print('sorry try again','the number was: ',choice)

import random

point = 0
while point<4:
    obj=('rock','paper','scissor')
    choice=random.choice(obj)
    user=input(('enter your choice: ')).lower()
    if user=='rock':
        if obj=='rock':
            print('tie',choice)
        elif obj=='scissor':
            print('you won',choice)
            point+=1
        else:
            print('you lost',choice)
    elif user=='paper':
        if obj=='rock':
            print('you won',choice)
            point+=1
        elif obj=='scissor':
            print('you lost',choice)
        else:
            print('tie',choice)
    elif user=='scissor':
        if obj=='rock':
            print('you lost',choice)
        elif obj=='scissor':
            print('tie')
        else:
            print('you won',choice)
            point+=1
    else:
        print('incorrect input try again')
print(point)