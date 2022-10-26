import SendersNumberValidification,Ownership
def sendMoneyFunction():
    senderPhoneNumber = SendersNumberValidification.SenderNumberValidation()
    senderAmount = int(input('Enter the amount being sent: '))
    accountMoney = Ownership.accountbalance() # This is initialised the amount of money in the account of this user
    userPin = Ownership.userpin() # This is initialised the pin of this user
    if senderAmount < accountMoney:
        userPinVerified = int(input('Enter your pin: '))
        
        # User Pin verification
        if userPinVerified == userPin and len(str(userPinVerified)) == 5:
            
            charge = round(0.0005 * senderAmount)
            
            balance = accountMoney - (senderAmount + charge)
            
            print(f"You have sent {senderAmount:,} to {senderPhoneNumber} at a charge of {charge:,} Your balance is {balance:,}")

        else:
            attempts = 1
            print('Incorrect pin. Try again')
            while attempts > 0:
                userPinVerified = int(input('Enter your pin: '))
                if userPinVerified == userPin:
                    charge = 0.5 * senderAmount
            
                    balance = accountMoney - (senderAmount + charge)
            
                    print(f"You have sent {senderAmount:,} to {senderPhoneNumber} at a charge of {charge:,} Your balance is {balance:,}")
                elif attempts == 0:
                    print('Invalid Pin!!')
                else:
                    continue
    else:
        print('Insufficient Funds')           