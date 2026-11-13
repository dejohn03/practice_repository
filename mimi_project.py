"""
Write a program that displays a menu with the following three options:

1. Deposit: Ask the user to enter the amount they want to deposit and add it to their account balance.
2. Withdraw: Ask the user to enter the amount they want to withdraw and deduct it from their account balance.
3. Check Balance: Display the user's current account balance.

The program should update the account balance after every deposit or withdrawal and display the remaining balance.
"""


# print("=" * 30)
# print("""THE MENU 
# 1. deposit 
# 2. withdraw
# 3. check balance""")

# def deposit():
#     amount = input("Enter the amount: ")split()
#     titlle.append("amount":amount."done":Fales)
#     print(f"amount:"{amount}" added")


# def withdraw():
#     if not amount:
#         print("insuffience balance")
#         return

# def check_balance():

balance = 0.0

def display_menu():
    print("""
=====Welcome=====
1. Deposit
2. Withdraw
3. Check balance
4. Quit
""")

def deposit():
    global balance
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Enter a postive amount")
            balance += amount
            return f"deposit of {amount} added!. Balance: {balance}"
        except ValueError:
            print("Enter a valid amount")
            continue
        
def withdraw():
    global balance
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Enter a postive amount")
            if balance < amount:
                print("Insufficient funds")
            balance -= amount
            return f"withdrawal of {amount} successful!. Balance: {balance}"
        except ValueError:
            print("Enter a valid amount")
            continue

def check_balance():
    global balance
    return f" your balance is {balance}"

def run():
    
    display_menu()
    while True:
        user_choice = input("Select Option: ").strip()
        if not user_choice:
            print("Select a valid option")
            continue
        
        if user_choice == "1":
            print(deposit())
        elif user_choice == "2":
            print(withdraw())
        elif user_choice == "3":
            print(check_balance())
        elif user_choice == "4":
            exit()
        else:
            print("Select a valid option")
            continue

if __name__ == "__main__":
    run()

    