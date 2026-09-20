#wap to print full name 
'''def fn(fname,lname):
    print(f'{fname} {lname}')

print(fn('vedika','marwah'))'''

#doc string
"""def movie(name):
    '''this function prints the name of the movie'''
    return name
print(movie('obsession'))
print(movie.__doc__)"""

#doc string for preserving the structure of the code

"""def poem(name):
    '''twinkle twinkle
    little star
    how i wonder
    what you are'''
    return name
print(poem('star'))
print(poem.__doc__)"""

#recursion
'''def prt(n):
    print(n)
    print(prt(n))#infinite loop
print(prt('amy'))'''

#factorial
#factorial of 5=5*4*3*2*1=120
#factorial of 0 is 1
'''def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))'''