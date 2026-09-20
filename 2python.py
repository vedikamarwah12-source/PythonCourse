'''print('STUDENT GRADING SYSTEM')
a=float(input('enter science marks here: '))
b=float(input('enter math marks here: '))
c=float(input('enter english marks here: '))
d=float(input('enter social science marks here: '))
obtained=a+b+c+d
total_marks=320
per=obtained/total_marks*100
if per<90:
    print('A GRADE STUDENT KEEP IT UP!')
elif per<70:
    print('GOOD JOB WORK HARDER!')
elif per<30:
    print('YOU NEED TO WORK HARDER')
else:
    print('FAIL!')

x=(input('enter a letter here: '))
if x=='a' or x=='i' or x=='e' or x=='u' or x=='o':
    print('your letter is a vowel')
else:
    print('your letter is a consonent')

letter=input('enter a letter here: ')
if letter.islower():
    print('the letter is small')
else:
    print("the letter is capital")

sym=input('enter any number, letter or character here: ')
if sym.isnumeric():
    print('your input is a number')
elif sym.isalpha():
    print('your input is an alphabet')
else:
    print("your input is a character")'''

