def check_balance(amount): # It display current balance 
    print(f"Your current balance is: {amount}")

 
def deposit_money(balance): # used to add money into account
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"{amount} deposited successfully.")
    else:
        print("Invalid amount. Please enter a positive number.")
    return balance


def withdraw_money(balance):  # to remove from the account 
    amount = float(input("Enter amount to withdraw: "))
    if amount > 0:
        if amount <= balance: 
            balance -= amount
            print(f" {amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")
    else:
        print("Invalid amount. Please enter only  positive number.")
    return balance

def main():
    amount = 0.0
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            check_balance(amount)
        elif choice == '2':
            amount = deposit_money(amount)
        elif choice == '3':
            amount = withdraw_money(amount)
        elif choice == '4':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please try again after some time.")

main()