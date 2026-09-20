"""for loop"""
# s="vedika"
# for i in s:#0,1
#     print("vedika")
# nums = [10, 20, 30, 40, 50]
# for a in nums:
#     print(a)
"""range()"""
# for i in range(5):# (0- 4(range-1)
#     print(i)
# print("out of for loop")
# for i in range(1,5):
#     print(i)
# print("out of for loop")
# for i in range(0,10,2):
#     print(i)
# print("out of for loop")
# for i in range(5,0,-1): # (start , end , skip)
#     print(i)
# print("out of for loop")

# WAP to print first 10 integers and their squares
"""for i in range(1,11):
    s=i*i
    print(i,s)"""
"""for i in range(1,11):
    print(i,i**2)
    """

# WAP to print the table of the number entered from the user
"""number=int(input('enter a number: '))
for i in range(1,11):
    print(i,i*number)"""

# WAP to print even numbers falls between two numbers these two numbers will be taken from user
"""one=int(input('enter a number: '))
two=int(input('enter a number: '))
for i in range(one,two):
    if i%2==0:
        print(i)"""

# Count the number of digits in a given number using a for loop without using the len function.*************************************
'''digit=int(input('enter a number: '))
str_digit=str(digit)
count=0
for i in str_digit:
    count+=1
print(count)'''


# Find the sum of digits of a given number.
"""digit=int(input('enter a number: '))#1234
string=str(digit)
sum=0
for i in string:
    i=int(i)
    sum=i+sum
print(sum)"""

# Write a Python program using a for loop to find and print all the vowels in your name.
'''name=input('enter your name: ')#vedika
for i in name:
    if i in 'aeiou':
         print(i)'''

# Write a Python program using a for loop to find and print all the consonants in your name.

"""name=input('enter your name: ')
for i in name:
    if i not in 'aeiou':
        print(i)"""

# Find the multiplication of digits of a given number.

"""digit=int(input('enter a number: '))#1234
string=str(digit)
product=1
for i in string:
    i=int(i)
    product=i*product
print(product)"""

# WAP to print the sum of all the even numbers falling between two numbers these two numbers will be taken from user

"""one=int(input('enter a number: '))
two=int(input('enter a number: '))
sum=0
for i in range(one,two):
    if i%2==0:
        sum=sum+i
print(sum)"""

# Write a Python program using a for loop to count and print all the vowels in the string.

"""word=input('enter a word: ')#vedika
count=0
for i in word:
    if i in 'aeiou':
        print(i)
        count=count+1
print(count)"""

# WAP to print the sum of all the even and odd numbers falling between two numbers these two numbers will be taken from user

"""one=int(input('enter a number: '))
two=int(input('enter a number: '))
sum=0
sumo=0"""
# for i in range(one,two):
#     sum=sum+i
# print(sum)
"""for i in range(one,two+1):
    if i%2==0:
        sum+=i
    else:
        sumo+=i
print(sum)
print(sumo)
print(sum+sumo)
"""
"""break keyword"""
# for i in range(1, 5):
#     if i  >2: #
#         break
#     print(i)
# print("out of for loop")
"""continue"""
# for i in range(1, 5):# 1,2,3,4
#     if i == 3:# 3==3
#         continue
#     print(i)#1,2,4
#     print("vedika")
# print("out of for loop")
# for i in range(1, 5):#
#     if i > 3:#
#         continue
#     print(i)#
# print("out of for loop")
# for i in range(2):
#     print(i)
# else:
#      print('End of for loop')
"""nested for loop"""
# for x in range(1,4): # 1-3     1    2    3
#     for y in range(1,3):#1-2   1,2  1,2  1,2
#         print('x = ', x, ', y = ', y)
#11,12,21,22,31,32
# for x in range(1,4):
#     for y in range(1,3):
#         for z in range(1,2):
#             print('x = ', x, ', y = ', y,'z = ', z)
#111,121,211,221,311,321

# Write a program that asks for a word and prints each letter until it finds the letter 'a', then break.
"""word=input('enter a word: ').lower()
for i in word:
    if i=='a':
        break
    print(i)"""

