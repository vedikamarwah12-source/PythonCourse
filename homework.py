def gc():
    print('welcome to art supplies store')
    print('get all your art supplies at one place')
print(gc())

price=float(input('enter the price of the item: '))
number=int(input('enter the number of items: '))

def calculate(price,number):
    total=price*number
    return total

print(calculate(price,number))

paid=float(input('enter the amount paid: '))
def change(paid,total):
    change=paid-total
    return change

def thank():
    if price>1000:
        print('thank you for shopping with us')
    else:
        print('thank you for shopping with us, please visit again')

print('reciept: ')
print(f'items: {number}')
print(f'total: {calculate(price, number)}')
print(f'amount paid: {paid}')
print(f'change: {change(paid,total)}')
thank()