# print("MY SHOPPING LIST")
# print("   ")
# print("t-shirt")
# print("shoes")
# print("watch")
# print("socks")
# print("bag")
# print("phone cover")
#
# choice= input(' enter your choice: '.lower())
# quan=int(input(' enter the quantity of what you are buying: '))
#
# if choice=='t-shirt':
#     price=20
#     total=price*quan
#     print('your total amount is:$',total)
#
# elif choice=='shoes':
#     price=70
#     total=price*quan
#     print('your total amount is:$',total)
#
# elif choice=='watch':
#     price=50
#     total=price*quan
#     print('your total amount is:$',total)
#
# elif choice=='socks':
#     price=40
#     total=price*quan
#     print('your total amount is:$',total)
#
# elif choice=='bag':
#     price=20
#     total=price*quan
#     print('your total amount is:$',total)
#
# elif choice=='phone cover':
#     price=2
#     total=price*quan
#     print("your total amount is:$")
#
# else:
#     print('your input is invalid!'.upper())


print('____________________')
print('GEOGRAPHY QUIZ')
print('   ')

score=0
print('QUESTION 1-\nIN WHICH CONTINENT IS EGYPT LOCATED IN?')
print('A.asia\nB.africa\nC.europe\nD.south america')
ans=input(" Choose the correct option: ").upper()

if ans=='B':
    score=0+1
    print('YES THIS IS THE RIGHT ANSWER!')
else:
    print(' SORRY THE CORRECT ANSWER WAS B\nEGYPT is located just bordering Asia which '
          'is to the north-east of Africa')

print('QUESTION 2-\nWHICH IS THE LARGEST FRESHWATER LAKE IN THE WORLD?')
print('A.Lake Superior\nB.Wular Lake\nC.Lake Tahoe\nD.Lake Baikal')
ans=input(" Choose the correct option: ").upper()

if ans=='D':
    score=score+1
    print('YES THIS IS THE RIGHT ANSWER!')
else:
    print(' SORRY THE CORRECT ANSWER WAS D\n Lake Baikal is the '
          'worlds,deepest, largest and oldest freshwater lake located in russia')

print('QUESTION 2-\nWHICH COUNTRY DOES NOT BORDER LAOS?')
print('A.MYANMAR\nB.VIETNAM\nC.CAMBODIA\nD.THAILAND')
ans=input(" Choose the correct option: ").upper()

if ans=='A':
    score=score+1
    print('YES THIS IS THE RIGHT ANSWER!')
else:
    print(' SORRY THE CORRECT ANSWER WAS A\n LAOS has 3 bordering countries-VIETNAM,CAMBODIA and THAILAND. ')
print('YOUR FINAL SCORE IS: ',score)