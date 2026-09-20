"""function""" # name() => print(),len(),sum ()
"""method""" # varaible_name.method_name()

# def fun_name():
#     print("vedika")
#     print(2)
# fun_name() # calling

"""function with parameters"""
# def hello():
#     print("hi","ankita")
# hello()
# hello()
# hello()
# def welcome():
#     print ('Hello ', "vedika")

# welcome() # calling function with argument
# welcome()

# def welcome(name):  #name = x = "ankita
#     print ('Hello', name)

# welcome('James Bond') # calling function with argument
# welcome(15)
# name = "vedika"
# welcome(name)
# x="ankita"
# welcome(x)

"""retrun function"""
# def addition(a,b):
#     print("fucntion to add 2 values")
#     c = a + b
#     print(c)

# a = 10
# b = 20
# addition(a,b)
# d = a + c
# print(d)
# def addition(a,b):
#     print("fucntion to add 2 values")
#     c = a + b
#     return c
#
# a = 10
# b = 20
# output = addition(a,b) # output= c
# d = a + output
# print(d)
# print(addition(a,b))
# def addition(a, b):
#     print("fucntion to add 2 values")
#     c = a + b
#     return c
#     print("vedika")
#     print("hi")
#
#
# print(addition(10, 20))
# print("ankita")

# 1. Write a function to check if a number is even.
'''
def even(a):
    if a%2==0:
        print('even')
    else:
        print('odd')
a=int(input('enter a number: '))
even(a)'''

# 3. Return the first character of the string.
'''def first(str):
    return str[0]
str=input('enter a word: ')
print(first(str))'''

# 8. Write a function to count vowels in a string.
'''def vowel(str):
    count = 0
    for i in str:#v
        if i in 'aeiou':
            count+=1
    return count
str=input('enter a word: ')
print(vowel(str))'''

# 11. Function to count how many times a character appears in a string
'''def count(str):
    return str.count(s)

str=input('enter a word: ')#apple
s=input('enter a letter: ')#p
print(count(str))'''


# HOMEWORK
# 4. Write a function to return the maximum of two numbers.
'''def more(a,b):
    return max(a,b)
a=int(input('enter number: '))
b=int(input('enter number: '))
print(more(a,b))
'''
# 6. Write a function to reverse a string.
'''def rev(str):
    return(str[::-1])
str=input('enter a word: ')
print(rev(str))'''

# 8. Write a function to count vowels in a string.
'''def cnt(str):
    count=0
    for i in str:
        if i in 'aeiou':
            count+=1
    return count
str=input('enter word: ')
print(cnt(str))'''

#return sum(1 for char in s if char in vowels)


# 9. Function to calculate the area of a rectangle
'''def area(l,b):
    return l*b
l=int(input('enter length: '))
b=int(input('enter breadth: '))
print(area(l,b))'''


# 10. Function to check if a string is a palindrome
'''def pal(str):
    if str[0:]==str[::-1]:
        return 'palindrome'
    else:
        return 'not'
str=input('enter word: ')
print(pal(str))'''
'''
def pal(str):
    return str[0:]==str[::-1]

str=input('enter word: ')
print(pal(str))'''


# Problem 1
#  Write a function is_even_two_digit_number that checks whether a given number is an even two-digit number.
# <!-- A number is considered a two-digit number if it has exactly two digits excluding any negative
# sign.
# NOTE: This is a function type question, you don't have to take input or print the output, just have
# to complete the required function definition.
# For example:
# 24 is an even two-digit number.
# -36 is an even two-digit number.
# 5 is not a two-digit number.
# 101 is not a two-digit number.
# -19 is not an even number.  -->

'''def ev2(num):
    return num%2==0 and num>9 or num<-9
num=int(input('enter number: '))
print(ev2(num))'''

# write a function which takes an email input and if the email ends with .com or .in . The function should return True
# if the domain has the specified suffix;
#  otherwise, it should return False .
# Examples
# 1. is_dot_com_or_dot_in("example.com") -> True
# Explanation: The domain ends with .com .
# 2. is_dot_com_or_dot_in("website.in") -> True
# Explanation: The domain ends with .in .
# 3. is_dot_com_or_dot_in("mydomain.org") -> False
# Explanation: The domain does not end with .com or .in . 4.
# is_dot_com_or_dot_in("invalidcom") -> False
# Explanation: The domain does not end with .com or .in .

'''def gm(email):
    return email[-4:]=='.com' or email[-3:]=='.in'

email=input('enter email: ')
print(gm(email))'''

'''def gm(email):
    return email.endswith('.com') or email.endswith('.in')

email=input('enter email: ')
print(gm(email))'''

#wap(function) to compute length of a string entered
'''def lnt(str):
    count=0
    for i in str:
        count+=1
    return count
str=input('enter string: ')
print(lnt(str))'''

#wap to identify a 10 digit even number
'''def evtn(num):
    return len(str(num))==10 and num%2==0
num=int(input('enter number: '))
print(evtn(num))'''





