"""list"""
l= []
# print(l,type(l))
l= [1,2,3,4,"vedika"]
# print(l,type(l))
names=["Aditya", "Joshi", "Mohit", "Rohit"]
# print(names[0 : ])
# # print(names[4])
# print(names[3])

"""nested list / list of list"""
data=[1, 2, 3, [4, 5, 6, [7, 8, [9]]], 10]
# print(len(data))
# print(data[1])
# print(data[5])
# print(data[3])
# print(data[3][3])
# print(data[3][3][2])
# print(data[3][3][2][0])
# print(data[4])

"""list constructor  => list()"""
num=[1,2,3,4]
# print(type(num))
mylist=list('BCA4')
# print(mylist)
num=list({1:'one',2:'two','vedika':3}) # dictionary { key : value,}
print(num)
num=list((40, 50, 60))
# print(num)
num=list({400, 500, 600}) # set {}
# print(num)


# for loop in a list
# s="hello"
# for i in s: #  a
#     print(i) #

"""for loop in a list"""
l = ["hello", 1, 2.34, True]
# for i in l:#
#     print(i,type(i))

"""list of list for loop"""
l1 = [1, 2.8, [10, 20, [100.200]], "done"]
# for i in l1:
#     print(i,type(i))

l = ["hello", 1, 2.34, True]
# for i in range(len(l)):# range(4) 0-3, 0
#     print(i,l[i])# 0, l[0]

#append () {in the last} and insert((at the index positio))
# can be used to update the list
l=["hello",1,2,"bye",4]
# print(l)
# l.append('u')
# l.append(5)
# print(l)
# # # inesrt nai change nahi kiya hello to 1 but add
l=["hello",1,2,"bye",4]
# print(l)
# l.insert(3,"ankita")
# l.insert(-1,"gabby")
# l.append("dani")
# print(l)
l2=[1,2,3]
l3=[4,5,6]
# l2.append(l3)
# print(l2)
# print(len(l2))#
l2=[1,2,3]
# l2.extend(l3)
# print(l2)
# print(len(l2))#
l4=l3+l2
# print(l4)

# HOMEWORK
# Q1. create a list and perform following operation
# 1-insert the elements(a,b,c,d,e) into the list ,
# 2- update the 3rd positon to "f",
# 3- append a new item "z" in the list,
# 4-delete a from the list
# 5-replace e with h

"""l=['a','b','c','d','e']
print(l)
l[3]='f'
print(l)
l.append('z')
print(l)
l.remove('a')
print(l)
l[3]='h'
print(l)"""
#
# Q2. Create two lists: one with 5 fruit names and another with   5 vegetable names.
#         Combine both lists into one.
#         Add Mango and Spinach at the appropriate index.
#         Remove Spinach from the list.
#         Find the index of Carrot in the list.
"""fruit=['banana','apple','watermelon','lychee','pineapple']
veg=['ladyfinger','bottle gourd','broccoli','cauliflower','carrot']
fruit.extend(veg)
print(fruit)
fruit.insert(5,'mango')
print(fruit)
fruit.insert(-1,'spinach')
print(fruit)
fruit.remove('spinach')
print(fruit)
print(fruit.index('carrot'))"""

# Q3. Create a list with numbers from 1 to 10.
#         Reverse the list.
#         Replace the first three numbers with 100, 200, 300.
#        Remove all even numbers from the list.
#         Check if 5 is still in the list.
# number=[1,2,3,4,5,6,7,8,9,10]
# reverse=number[::-1]
# print(reverse)
# # number[0]=100
# # number[1]=200
# # number[2]=300
# number[:3]=100,200,300
# print(number)
# # for i in number:
# #     if i%2==0:
# #         continue
# #     print(i)
# number=[i for i in number if i%2!=0]
# print(number)
#
# # if 5 in number:
# #     print(True)
# print(5 in number)
"""list comprehension"""
"""# new_list = [expression (for item in iterable) if condition]

l= [10,2,30,44,57,0,6,3,100]
print(l)
new_list=[] # [2,0]
for i in l:
    if i >=10:
        continue
    new_list.append(i)
print(new_list)

second_new_list= [i for i in l if i<10] #[2]
print(second_new_list)"""
# create two list of 5 odd no. and 5 even no.
# combine the list , add prime no 157 at the beginning of the combined list, report how may items in the list now
# replace the last 3 no with 1,2,3, del all the no. from the list ,last del the list

# l=[1,3,5,7,9]
# n=[2,4,6,8,10]
# l.extend(n)
# print(l)
# l.insert(0,157)
# print(l)
# print(l[-1:-4])
# print(l[-3:])

# HOMEWORK
# 1 Create a list: [10, 20, 30, 40, 50]
# Insert 25 after 20
# Replace 40 with 45
# Append 60
# Remove 30
# Sort the list in ascending order
"""list=[10, 20, 30, 40, 50]
print(list)
list.insert(2,25)
print(list)
list[4]=45
print(list)
list.append(60)
print(list)
list.remove(30)
print(list)
list.sort()
print(list)"""



# 2 Create a list of 6 numbers
# Remove the first element
# Insert a number at the last position
# Replace the 2nd element
# Count how many elements are greater than 10
# Print the maximum number
"""list=[1,5,70,35,0,10]
print(list)
list.remove(1)
print(list)
list[1]=2
print(list)
list=[i for i in list if i>10]
print(list)
print(max(list))"""


# 3 Create a list: [1, 2, 3, 4, 5, 6]
# Print only the middle 3 elements using slicing
# Replace the first 2 elements with 10, 20
"""# Remove elements from index 2 to 4(doubt)"""
# Add 100, 200 at the end of the listt
# Reverse using slicing
"""list=[1, 2, 3, 4, 5, 6]
print(list[1:4])
list[0]=10
list[1]=20
print(list)
list.extend([100,200])
print(list)
print(list[::-1])"""



