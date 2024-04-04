shopping_cart = []
prices = []

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
        item_price = float(input(f"What is the price of '{item_name}'? "))
        shopping_cart.append(item_name)
        prices.append(item_price)
        print(f"'{item_name}' has been added to the cart.\n")

    elif choice == '2':
        print("The contents of the shopping cart are:")
        for index, item in enumerate(shopping_cart, start=1):
            print(f"{index}. {item} - ${prices[index-1]:.2f}")
        print()

    elif choice == '3':
        if len(shopping_cart) == 0:
            print("Your cart is already empty.")
        else:
            item_to_remove = int(input("Which item would you like to remove? ")) - 1
            if 0 <= item_to_remove < len(shopping_cart):
                removed_item = shopping_cart.pop(item_to_remove)
                removed_price = prices.pop(item_to_remove)
                print(f"'{removed_item}' has been removed from the cart.\n")
            else:
                print("Invalid item number.")

    elif choice == '4':
        total_price = sum(prices)
        print(f"The total price of the items in the shopping cart is ${total_price:.2f}\n")

    elif choice == '5':
        print("Thank you. Goodbye.")
        break
