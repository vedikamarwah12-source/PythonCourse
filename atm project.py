balance=10000
print('ATM\nSYSTEM')
for i in range(1,4,1):
    opt=(input('do you want to continue or not?\nyes or no?: ')).lower()
    if opt!='yes':
        print('thanks for using atm')
        break
    print('1.check balance\n2.deposit money\n3.withdraw money\n4.exit')
    choice=int(input('enter a choice number for proceeding further: '))
    if choice==1:
        print('current balance is',balance)
    elif choice==2:
        amount=int(input('enter the amount to be deposited to your account: '))
        if amount>0:
            balance=balance+amount
            print('you have successfully deposited',amount,'to your prior balance')
        else:
            print('invalid amount error incurred')
    elif choice==3:
        amount=int(input('enter the amount to be taken out of your account: '))
        if amount>0:
            balance=balance-amount
            print('you have successfully withdrawn',amount,'from your account')
        elif amount>balance:
            print('insufficient balance')
        else:
            print('invalid amount error incurred')
    elif choice==4:
        print('thanks for using atm')
        break
    else:
        print('invalid choice,please enter choice 1 to 4')
print('atm session ended')