"""tuple ()"""
# t = ()
# print(t,type(t))
t = 1,2,3
# print(t,type(t))
t = (1,)
# print(t,type(t))
names = ('Aditya', 'Neha', 'Shree', 'GEU')
# print(names[2:3])
names = ('Aditya', 'Neha', 'Shree', 'GEU')
# print(names)
# print(names)
# w,x,y,z=names #unpacking tuples*********************************
# print(w,z,y,x)
names = ('Aditya', 'Neha', 'Shree', 'GEU')
# del names
# print(names)
# names.clear
""" tuple() constructor"""
tpl = tuple('Hello') #
# print(tpl)
tpl = tuple([1,2,3,4,5]) #
# print(tpl)
tpl = tuple({1,2,3,4,5}) #
# print(tpl)
tpl = tuple({1:"One",2:"Two"}) #
# print(tpl)

# basic function
# t = (1, 5, 2, 9,2,3, 45,7)
# print(len(t))      #
# print(max(t))      #
# print(min(t))      #
# print(sum(t))      #
# print(sorted(t))   #

# tuples operation
# t=(1,11,7,34,30)
# t2=(1,2,3)
# t3=t2+t #concatination
# print(t3)
# t.append(t2)
# print(t)
# print(t2*4) # repetition
# print(7 in t) # membership
# t = (10, 20, 30, 40)
# print(t[1:-2])  #
# for i in t2: # itration
#     print(i)

# methods
# t=(1,11,7,34,30,7,7,7)
# print(t.index(7) )  #
# print(t.count(7))   #

#wap to join 2 tuples if the initial element of both the tuple is same otherwise print the tuple as it is
"""x=(4,5,'hello','hmm')
y=(9,6,'hi')
if x[0]==y[0]:
    print(x+y)
else:
    print(x,y)"""

#given a following t=(f,a,b,b,y) write a py program to carry out following operation
#1- add an ? at the end of tupple
# 2-  find out the occurance of "b" in the tuple (using count())
# 3-check weather "a "exist in the tuple
# 4-del char f and y from the t

"""t=('f','a','b','b','y')
t2='?',
t3=(t+t2)
print(t3)
print(t3.count('b'))
print('a' in t3)
t4=list(t3)
t4.remove('f')
t4.remove('y')
t4=tuple(t4)
print(t4)"""


"""t = (2, 5, 8, 3, 9, 5, 7, 5, 1)
# Perform the following operations:
#
#     Add 12 at the end of the tuple.
t2=12,
t3=(t+t2)
print(t3)
t2=t+(12,)
print(t2)
#
#     Find the index of the first occurrence of 5.
print(t2.index(5))
#
#     Count how many times 5 appears in the tuple.
print(t2.count(5))
#     Reverse the elements of the tuple.
print(t2[::-1])
#     Slice the tuple to get only even numbers.
t4=[]
for i in t2:
    if i%2==0:
        t4.append(i)
t4=tuple(t4)
print(t4)
#     Remove the first occurrence of 5 from the tuple.
t2=list(t2)
t2.remove(5)
t2=tuple(t2)
print(t2)
#     Check if 3 exists in the tuple.
print(3 in t2)
#     Sort the tuple in ascending order.
print(sorted(t2))
#     Find the maximum and minimum element in the tuple.
print(max(t2))
print(min(t2))
# Multiply each element by 2 and create a new tuple with the results.
y=[]
for i in t2:
    # z=i*2
    y.append(i*2)
y=tuple(y)
print(y)"""

t = ('x', 'p', 'z', 'x', 'y', 'z', 'a', 'p')
# Perform the following operations in sequence:
#     Add the element 'q' at the beginning of the tuple.
# t=list(t)
# t.insert(0,'q')
# t=tuple(t)
# print(t)
# #     Find the number of times 'z' appears in the tuple.
# print(t.count('z'))
# #     Check if 'y' exists in the tuple.
# print('y' in t)
#     Convert the tuple into a list and remove the first occurrence of 'p'.
'''t=list(t)
t.remove('p')
t=tuple(t)
print(t)'''
#     Replace the element 'x' with 'w' wherever it appears.
'''t=list(t)
for i in range(len(t)):
    if t[i]=='x':
        t[i]='w'
print(t)'''
#     Convert the list back to a tuple.
# t=tuple(t)
# print(t)
#     Sort the tuple in descending order.

#     Slice the tuple to get the first 5 elements.
# print(t[0:5])
# #     Count the total number of elements in the modified tuple.
# print(len(t))
# #     Display the final state of the tuple.
# print(t)
