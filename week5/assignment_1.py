shopping_cart = []

while True:
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    choice = input("Please enter an action: ")

    if choice == '1':
        item_name = input("What item would you like to add? ")
        shopping_cart.append(item_name)
        print(f"'{item_name}' has been added to the cart.\n")

    elif choice == '2':
        print("The contents of the shopping cart are:")
        for index, item in enumerate(shopping_cart, start=1):
            print(f"{index}. {item}")
        print()

    elif choice == '5':
        print("Thank you. Goodbye.")
        break
