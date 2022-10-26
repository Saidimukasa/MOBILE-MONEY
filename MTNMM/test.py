toSendPhoneNumber = str(input('Enter the number you are sending to: '))
        
countryCode = "+256 ";activeNumber = countryCode + toSendPhoneNumber[1:]
print(activeNumber)
print(len(activeNumber))