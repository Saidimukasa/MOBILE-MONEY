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
                
                    print(f"You have sent {withdrawAmount:,} at a charge of {charge:,} Your balance is {balance:,}")
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
                    
                            print(f"You have accepted withdraw of {withdrawAmount:,} at a charge of {charge:,} Your balance is {balance:,}")
                        elif attempts == 0:
                            print('Invalid Pin!!')
                        else:
                            continue
        else:
            print('Insufficient Funds')