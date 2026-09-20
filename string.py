#
# """string"""
# s="hi"
#
# print(s,type(s))
# s='hello'
#
# print(s,type(s))
# s=bye
# how r u
# i'm good
#
# print(s,type(s))
# str1='Welcome to "Python Clas" BCA Students'
#
# print(str1)
# str2="Welcome to 'Python Class' BCA Students"
# print(str2)
# s="hello world"
#
# print(len(s)) # 11
# """positive indexing""" # 0-(len-1)
# s="hello world" # 0-10(len-1) (11-1)
#
# print(s[3])
# """negative indexing""" #(-len)-(-1)
# s="hello world"

# print(s[-5])
# """slicing""" # s[starting : (ending-1)]
s="hello world" # 0-10
#
# print(s[1:5]) #s[1:4] e:o
# print(s[1:11])# s[1:10]
# print(s[-11:-1])# s[] h-
# print(s[-8:-4])#
# print(s[-11:11])
"""print(s[10:1])
print(s[:4])"""
# print(s[1:])
# print(s[:])
# """slicing""" # s[starting : (ending-1) : skip]
# s="hello world"

# print(s[::2])
# print(s[::3])
# print(s[::-1]) # to reverse a string
# 1 Given s = "Python", print the first and last characters.
"""s='python programming'
print(len(s))
print(s[0],s[17])
print(s[-1])"""
# 5 Given s = "Indexing", print the last 3 characters
"""s = "Indexing"
print(s[-3:])"""

"""HOMEWORK
2 Given s = "Programming", print the 3rd to 7th characters.
3 Given s = "HelloWorld", print the string in reverse order.
4 Given s = "Computer", print every 2nd character.
6 Given s = "Artificial", print all characters except the first and last.
7 Given s = "Languages", print the middle three characters.
8 Given s = "DataScience", print the substring "Science" using slicing.
9 Given s = "abcdefg", print "gfedc" using slicing only.
Given s = "IndexSlicing", print the string from right to left skipping 2 characters each time.
Given s = "abcdefgh", print "aceg" and "bdfh" using slicing."""
"""
s = "abcdefgh"
print(s[0::2])
print(s[1::2])

s = "Programming"
print(s[4:8])

s = "HelloWorld"
print(s[::-1])

s = "Computer"
print(s[0::2])

s = "Artificial"
print(s[1:-2])

s = "Languages"
print(s[3:6])

s = "DataScience"
print(s[4:])

s = "abcdefg"
print(s[:1:-1])

s = "IndexSlicing"
print(s[::-2])"""
"""
# Given s = "Traversal", print the string except the first 2 and last 2 characters.
s = "Traversal"
print(s[2:-2])

# Given s = "banana", print the second and second-last characters.

s = "banana"
print(s[1])
print(s[-2])

# Given s = "rainbow", print the first four characters backward.

s = "rainbow"
print(s[-4::-1])

# Given s = "abcdef", print the string without the middle two characters.
s = "abcdef"
print(s[:2]+s[-2:])
# Given s = "pythonrocks", print the last five characters in reverse.

s = "pythonrocks"
print(s[-1:-6:-1])

# Given s = "pineapple", print "applepine" using slicing only.

s = "pineapple"
print(s[-5:]+s[:4])

# Given s = "datastructure", print every second character in reverse order
s = "datastructure"
print(s[::-2])

# methods of the string
# 2.upper()/lower() ->it convert name string into u/l 
# s="VediKA"
# print(s.upper())
# print(s)
# print(s.lower())
# 3.rstrip()->only remove tralling " ";
name="!!!ANkita !! SHaliiY !!!!!!!"
# print(name.rstrip("!"))
# print(name.lstrip("!"))
# print(name.strip("!"))
# 4.replace()
# name="ankita vedika ankita"
# print(name)
# print(name.replace("vedika","alex"))
# # 6.capitalize()->convert the first letter into capital n rest to 
# small letters
string="hey this is ANKITA and i'm DOING bca kindA worry about Future"
# print(string.capitalize())"""

"""name = "!!!Hello World!!!"
# Expected Output: Hello World
print(name.strip('!'))"""

# Write a program that replaces all occurrences of "Python" with "Java" in a given string.
# python is a snake and python is a language

