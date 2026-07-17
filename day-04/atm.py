#simple atm program where it will ask to enter your pin before doing withdrawl



def atm():
    pin =9369
    amount=50000
    pinx = int(input(" enter you pin to access = "))
    if pinx==pin:
        
        winamount = int(input(" enter the amount you want to withdrawl from atm "))
        if winamount<=0:
            print("please enter amount more then 0")
        elif winamount<=amount:
            print("Transaction Successful")
            amount=amount-winamount
            print(amount)
        else:
            print("Insufficient Balance")
    else:
        print("Wrong pin")
atm()