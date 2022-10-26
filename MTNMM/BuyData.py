import Ownership
def buyDataFunction():
    print('Welcome to MTN Data Bundles')
    print("Daily Bundle \n weekly Bundle \n Monthly Bundle")
    dataBundle = input("Enter the data bundle you want to buy: ")
    if dataBundle == 'Daily Bundle':
        print("Daily Bundle")
        print("1. 100MB for 1000 UGX")
        print("2. 200MB for 2000 UGX")
        print("3. 500MB for 3000 UGX")
        print("4. 1GB for 5000 UGX")
        choice = int(input("Enter the data bundle you want to buy: "))
        if choice == 1:
            payingOption = input("Do you want to pay with MTN Mobile Money or MTN Airtime? (1. MTN Mobile Money, 2. MTN Airtime): ")
            if payingOption == '1':
                balance = Ownership.accountbalance() - 1000
                print(f"You have successfully bought 100MB for 1000 UGX balance is {balance:,}")
            elif payingOption == '2':
                print("You donot have enough airtime")
            else:
                print("Invalid Option")
                buyDataFunction()
        elif choice == 2:
            payingOption = input("Do you want to pay with MTN Mobile Money or MTN Airtime? (1. MTN Mobile Money, 2. MTN Airtime): ")
            if payingOption == '1':
                balance = Ownership.accountbalance() - 2000
                print(f"You have successfully bought 200MB for 1000 UGX balance is {balance:,}")
            elif payingOption == '2':
                print("You donot have enough airtime")
            else:
                print("Invalid Option")
                buyDataFunction()
        elif choice == 3:
            payingOption = input("Do you want to pay with MTN Mobile Money or MTN Airtime? (1. MTN Mobile Money, 2. MTN Airtime): ")
            if payingOption == '1':
                balance = Ownership.accountbalance() - 3000
                print(f"You have successfully bought 500MB for 3000 UGX balance is {balance:,}")
            elif payingOption == '2':
                print("You donot have enough airtime")
            else:
                print("Invalid Option")
                buyDataFunction()
            
        elif choice == 4:
            payingOption = input("Do you want to pay with MTN Mobile Money or MTN Airtime? (1. MTN Mobile Money, 2. MTN Airtime): ")
            if payingOption == '1':
                balance = Ownership.accountbalance() - 5000
                print(f"You have successfully bought 1GB for 5000 UGX balance is {balance:,}")
            elif payingOption == '2':
                print("You donot have enough airtime")
            else:
                print("Invalid Option")
                buyDataFunction()
        else:
            print("Invalid Option")
            buyDataFunction()
    elif dataBundle == 'Weekly Bundle':
        print("Weekly Bundle")
        print("1. 500MB for 5000 UGX")
        print("2. 1GB for 7500 UGX")
        print("3. 2GB for 10000 UGX")
        print("4. 5GB for 15000 UGX")
        choice = int(input("Enter the data bundle you want to buy: "))
        if choice == 1:
            payingOption = input("Do you want to pay with MTN Mobile Money or MTN Airtime? (1. MTN Mobile Money, 2. MTN Airtime): ")
            if payingOption == '1':
                balance = Ownership.accountbalance() - 5000
                print(f"You have successfully bought 500MB for 5000 UGX balance is {balance:,}")
            elif payingOption == '2':
                print("You donot have enough airtime")
            else:
                print("Invalid Option")
                buyDataFunction()
        elif choice == 2:
            payingOption = input("Do you want to pay with MTN Mobile Money or MTN Airtime? (1. MTN Mobile Money, 2. MTN Airtime): ")
            if payingOption == '2':
                balance = Ownership.accountbalance() - 7500
                print(f"You have successfully bought 1GB for 7500 UGX balance is {balance:,}")
            elif payingOption == '2':
                print("You donot have enough airtime")
            else:
                print("Invalid Option")
                buyDataFunction()
        elif choice == 3:
            payingOption = input("Do you want to pay with MTN Mobile Money or MTN Airtime? (1. MTN Mobile Money, 2. MTN Airtime): ")
            if payingOption == '1':
                balance = Ownership.accountbalance() - 10000
                print(f"You have successfully bought 2GB for 10000 UGX balance is {balance:,}")
            elif payingOption == '2':
                print("You donot have enough airtime")
            else:
                print("Invalid Option")
                buyDataFunction()
        elif choice == 4:
            payingOption = input("Do you want to pay with MTN Mobile Money or MTN Airtime? (1. MTN Mobile Money, 2. MTN Airtime): ")
            if payingOption == '1':
                balance = Ownership.accountbalance() - 15000
                print(f"You have successfully bought 100MB for 15000 UGX balance is {balance:,}")
            elif payingOption == '2':
                print("You donot have enough airtime")
            else:
                print("Invalid Option")
                buyDataFunction()
        else:
            print("Invalid Option")
            buyDataFunction()
    elif dataBundle == 'Monthly Bundle':
        print("Monthly Bundle")
        print("1. 10GB for 25000 UGX")
        print("2. 20MB for 30000 UGX")
        print("3. 50MB for 45000 UGX")
        print("4. 100GB for 70000 UGX")
        choice = int(input("Enter the data bundle you want to buy: "))
        if choice == 1:
            payingOption = input("Do you want to pay with MTN Mobile Money or MTN Airtime? (1. MTN Mobile Money, 2. MTN Airtime): ")
            if payingOption == '1':
                balance = Ownership.accountbalance() - 25000
                print(f"You have successfully bought 10GB for 25000 UGX balance is {balance:,}")
            elif payingOption == '2':
                print("You donot have enough airtime")
            else:
                print("Invalid Option")
                buyDataFunction()
        elif choice == 2:
            payingOption = input("Do you want to pay with MTN Mobile Money or MTN Airtime? (1. MTN Mobile Money, 2. MTN Airtime): ")
            if payingOption == '1':
                balance = Ownership.accountbalance() - 30000
                print(f"You have successfully bought 20Gb for 30000 UGX balance is {balance:,}")
            elif payingOption == '2':
                print("You donot have enough airtime")
            else:
                print("Invalid Option")
                buyDataFunction()

        elif choice == 3:
            prpayingOption = input("Do you want to pay with MTN Mobile Money or MTN Airtime? (1. MTN Mobile Money, 2. MTN Airtime): ")
            if payingOption == '1':
                balance = Ownership.accountbalance() - 45000
                print(f"You have successfully bought 50GB for 1000 UGX balance is {balance:,}")
            elif payingOption == '2':
                print("You donot have enough airtime")
            else:
                print("Invalid Option")
                buyDataFunction()
        elif choice == 4:
            payingOption = input("Do you want to pay with MTN Mobile Money or MTN Airtime? (1. MTN Mobile Money, 2. MTN Airtime): ")
            if payingOption == '1':
                balance = Ownership.accountbalance() - 70000
                print(f"You have successfully bought 100GB for 70000 UGX balance is {balance:,}")
            elif payingOption == '2':
                print("You donot have enough airtime")
            else:
                print("Invalid Option")
                buyDataFunction()
            print("Invalid Option")
            buyDataFunction()
    else:
        print("Invalid Option")
        buyDataFunction()
   