import Ownership
def buyAirtimeFunction():
    print('Buy Airtime')
    airtimeAmount = int (input('How much airtime do you want to buy? '))
    balance = Ownership.accountbalance() - airtimeAmount
    print(f'You have bought {airtimeAmount}  airtime and your balance is {balance:,}')
    print('Thank you for using our services')
    print('Have a nice day')
    exit()