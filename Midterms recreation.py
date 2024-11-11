ACCOUNTS_DATA = [
    {
        "account_number": "34a0",
        "first_name": "Ibong",
        "last_name": "Adarna",
        "pin": "1234",
        "balance": 5000.0,
        "attempts": 0
    },
    {
        "account_number": "95fe",
        "first_name": "Enteng",
        "last_name": "Kabisote",
        "pin": "5678",
        "balance": 10000.0,
        "attempts": 0
    },
    {
        "account_number": "b99c",
        "first_name": "Captain",
        "last_name": "Barbell",
        "pin": "9102",
        "balance": 15000.0,
        "attempts": 0
    }
]

# 1. Function to get account details
def get_account_details(account_number):
    for account in ACCOUNTS_DATA:               # (1) Loop through each account in ACCOUNTS_DATA
        if account["account_number"] == account_number:    # (2) Check if the account number matches
            return account                           # (3) Return the matching account details
    return None                                   # (4) Return None if no account is found

# 2. Quick balance function
def quick_balance():
    account_number = input("Enter your account number: ")  # (5) Prompt for account number
    account_details = get_account_details(account_number)  # (6) Retrieve account details
    if account_details:                                    # (7) Check if account exists
        print("Balance:", account_details["balance"])	# (8) Display balance
    else:
        print("Account not found!")                        # (9) Print message if account is not found

# 3. Login function
def login():
    account_number = input("Enter your account number: ")  # (10) Prompt for account number
    account_details = get_account_details(account_number)  # (11) Retrieve account details
    if ? account_details:                                    # (12) Check if account exists
        return account_details                             # (13) Return account details if found
    while account_details["attempts"] < 3:                 # (15) Allow up to 3 attempts
        pin = input("Enter your PIN: ")                    # (16) Prompt for PIN
        if pin == account_details["pin"]:                  # (17) Check if PIN matches
            account_details["attempts"] = 0                # (18) Reset attempts if successful
							# (19) ?
            return account_details                         # (20) Return account details
        else:
            account_details["attempts"] += 1               # (21) Increment attempts if PIN is incorrect
            remaining_attempts = 3 - account_details["attempts"]  # (22) Calculate remaining attempts
            print("Incorrect PIN. Attempts remaining:", remaining_attempts)	# (23) Reset attempts after failure
    account_details["attempts"] = 0                        	# (24) Account lock message
    print("Account locked. Too many attempts!")            # (24) Account lock message
    return None                                            # (25) Return None if locked

# 4. Check balance function
def check_balance(balance):
    print("Your balance is:", balance)                     # (26) Display balance

# 5. Deposit function
def deposit(account_details):
    deposit_amount = float(input("Enter amount to deposit: "))  # (27) Prompt for deposit amount
								# (28) ?
    account_details["balance"] += deposit_amount                # (29) Add deposit to balance
    print("Deposit successful! New balance:", account_details["balance"])	# (30)

# 6. Withdraw function
def withdraw(account_details):
    withdraw_amount = float(input("Enter amount to withdraw: "))  # (31) Prompt for withdraw amount
									# (32) ?
    if account_details["balance"] >= withdraw_amount:             # (33) Check if balance is sufficient
									# (34) ?
        account_details["balance"] -= withdraw_amount             # (35) Subtract withdrawal from balance

        print("Withdrawal successful! New balance:", account_details["balance"])
    else:
        print("Insufficient balance.")                            # (36) Print message if insufficient funds

# 7. ATM menu function
def atm_menu(account_details):
    is_logged_in = True                                           # is_logged_in initialized to True
    while is_logged_in:
        print("\n- ATM Menu -")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        
        selection = input("\nSelect an option: ")
        if selection == "1":
            check_balance(account_details["balance"])             # Call check_balance
        elif selection == "2":
            deposit(account_details)                              # (37) Call deposit function
        elif selection == "3":
            withdraw(account_details)                             # Call withdraw function
        elif selection == "4":
            print("Logging out")
            is_logged_in = False                                  # (38) Logout, set is_logged_in to False

# 8. Main function
def main():
    while True:
        print("\n- Welcome to the ATM -")
        print("1. Quick Balance")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            quick_balance()                                       # Call quick_balance
        elif choice == "2":
            account_details = login()                             # (39) Call login to get account details
            if account_details:
                atm_menu(account_details)                         # If login is successful, show ATM menu
							# (40) ?
        elif choice == "3":
            print("Thank you for using the ATM. Goodbye!")        
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()