# x='python is a snake and python is a language'
# print(x.replace('python','java'))
#
# Take a sentence from the user and replace all occurrences of "bad" with "***"
# line=input('enter a sentence using the word bad: ').lower()
# print(line.replace('bad','***'))
#
# Take a sentence from the user AND convert all of WORD to uppercase and replace "John" with "Johnny"
"""line=input('enter a sentence using the word john: ').lower()
print(line.replace('john','johnny').upper())"""

"""
HOMEWORK 
1.Ask the user to enter a paragraph.
Count the number of times "the" appears.
Replace all "the" with "THE".
Print the updated paragraph.
2. Given a messy string like "!!!@@@HELLO python!!!@@@", remove all ! and @ symbols from both 
ends and convert the cleaned string to upper case.
3.Create a string variable containing "python is FUN!!!". Remove the trailing exclamation marks,
 convert it to lowercase, and then replace "fun" with "awesome"
4. Take a string input from the user and replace all spaces  with underscores "_"."""

# para=input('write a short paragraph based on something you want to share using the word "the": ').lower()
# print(para.replace('the','THE'))
#
# mess="!!!@@@HELLO python!!!@@@"
# print(mess.strip('!@').upper())

# var="python is FUN!!!"
# print(var.rstrip('!').lower().replace('fun','awesome'))

# space=input('enter a sentence: ')
# print(space.replace(' ','_'))

# 5.split()-> there should be space in the string and it makes the list of it
string="hey this is ankita"
# print(string,len(string),type(string))
# l=string.split(" ") # converts the str to list
# print(l,len(l),type(l))
# s= " ".join(l) # converts the list to str
# print(s,len(s),type(s))
# 8.count()
string="hey this is ANKITA and i'm DOING bca kindA worry about Future"
# print(string.count("A"))
# 9.endswith()/startswith()-> gives true or false
string="hey this is ANKITA and i'm DOING bca kindA worry about Future"
# print(string.endswith("Ture"))
# print(string.startswith("hey "))
# 10.find()->return the index,if the value is not present
# then return -1
string="hey this is ANKITA and i'm DOING bca kindA worry about Future"
# print(string.find("is"))
# print(string.find("ho"))
# 10.index()->same as find(),but if value is not present then
# raise error(substring not found)
string="hey this is ANKITA and i'm DOING bca kindA worry about Future"
# print(string.index("is"))
# print(string.index("ho"))
# 11.isalnum()->return T is the string is 0-9,a-z,A-Z,but if ($#@!) 
# then return F
a="598asad7"
b="aN3#*"
# print(a.isalnum())
# print(b.isalnum())
# n= "12444s"
# print(n.isdigit())
a="ankita2"
# print(a.isalpha())
# # 12.islower()
a="anjmfh"
# print(a.islower())
a="GJHKJLKb"
# print(a.isupper())
# 14.isspace()
a="      "
# print(a.isspace())
# 15.swapcase()->covert lowercase to uppercase vice versa
a="aNKITA"
# print(a.swapcase())
# 16.title()->first letter of the each word is converted into capital letter
string="hey this is ANKITA and i'm DOING bca kindA worry about Future"
# print(string.title())


# Take a sentence as input and replace a word of the user's choice with another word.
"""sentence=input('enter a sentence: ')
j=input('enter a word from your previous sentence: ')
m=input('enter the word that is to be replaced: ')
print(sentence.replace(j,m))"""

# Take a sentence from the user and count the number of spaces in it.
"""x=input('enter a sentence: ')
print(x.count(' '))"""

# Take a email from the user and check the email ends with .com
"""d=input('enter you email id: ')
print(d.endswith('.com'))
"""


# Convert "hELLo worLD" → proper title case.
# Swap the case of every character in a string.
# Check if a string contains only spaces.

"""s='hELLo worLD'
print(s.title())
d=input('enter a sentence: ')
print(d.swapcase())
d='  '
print(d.isspace())"""

# Find the first position of "the" in a sentence.
"""d=input('enter a sentence: ')
print(d.find('the'))"""

# HOMEWORK
#
# 1 write a program to reverse the string
# 2 Reverse Words in a Sentence: Given a sentence, reverse the order of the words.
#      Input: "Hello world Python vedika"
#      Output: " vedika Python world Hello"


"""v='vedika'
print(v[::-1])
d='hello world python vedika'
l=d.split(' ')
k=(l[::-1])
h=' '.join(l)
print(h)"""

# n= "12444s"
# print(n.isdigit())
# print(n.isalnum())


