# Check if a string starts with a capital letter
"""string=input('enter a word: ')
if string[0].isupper():
    print('true')
else:
    print('false')"""

# Take a number as input and check:
#
# If divisible by 3 → Print 'Fizz'
# If divisible by 5 → Print "Buzz"
# If divisible by both 3 and 5 → Print "FizzBuzz"
# Otherwise, print the number itself
"""number=int(input('enter a number: '))
if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number%5==0:
        print('Buzz')
elif number%3==0:
    print('Fizz')
else:
    print(number)"""

"""1 Take an integer input:
If it's even and divisible by 4, print "Even and Divisible by 4".
If it's even but not divisible by 4, print "Even but not Divisible by 4".
If it's odd, print "Odd"."""
# integer=int(input('enter a number: '))
# if integer%2==0 and integer%4==0:
#     print('even and divisible by 4')
# elif integer%2==0 and integer%4!=0:
#     print('even but not divisible by 4')
# else:
#     print('odd'.capitalize())


"""2. Login System
Create a program that checks a user's login attempt:
take password and username input from the user:
The correct username is "admin" and the password is "pass123".
If both are correct, print "Login successful".
If only the username is correct, print "Wrong password".
If only the password is correct, print "Wrong username".
If both are wrong, print "Invalid credentials"."""
# username=input('enter your username: ')
# password=input('enter your password: ')
# if username=='admin' and password=='pass123':
#     print('login successful')
# if password=='pass123' and username!='admin':
#     print('wrong username')
# if username=='admin' and password!='pass123':
#     print('wrong password')
# else:
#     print('invalid credentials')
#
# """3 Input time in 24-hour format and print:
# Morning (5–11)
# Afternoon (12–16)
# Evening (17–20)
# Night (21–4)"""
"""time=int(input('enter the time in 24 hour format: '))
if time in range(5,12):
    print('morning')
elif time in range(12,17):
    print('afternoon')
elif time in range(17,21):
    print('evening')
elif time in range(21,25) or time in range(1,5):
    print('night')
else:
    print('invalid time')"""
# """4 Take age as input and classify:

"""0-12 → Child
13-19 → Teenager
20-59 → Adult
60+ → Senior Citizen"""

"""age=int(input('enter your age: '))
if age <13 and age>0:
    print('you are a child')
elif age<20 and age>12:
    print('you are a teenager')
elif age>19 and age<60:
    print('you are an adult')
elif age>59 and age<121:
    print('you are a senior citizen')
else:
    print('incorrect age')""""""

# 1 Simple calculator:
# Take two numbers and operator (+, -, *, /).
# Perform operation using if-elif.

print('calculator')
one=int(input('enter the first operand: '))
two=int(input('enter the second operand: '))
operation=(input('enter the operation to be performed: '))
if operation=='+':
    print(one+two)
elif operation=='x':
    print(one*two)
elif operation=='/':
    print(one/two)
elif operation=='-':
    print(one-two)
else:
    print('incorrect operator')

# 2 Input a character.
# Check if it is vowel, consonant, or not a letter.
character=input('enter a character: ').lower()
# if character=='a' or character=='e' or character=='i' or character=='u' or character=='o':
if character in 'aeiou':
    print('its a vowel')
elif character.isalpha():
    print("it's a consonant")
elif character.isdigit():
    print('it is a number')
elif character.isalnum():
    print('it is a mix of digit and a letter')
else:
    print('your input is a special character')"""

# Write a program that asks the user for a password. If it matches "admin123", print "Access Granted", otherwise print "Access Denied".
"""password=input('enter your password: ')
if password=='admin123':
    print('access granted')
else:
    print('access denied')"""

