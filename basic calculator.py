print("Basic Calculator")
print("      ")

print("Select the option to perform")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
print("5. Modulus")
print("6. Clear")
print("7. Exit")

in1= int(input('enter the number- '))
in2=int(input('enter the number- '))
choice=int(input('enter your choice- '))

if choice==1:
    result=in1+in2
    print('the result is: ', result)

elif choice==2:
    result=in1-in2
    print('the result is: ', result)

elif choice==3:
    result=in1/in2
    print('the result is: ', result)

elif choice==4:
    result=in1*in2
    print('the result is: ', result)

elif choice==5:
    result=in1%in2
    print('the result is: ', result)

elif choice==6:
    result=0
    print(result)

elif choice==7:
    print("thanks for using")
