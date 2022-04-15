# USSD simulator
# USSD-code = *123#
def USSD():
  user = {'password': '0101', 'acc_no': '123456', 'phone': '123456789', 'balance': 10000, 'airtime': 1000}

  active = True

  while active:

    USSD_code = input("Hello there! \nEnter a valid USSD code: ")
    if (USSD_code != '*123#'):
      print("Oops! USSD is not valid. \nEnter corect USSD next time.")
      return
    option = input("Select option. \nEnter 1 to check balance \nEnter 2 to send money \nEnter 3 to check airtime \n")
    
    # Balance response
    if option and option == '1':
      password = input("Enter password: ")
      
      if password == user['password']:
        print(f"Your balance is: {user['balance']}")
  
    # Send money response
    elif option and option == '2':
      bank = input("Dear customer, kindly select a bank. \nEnter 1 for first bank \nEnter 2 for access bank \nEnter 3 for kuda bank \n")
      if bank and (bank == '1' or bank == '2' or bank == '3'):
        acc = input("Input account number: ")
        if acc and acc == user['acc_no']:
          amt_to_send = input("How much would you like to send: ")
          password = input("Enter password: ")
  
          if (int(amt_to_send) < user['balance'] and password == user['password']):
            print(f"Sending {amt_to_send} to {bank == '1' and 'first bank' or (bank=='2' and 'access bank') or (bank=='3' and 'kuda bank')}")
            user['balance'] = user['balance'] - int(amt_to_send)
            print(f"New balance is {user['balance']}")
      else: print("Transaction cancelled. Bank not available")
  
    # recharge airtime response
    elif option and option == '3':
      phone = input("Dear customer, \nEnter your phone number: ")
      if phone and (phone == user['phone']):
        acc = input("Input account number: ")
        if acc and acc == user['acc_no']:
          amt_to_send = input("How much would you like to send: ")
          password = input("Enter password: ")
  
          if (int(amt_to_send) < user['airtime'] and password == user['password']):
            print(f"Purchasing {amt_to_send} airtime for {user['phone']}")
            user['airtime'] = user['airtime'] + int(amt_to_send)
            user['balance'] = user['balance'] - int(amt_to_send)
            
            print(f"New account balance is {user['balance']}. \nYour recharge was successful. \n you now have {user['airtime']}")
      else: print("Transaction cancelled. \nCheck phone number and try again.")
    
    
    quit = input("Would you like to perform another operation? \nEnter 'n' to quit or any button to continue: ") 
    if quit == 'n':
      active = False

  print("Thanks for your patronage")

  
USSD()
