import random
import csv
from datetime import date


accounts = []

def signUp(username, password, age, subscription, balance, sort, rekeningnumber):
    account = {
        "Username: ": username,
        "Password: ": password,
        "Age: ": age,
        "Subscription: ": subscription,
        "Balance: ": balance,
        "Sortcode: ": sort,
        "Rekening Number: ": rekeningnumber
    }
    accounts.append(account)
    # save_accounts_to_csv()

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

def checkPassword():
    Password = input("Enter your password of at least 4 characters, 1 digit and 1 capital letter: ")
    while True:
        if len(Password) >= 4 and any(char.isdigit() for char in Password) and any(char.isupper() for char in Password):
            print("Password Accepted!")
            return Password
        else:
            print("Password does not meet requirements. Please try again.")
            Password = input("Please enter your password again: ")  

def checkUsername():
    username = input("Enter your username of at least 4 characters: ")
    while True:
        if len(username) >= 4:
            print("Username Accepted!")
            return username
        else:
            print("Username does not meet requirements. Please try again.")
            username = input("Please enter your username: ")
            
def login(username, password):
    for account in accounts:
        if account["Username: "] == username and account["Password: "] == password:
            return True

def loginRekening(rekening):
    for account in accounts:
        if account["Rekening Number: "] == rekening:
            return True
            
def welcome():
    while True:
        print("===========================================================")
        print("Welcome to the Bank of Choma")
        print("Option 1: View your Bank Account")
        print("Option 2: Make a Deposit")
        print("Option 3: Make a Withdrawal")
        print("Option 4: Logout")
        print("===========================================================")
        print("Welcome to the Bank of Choma! Enter an Option:")
        option = int(input("Option: "))
        if option == 1:
            for account in accounts:
                if account["Username: "] == username and account["Password: "] == password or account["Rekening Number: "] == rekeningnumber:
                    print("Username: ", account["Username: "])
                    print("Your current balance is: $", account["Balance: "]) 
                    print("Subscription: ", account["Subscription: "])
                    print("Rekening Number: ", account["Rekening Number: "])
                    print("Sortcode: ", account["Sortcode: "])
                    break
        elif option == 2:
            for account in accounts:
                if account["Username: "] == username and account["Password: "] == password or account["Rekening Number: "] == rekeningnumber:
                    print(" ")
                    deposit = int(input("Enter the amount you would like to deposit: "))
                    account["Balance: "] = account["Balance: "] + deposit
                    print(" ")
                    print("Your current balance is: $", account["Balance: "])  
                    print(" ")
        elif option == 3:
            for account in accounts:
                if account["Username: "] == username and account["Password: "] == password or account["Rekening Number: "] == rekeningnumber:
                    print(" ")
                    withdrawal = int(input("Enter the amount you would like to withdraw: "))
                    if account["Subscription: "] == "Standard":
                        if withdrawal > account["Balance: "]:
                            print("Insufficient Funds")
                            break
                        else:
                            account["Balance: "] = account["Balance: "] - withdrawal
                            print("Your current balance is: $", account["Balance: "])
                            break
                    else:
                        account["Balance: "] = account["Balance: "] - withdrawal
                        print("Your current balance is: $", account["Balance: "])
                    print(" ")
        elif option == 4:
            print(" ")
            print("Goodbye!")
            print(" ")
            break
        else:
            print("Invalid option, please try again.")

def save_accounts_to_csv():
    with open('accounts.csv', 'w', newline='') as csvfile:
        fieldnames = ['Username: ', 'Password: ', 'Age: ', 'Subscription: ', 'Balance: ', 'Sortcode: ', 'Rekening Number: ']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for account in accounts:
            writer.writerow(account) 

while True:
    print("Welcome to the Bank of Choma:")
    print("Please select an option to do:")
    print("1. Create a new Account \n2. Create a new gold account \n"
          "3. Login to your account \n4. Quit")
    choice = input("Select:")
    if choice == "1":
        username = checkUsername()
        password = checkPassword()
        year = int(input("Enter your birth year:"))
        month = int(input("Enter your birth month:"))
        day = int(input("Enter your birth day:"))
        age = calculateAge(date(year, month, day))
        sort = len(accounts) + 1
        rekeningnumber = random.randint(00000000, 99999999)
        signUp(username, password, age, "Standard", 0, sort, rekeningnumber)
        print("Welcome to the Bank of Choma")
        welcome()    
    elif choice == "2":
        username = checkUsername()
        password = checkPassword()
        year = int(input("Enter your birth year:"))
        month = int(input("Enter your birth month:"))
        day = int(input("Enter your birth day:"))
        age = calculateAge(date(year, month, day))
        sort = len(accounts) + 1
        rekeningnumber = random.randint(00000000, 99999999)
        if age < 18:
            print("You are not old enough to create a gold account")
        else:
            signUp(username, password, age, "Gold", 0, sort, rekeningnumber)
            print("Welcome to the Bank of Choma")
            welcome()
    elif choice == "3":
        print("1. Login to your account \n2. Forgot Password \n3. Cancel")
        choice = input("Select:")
        if choice == "1":
            username = input("Enter your username:")
            password = input("Enter your password:")
            if login(username, password):
                print("Login successful!")
                welcome()
            else:
                print("Login failed. Please try again.")
        elif choice == "2":
            rekeningnumber = int(input("Enter your rekening number:"))
            if loginRekening(rekeningnumber):
                print("Login successful!")
                welcome()
            else:
                print("Login failed. Please try again.")
        elif choice == "3":
            pass
            
    elif choice == "4":
        print("Thank you for using the Bank of Choma")
        
        break
    elif choice == "test":
        print(accounts)
    else:
        print("Invalid choice")