# l= [10,2,30,44,57,0,6,3,100]
# newl=[i for i in l if i%2==0]
# print(newl)



"""how to add values in the list"""
"""#append () {in the last} and insert((at the index position)) 
# can be used to update the list
l=["hello",1,2,"bye",4]
# print(l)
# l.append('u')
# l.append(5)
# print(l)
# insert nai change nahi kiya hello to 1 but add
l=["hello",1,2,"bye",4]
# print(l)
# l.insert(3,"ankita")
# l.insert(1,"gabby")
# l.append("dani")
# print(l)# 
l2=[1,2,3]
l3=[4,5,6]
# l2.append(l3)
# print(l2)
# print(len(l2))#
# l2=[1,2,3]
# l2.extend(l3)
# print(l2)
# print(len(l2))#
# l4=l3+l2
# print(l4)"""
"""remove ,pop,del"""
# l=['hello',1,2,'bye', 10,True, 'u']
# print(l)
# l.remove(1)
# l.remove('bye')
# print(l)
# l.pop(1)
# print(l)
# l.pop(4)
# print(l)
# l.clear()
# print(l)
# del l
# print(l)
"""function of the list"""
"""#len(list),max(list),min(list),sum(list),del(list),sorted(list),reversed(list)
l=[1,5,0,7,2,8,4]
print(l)
# l=['abs','acgfhkuj','brs','z',"sam",'ken']
# print("length =",len(l)) # len(l)
# print("max =",max(l))
# print("min =",min(l))
# print(sum(l))
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# l=[1,5,0,7,2,8,4]
# print(l)
# p=l[::-1]
# print("reversed list",p)"""
"""# methods of the list
l=[1, 5, 2,7, 2, 8, 4,7,7,7]
# print(l.index(7))
# print(l.count(7))"""

# find the average of all elements in a list,
"""l=[1,2,3,4,5,6,7,8,9,10]
print(sum(l)/len(l))"""

# Find the largest number in a list
"""l=[10, 5, 22, 3]
print(max(l))"""

# Write a program to count how many positive and negative numbers are in the list.
"""l=[4, -1, 9, -6, 0, 3]
n=0
p=0
for i in l:
    if i<0:
        n=n+1
print(n)
for i in l:
    if i>0:
        p=p+1
print(p)"""

"""l=[4, -1, 9, -6, 0, 3]
n=0
p=0
for i in l:
    if i<0:
        n=n+1
    elif i>0:
        p+=1
print(n,p)
"""

# Find the second largest number in a list
# l=[10, 5, 22, 3,33,53,23,64]
"""n=[]
for i in l:
    if i<(max(l)):
        n.append(i)
print(max(n))"""

"""l.sort()
print(l)
print(l[-2])"""

# 5. Loop through a list of names and skip any name shorter than 5 letters and starting with a .
"""name=['vedika','ayda','aaliyah','arit','veer']
n=[]
for i in name:
    if len(i)<5 and i.startswith('a'):
        continue
    n.append(i)
print(n)
n=[i for i in name if not (len(i)<5 and i.startswith('a'))]
print(n)"""


# From a list of numbers, keep only even numbers and square them
"""nums = [1, 2, 3, 4, 5, 6]
n=[i**2 for i in nums if i%2==0]
print(n)"""

# HOMEWORK
# 1. Remove duplicates without using set
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]
"""number=[1, 2, 2, 3, 4, 4, 5]
empty=[]
for i in number:
    if i not in empty:
        empty.append(i)
print(empty)"""


# 2. Find second largest element
# Input: [10, 20, 4, 45, 99]
# Output: 45
x=[10, 20, 4, 45, 99]
"""x.remove(max(x))
print(max(x))
"""
#OR

"""x.sort()
print(x)
print(x[-2])"""

# 3. Rotate list to the right by k steps
# Input: [1,2,3,4,5], k=2
# Output: [4,5,1,2,3]
"""x=[1,2,3,4,5] #[5,1,2,3,4]
k=2
for i in range(k): #0-1, 0, 
    last=x.pop() # last=5
    x.insert(0,last) #(0,5)
print(x)"""

# Wap that removes all strings from a mixed list.
# Example: [1,"a",2,"b"] → [1,2]
"""lis=[1,"a",2,"b"]
empt=[]
for i in lis:
    if isinstance(i,int):
        empt.append(i)
print(empt)"""

# Write a function that flattens a nested list.
# Example: [[1,2],[3,4]] → [1,2,3,4]
"""nested=[[1,2],[3,4]]
s=[]
for i in nested:
    s.extend(i)
print(s)"""

# Write a program  that checks whether an element exists in a list.
"""y=int(input('enter a number to check if it is in the list or not: ')) #2
x=[1,2,3,4,5]
print(y in x)"""

# HOMEWORK
# Write a program that merges two lists into one.
"""list1=[1,5,'hi',76]
list2=[2,20,8,'yo']
list1.extend(list2)
print(list1)"""
# Write a program that returns a new list containing only odd numbers.
"""x=[1,2,3,4,5,6]
y=[]
for i in x:
    if i%2!=0:
        y.append(i)
print(y)"""
# Write a program that converts all strings in a list to uppercase.
"""s=['namaste','bonjour','hello','sayonara']
u=[]
for i in s:
    t=i.upper()
    u.append(t)
print(u)"""
# Write a program that multiplies every element in a list by 2.
"""x=[1,2,3,4,5]
for i in x:
    print(i*2)"""
# Write a program that returns the longest string in a list.***************************
"""s=['namaste','bonjour','hello','sayonara']
long=s[0]
for i in s:
    if len(i)>len(long):
        long=i
print(long)"""


