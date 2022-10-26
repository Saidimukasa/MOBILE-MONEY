def SenderNumberValidation():
    networkCodes = {1: {'name':'MTN','code': 77, 'digits': 2}, 2: {'name':'Airtel','code': 75, 'digits': 2}, 3: {'name':'Uganda Telecom','code': 71, 'digits': 2}, 4: {'name':'Africell','code': 78, 'digits': 2}}
    networks = int(input("Available Networks\n1.MTN \n2.Airtel \n3.Uganda Telecom \n4.Africell \nEnter the network selection : "))
    if networks in networkCodes:
        toSendPhoneNumber = str(input('Enter the number you are sending to: '))
        if toSendPhoneNumber[1:3] == str(networkCodes[networks]['code']):
            countryCode = "+256 ";activeNumber = countryCode + toSendPhoneNumber[1:]
            size = len(str(activeNumber))
            while size != 14:
                print('Invalid Phone Number')
                toSendPhoneNumber =int(input("Enter the right Phone Number: "))
                size = len(str(toSendPhoneNumber))
            if len(str(toSendPhoneNumber)) == 9:
                return toSendPhoneNumber
        else:
            print('Invalid Phone Number')
            SenderNumberValidation()
    else:
        print("Cannot send to that network")
        #Asking a user if they want to try another network
        choice = int(input('Do you want to try another network?\n 1.Yes \n 2.No : '))
        if choice == 1:
            SenderNumberValidation()
        else:
            print("Thank you for using MTN Mobile Money")
            exit()

    return str(toSendPhoneNumber)