# Loop through characters of your name and skip repeating letters (if any).
"""name=input('enter your full name: ')#hello
empty=''#empty=helo
for i in name:
    if i in empty:
        continue
    empty+=i
    print(i)"""


# Print all letters of a word, but skip vowels
"""word=input('enter a word: ')
for i in word:
    if i in 'aeiou':
        continue
    print(i)
"""

# Print all numbers from 1 to 100, but stop when the number becomes divisible by 13.
"""for i in range(1,101):
    if i%13==0:
        break
    print(i)
"""

# Loop through numbers from -10 to 10 and print only positive numbers.
"""for i in range(-10,11):
    if i<1:
        continue
    print(i)"""

# 3. Ask for characters one by one (use input() inside a for loop) and stop when the user enters 'q'.
"""for i in range(10):
    char=input('enter a random letter: ').lower()
    if char=='q':
        break
    print(char)"""

# HOMEWORK
# 1. Print numbers from 1 to 20, but skip odd numbers.
"""for i in range(0,21,2):
    print(i)"""
#second methond
"""for i in range(1,21):
    if i%2!=0:
        continue
    print(i)"""
# 2.Ask the user to enter 5 numbers. Stop asking as soon as they enter a negative number.
"""for i in range(10):
    number=int(input('enter a number: '))
    if number<0:
        break
    print(i)"""
# 3.Print numbers from 1 to 20, but skip the multiples of 3.
"""for i in range(1,21):
    if i%3==0:
        continue
    print(i)"""
# 4. Loop through a sentence and skip punctuation marks.
"""sen=input('enter a sentence: ').lower()#vedika
for i in sen:
    if i in '=%";,/?.-_!':
        continue
    print(i)"""
# anothe method
"""sen=input('enter a sentence: ').lower()
for i in sen:
    if i not in 'qwertyuiopasdfghjklzxcvbnm':
        continue
    print(i)"""
# another method
"""sen=input('enter a sentence: ').lower()
for i in sen:
    if not i.isalpha():
        continue
    print(i)"""

# 5. Loop through a list of names and skip any name shorter than 4 letters.
"""lis=['vedika','ayda','man','sam','akarshi']
for i in lis:
    if len(i)<4:
        continue
    print(i)"""
# Loop through numbers from -10 to 10 and print only negative numbers.
"""for i in range(-10,11):
    if i>-1:
        continue
    print(i)"""

# 2. Print all characters of a word, but skip digits (like '3', '5', etc.). EXAMPLE:HELLO123HI output: hellohi
"""string='HELLO123HI'.lower()
for i in string:
    if i.isdigit():
        continue
    print(i,end='')"""

# Print squares of numbers from 1–20, but break when the square exceeds 200.
"""for i in range(1,21):
    i = i ** 2
    if i>200:
        break
    print(i)"""

"""var=int(input('enter a number: '))
for i in range(var):
    print('* '*var)"""

"""var=int(input('enter a number: '))
for i in range(1,var+1):
    print('* '*i)"""

"""var=int(input('enter a number: '))
for i in range(var,0,-1):
    print('* '*i)"""
#
# var=int(input('enter a number: '))
# for i in range(1,var+1):
#     for i in range(var,0,-1):
#        print(' '+'* '*i+' ')

"""
var=int(input('enter a number: '))
for i in range(var,0,-1):
    # print(' '+'* '*i+' ')
    print(' '*(var-i)+'* '*i)"""
#   *
#  * *
# * * *
#* * * *


"""var=int(input('enter a number: '))
for i in range(1,var+1):
    print(' '*(var-i)+'* '*i)
# print('* '*(var+1))
for i in range(var-1,0,-1):
    print(' '*(var-i)+'* '*i)"""

# 1
# 12
# 123
# 1234
# 12345

"""var=int(input('enter a number: '))#4
num=1
for i in range(1,var+1):#1-5   1      2
    for j in range(1,i+1):#1-1 1  1-2 1
       print(j,end='')
    print()"""

# A
# AB
# ABC
# ABCD
# ABCDE

# var=int(input('enter a number: '))#4
"""al='abcdefghijklmnopqrstuvwxyz'
for i in range(0,6):#a       a  b
    for j in range(0,i+1):#a b  a  b
        print(al[j],end=' ')
    print()"""
