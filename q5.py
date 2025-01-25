def display_menu():
    print("Shopping Cart Menu:")
    print("1. Add item")
    print("2. View cart")
    print("3. Calculate total")
    print("4. Exit")

def add_item(cart):
    item = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    cart.append((item, price))
    print(f"{item} has been added to the cart.")

def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for item, price in cart:
            print(f"{item}: {price:.2f}")

def calculate_total(cart):
    total = 0
    for item,price in cart:
        total += price
    print(f"Total price: {total:.2f}")

def main():
    cart = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_item(cart)
        elif choice == '2':
            view_cart(cart)
        elif choice == '3':
            calculate_total(cart)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()