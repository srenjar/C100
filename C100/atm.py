class Atm :
    def __init__ (self,cardno,pin):
        self.cardno = cardno
        self.pin = pin
        
    def check_balance (self):
        print('ur balance amount is 50000')
    
    def withdrawal (self,amount):
        new_amount = 50000 - amount
        print('U have withdrawn amount '+ str(amount) + '. Ur remaining balance is ' + str (new_amount))
    

def main ():
    card_no = input('Enter your card no : ')
    pin_no = input( 'Enter your pin no : ')

    new_user = Atm(card_no,pin_no)
    print('Choose ur activity')
    print('1. Balance enquiry 2. Withrawal')

    activity = int(input('Enter the activity no : '))

    if(activity == 1):
        new_user.check_balance()
    elif ( activity == 2):
        amount = int(input('Enter the amount'))
        new_user.withdrawal(amount)
    else :
        print('Enter a valid no')

main()