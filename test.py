# Given s = "Traversal", print the string except the first 2 and last 2 characters.
# s = "Traversal"
# print(s[2:-2])

# 3.Create a string variable containing "!!!python is FUN!!!". Remove the  exclamation marks from the left side only, convert it to lowercase,
# and then replace "fun" with "awesome"

# srt="!!!python is FUN!!!"
# print(srt.lstrip('!').lower().replace('fun','awesome'))

#2 Input a character.
# Check if it is vowel, consonant, or not a letter.
# s=input('enter a letter: ').lower()
# if s.isdigit():
#     print('digit')
# elif s in 'aeiou':
#     print('vowel')
# elif s.isalnum():
#     print('consonant')
# else:
#     print('special character')
#method 2:
# s=input('enter a letter: ').lower()
# if s.isdigit():
#     print('digit')
# elif s in 'aeiou':
#     print('vowel')
# elif not s.isalnum():
#     print('special character')
# else:
#     print('consonant')

# Take a string and count how many digits it contains.
#     Example
#     Input:
#     abc123xy9

digit='abc123xy9'
# t=[]
# for i in digit:
#     if i.isalpha():
#         continue
#     else:
#         t.append(i)
# print(len(t))
# method 2:
# digit='abc123xy9'
# count=0
# for i in digit:
#     if i.isdigit():
#         count+=1
# print(count)

# Use a while loop to sum all even and odd numbers between two numbers taken from the user

'''one=int(input('enter a number: ')) #1
two=int(input('enter a number: ')) #10
i=one
even=0
odd=0
while i<=two:#1<10,
    if i%2==0:
        even+=i
    else:
        odd+=i
    i+=1
print(even)
print(odd)'''


#Print numbers from 1 to 10, but skip even numbers
'''for i in range(1,11):
    if i%2==0:
        continue
    print(i)'''
'''i=0
while i<10:
    i+=1
    if i%2==0:
        continue
    print(i)'''


# 2 Keep asking the user to enter a number. If the number is negative, stop the loop using break.
'''while True:
    num = int(input('enter a number: '))
    if num<0:
        break'''

# HOMEWORK ########################################################################
# Print characters of a string, skip vowels.
'''str=input('enter a word: ')
for i in str:
    if i in 'aeiou':
        continue
    print(i)'''


# Write a loop that continues asking the user to enter a number until they type 0. Then, print the multiplication of all numbers entered.
'''while True:
    num = int(input('enter a number: '))
    if num==0:
        break
    else:
        for i in range(1,11):
            print(num*i)'''

# 3 Create a list: [1, 2, 3, 4, 5, 6]
# Print only the middle 3 elements using slicing
l=[1, 2, 3, 4, 5, 6]
'''print(l[2:5])'''
# Replace the first 2 elements with 10, 20
# l[0]=10
# l[1]=20
'''l[:2]=10,20
print(l)'''
# Remove elements from index 2 to 4********************************
'''print(l.pop(2))
print(l.pop(3))
print(l.pop(4))'''
# Add 100, 200 at the end of the list**************************
'''l.append(100)
l.append(200)
print(l)'''

# Reverse the list
'''print(l[::-1])'''
# 4- Write a program to count how many positive and negative numbers are in the list.
'''n=[]
p=[]
s=[4, -1, 9, -6, 0, 3]
for i in s:
    if i<0:
        n.append(i)
    elif i>0:
        p.append(i)
    else:
        continue
print(len(n))
print(len(p))'''

# 5- Take an integer input and check:
# If the number is positive
# If even → print "Positive Even"
# Else → print "Positive Odd"
# Else if negative
# If even → print "Negative Even"
# Else → print "Negative Odd"
'''num=int(input('enter a number: '))
if num>0:
    if num%2==0:
        print('positive even')
    else:
        print('positive odd')
elif num<0:
    if num%2==0:
        print('negative even')
    else:
        print('negative odd')
else:
    print('zero')'''





