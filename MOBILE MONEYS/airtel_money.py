
from calendar import c
balance=1000000
pin_number=1122
def mobile_money(choice):
    # This is the send money function in case the User enters choice 1 and this will be automatically generated
    if choice == 1:
        send_money()
        pass
    #   This is the withdraw money function in case the User enters choice 2 and this will be called in the main function
    elif choice == 2:
        withdraw_money()
    else:
        # This error will  be automatically generated if the user enters a wrong choice
        # But we need a loop here to allow the user enter the right choice not definately stopping the program
        print("Invalid choice")   
    #This is the main function where the user is prompted to enter the choice    
def send_money():
    print(".................SEND MONEY.....................")
    # This is the Option for the user to choose the network to send money to:
    print("1.Send to Airtel Money\n2.Send to Other Networks\n0.Back")
    choice1 = int(input("Enter your choice:"))
    # If the user entered 1 we call the send_to_airtel function
    if choice1 == 1:
        send_to_airtel()
    # If the user enters 2 we call the send_to_other_networks function  
    elif choice1== 2:
        send_to_other_networks()
        
    else:
        print("Invalid choice")  
        #This is the send Airtel to airtel   
def send_to_airtel():
    print(".................SEND TO AIRTEL.....................")
    phone_number = int(input("Enter the phone number:(070,074,075)"))
    if len(phone_number) < 9:
        Amount = int(input("Enter the amount:"))
        if Amount >balance:
            print("Insufficient balance")     
        else:
            print("Transaction successful")
            charges=Amount*0.01
            print("New balance is:",balance-Amount)
            
    else:
        print("Invalid phone number")
# Sending money to other networks function   
def send_to_other_networks():
    # Tell the user to enter the phone number from other networks
    phone_number = int(input("Enter the phone number:(077,078,079)"))
    # If the Number is less than 9 digits
    if int(len(phone_number)) == 10:
        Amount = int(input("Enter the amount:"))
        if Amount >balance:
            print("Insufficient balance")
            # Right amount goes here    
        else:
            print("Transaction successful")
            charges=Amount*0.05
            print("New balance is:",balance-Amount)
            print(f"Your transaction was successful. You have sent {Amount} to {phone_number} and the charges are: {charges}")        
    else:
        print("Invalid phone number")
        # Looping back to allow user enter the right number
          
    #This is the Withdraw money function in case the User enters choice 2    
def withdraw_money():
    print(".................WITHDRAW MONEY.....................")
    withdraw_amount = int(input("Enter the amount:"))
    if withdraw_amount < balance:
        pin_number = int(input("Enter your pin number:"))
        # Validating the  pin number enter the by the user
        if pin_number == pin_number:
            print("Transaction successful")
            print(f"New balance is:{balance-withdraw_amount} and transaction charges are: {withdraw_amount*0.05}")
        # If the pin number is wrong or of greater length of less we show the user the error message
        elif pin_number != pin_number or len(pin_number)>4 or len(pin_number)<4:
            print("Invalid pin number")
            Rightpin_number = int(input("Enter your pin number:"))
            # Create a loop here to allow the user enter the right pin number
            if Rightpin_number == pin_number:
                print("Transaction successful")
                print(f"New balance is:{balance-withdraw_amount} and transaction charges are: {withdraw_amount*0.05}")
                
                
# This is the main function where the user is prompted to enter the choice once they enter the system 
def main():
    print("................AIRTEL MOBILE MONEY.....................")
    print("1.Send Money\n2.Withdraw Money")
    choice = int(input("Enter your choice:"))
    print(mobile_money(choice))
main()
           
        



