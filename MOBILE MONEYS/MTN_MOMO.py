# Prompting User to input their Phone Number
UserPhoneNumber =int(input("Enter your Phone Number (078- or 077- or 074-): "))

# FUNCTIONS
# Function for sending money
def sendMoneyFunction():
    senderPhoneNumber = int(input('Enter Sender\'s phone number: '))
    
    accountMoney = 10000000
    userPin = 25252
    
    if len(str(senderPhoneNumber)) == 9:
        senderAmount = int(input('Enter the amount being sent: '))
        
        if senderAmount < accountMoney:
            userPinVerified = int(input('Enter your pin: '))
            
            # User Pin verification
            if userPinVerified == userPin and len(str(userPinVerified)) == 5:
                
                charge = round(0.0005 * senderAmount)
                
                balance = accountMoney - (senderAmount + charge)
                
                print('You have sent '+ str(senderAmount) + ' to '+ str(senderPhoneNumber) + ' at a charge of '+str(charge)+'. Your balance is '+str(balance)+'.')
            else:
                attempts = 1
                print('Incorrect pin. Try again')
                userPinVerified = int(input('Enter your pin: '))

                while attempts > 0:
                    print('You have '+str(attempts)+' left')
                    attempts+=-1
                    userPinVerified = int(input('Enter your pin: '))
                    if userPinVerified == userPin:
                        charge = 0.5 * senderAmount
                
                        balance = accountMoney - (senderAmount + charge)
                
                        print('You have sent '+ str(senderAmount) + ' to '+ str(senderPhoneNumber) + ' at a charge of '+str(charge)+'. Your balance is '+str(balance)+'.')
                    elif attempts == 0:
                        print('Invalid Pin!!')
                    else:
                        continue
        else:
            print('Insufficient Funds')           
    else:
        print('Invalid Phone Number!!')

# Function for Withdrawing money
def withdrawMoneyFunction():
    
    accountMoney = 10000000
    userPin = 25252
    
    withdrawAmount = int(input('Enter the amount you want to withdraw: '))
    
    if withdrawAmount < accountMoney:
            userPinVerified = int(input('Enter your pin: '))
            
            # User Pin verification
            if userPinVerified == userPin and len(str(userPinVerified)) == 5:
                
                charge = round(0.0003 * withdrawAmount)
                
                balance = accountMoney - (withdrawAmount + charge)
                
                print('You have withdrawn '+ str(withdrawAmount) +' at a charge of '+str(charge)+'. Your balance is '+str(balance)+'.')
            else:
                attempts = 1
                print('Incorrect pin. Try again')
                userPinVerified = int(input('Enter your pin: '))

                while attempts > 0:
                    print('You have '+str(attempts)+' left')
                    attempts+=-1
                    userPinVerified = int(input('Enter your pin: '))
                    if userPinVerified == userPin and len(str(userPinVerified)) == 5:
                        charge = round(0.0003 * withdrawAmount)
                
                        balance = accountMoney - (withdrawAmount + charge)
                
                        print('You have withdrawn '+ str(withdrawAmount) + ' at a charge of '+str(charge)+'. Your balance is '+str(balance)+'.')
                    elif attempts == 0:
                        print('Invalid Pin!!')
                    else:
                        continue
    else:
        print('Insufficient Funds')   

# Checking if the Phone Number is correct
# 1. if it is a real phone number
def realPhoneNumber():
    if(len(str(UserPhoneNumber)) == 9 ):
        
        print('MTN Options\n')
        Options = ['1. Send Money', '2. Withdraw Money']
        
        for option in Options:
            print(option)
        
        userPrompt = int(input('Enter an option (1 or 2): '))
        
        # SENDING MONEY OPTION
        if userPrompt == 1:
            sendMoneyFunction()
        elif userPrompt == 2:
            withdrawMoneyFunction()
        else:
            print('Invalid Option!!')
    else:
        print('Invalid PhoneNumber!!')

realPhoneNumber()