#function with return statement
#return statement exits the function
def fn(fname,lname):
    return fname,lname
clientname=fn('jerry','lawler')
print(clientname)

def add(n1,n2):
    return n1+n2
    print('this line will not be executed')
     
result=add(1,10)
print(result)

if result>10:
    print('result is greater than 10')
else:
    print('result is less than or equal to 10')

#writing return statement conditionnally
 if result<0:
    print('result must be greater than 0')
else:
    print(result**2)

#functions with default arguement
def add(n1,n2,n3=0)
   return n1+n2+n3
print(add(1,2))
def about(name, age, city):
  print(f"Hi, My name is {name}. I am {age} years old. I live in {city}.")

about("Vedika", 15, "Gurugram")


# functions with keyword arguments
about(age=15, city="Noida", name="Rohit")

# defining functions with positional arguments with tuples
def fruits(fruit1, fruit2, *fruits):
  print(fruit1)
  print(fruit2)

  print(fruits) # tuple

  # iterating over the fruits tuple
  for x in fruits:
    print(x)

fruits("Apple", "Orange")
fruits("Apple", "Orange", "Banana", "Grapes")
fruits("Apple", "Orange", "Banana", "Grapes", "watermelon", "kiwi")