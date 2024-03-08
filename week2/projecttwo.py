# Ask the user for the price of a child's meal
child_meal_price = float(input("Enter the price of a child's meal: $"))

# Ask the user for the price of an adult's meal
adult_meal_price = float(input("Enter the price of an adult's meal: $"))

# Ask the user for the number of children
num_children = int(input("Enter the number of children: "))

# Ask the user for the number of adults
num_adults = int(input("Enter the number of adults: "))

# Calculate the subtotal
subtotal = (num_children * child_meal_price) + (num_adults * adult_meal_price)

# Display the subtotal
print(f"Subtotal: ${subtotal:.2f}")

# Ask the user for the sales tax rate
sales_tax_rate = float(input("Enter the sales tax rate as a percentage: "))

# Compute and display the sales tax
sales_tax = (subtotal * sales_tax_rate) / 100
print(f"Sales Tax: ${sales_tax:.2f}")

# Compute and display the total price of the meal
total_price = subtotal + sales_tax
print(f"Total Price: ${total_price:.2f}")

# Ask the user for the payment amount
payment_amount = float(input("Enter the payment amount: $"))

# Compute and display the change
change = payment_amount - total_price
print(f"Change: ${change:.2f}")
