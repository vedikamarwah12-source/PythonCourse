import random
print('*********ROCK PAPER SCISSORS*********')
options=['rock','paper','scissors']
score1=0
score=0

while score1<3 and score<3:
  comp = random.choice(options)
  user = input('enter your hand position: ').lower()
  print('the computer chose: ', comp)
  if user==comp:
    print('its a tie!')

  elif user=='scissors' and comp=='rock':
    print('the computer wins!')
    score=score+1
    print('your score is: ',score1)
    print("the computer's score is: ",score)

  elif user=='rock' and comp=='paper':
    print('the computer wins!')
    score=score+1
    print('your score is: ',score1)
    print("the computer's score is: ",score)

  elif user=='rock' and comp=='scissors':
    print('you win!')
    score1=score1+1
    print('your score is: ', score1)
    print("the computer's score is: ", score)

  elif user=='paper' and comp=='scissors':
    print('you win!')
    score1=score1+1
    print('your score is: ', score1)
    print("the computer's score is: ", score)

  elif user=='paper' and comp=='scissors':
    print('the computer wins!')
    score=score+1
    print('your score is: ', score1)
    print("the computer's score is: ", score)

  elif user=='scissors' and comp=='paper':
    print('you win!')
    score1=score1+1
    print('your score is: ', score1)
    print("the computer's score is: ", score)

  elif user == 'paper' and comp == 'rock':
    print('you win!')
    score1 = score1 + 1
    print('your score is: ', score1)
    print("the computer's score is: ", score)

  else:
    print('incorrect input try again')

print("your total score is: ",score1)
print("the computer's total score is: ",score)
if score>score1:
    print('the computer wins!')
else:
    print('you win!')



