# Triangle Type
# Take 3 sides of a triangle and check:
# If all sides are equal → Equilateral
# If any two sides are equal → Isosceles
# If all sides are different → Scalene
# If sum of any 2 sides ≤ third side → Not a Triangle
"""side1=int(input('enter the first side of the triangle: '))
side2=int(input('enter the second side of the triangle: '))
side3=int(input('enter the third side of the triangle: '))"""
# if side1==side2==side3:
#     print('it is a equilateral triangle')
# elif side1 == side2 != side3:
#     print('it is an isosceles triangle')
#     if side1 + side2 >= side3:
#         print('not a triangle')
#     elif side1 + side3 >= side2:
#         print('not a triangle')
#     elif side3 + side2 >= side1:
#         print('not a triangle')
# elif side1==side3!=side2:
#     print('it is an isosceles triangle')
# elif side3==side2!=side1:
#     print('it is an isosceles triangle')
# elif side1!=side2!=side3:
#     print('scalene triangle')
# else:
#     print('invalid input')
"""if side1 + side2 <= side3 or side1 + side3 <= side2 or side3 + side2 <= side1:
    print('not a triangle')
else:
    if side1==side2==side3:
       print('it is an equilateral triangle')
    elif side1==side2 or side2==side3 or side3==side1:
        print('isosceles triangle')
    else:
        print('scalene triangle')"""

# Take an integer input and check:
# If the number is positive
# If even → print "Positive Even"
# Else → print "Positive Odd"
# Else if negative
# If even → print "Negative Even"
# Else → print "Negative Odd"
# Else → print "Zero"
"""integer=int(input('enter a number: '))
if integer>0:
    if integer%2==0:
        print('positive even')
    else:
        print('negative even')
elif integer<0:
    if integer%2==0:
        print('positive odd')
    else:
        print('negative odd')
else:
    print('0')"""


