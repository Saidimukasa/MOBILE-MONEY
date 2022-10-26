import SendMoney, WithdrawMoney,BuyData, BuyAirtime
def activity():
    activity = input('What do you want to do? \n1. Send Money, \n2. Withdraw Money, \n3. Buy Airtime, \n4. Buy Data: ')
    if activity == '1':
        SendMoney.sendMoneyFunction()
    elif activity == '2':
        WithdrawMoney.withdrawMoneyFunction()
    elif activity == '3':
        BuyAirtime.buyAirtimeFunction()
    elif activity == '4':
        BuyData.buyDataFunction()
    else:
        print('Invalid Option!!')
        activity()