def numberEntery():
    UserPhoneNumber = (input("Enter your Phone Number: "))
    size = len(str(UserPhoneNumber))
    count = 0
    if not(UserPhoneNumber[1:3] == "77" or UserPhoneNumber[1:3] == "78" or UserPhoneNumber[1:3] == "76"):
        while size != 9:
            print('Invalid Phone Number')
            UserPhoneNumber =int(input("Enter the right Phone Number (078- or 077- or 074-): "))
            count += 1
            size = len(str(UserPhoneNumber))
            if count == 3:
                print("You have entered the wrong number 3 times. Please try again later")
                exit()