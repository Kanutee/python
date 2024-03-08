children_meal_price = float(input("Price of meal for children: "))
adult_meal_price = float(input("price of meal for adult: "))
number_of_children = int(input("Enter the number of children: "))
number_of_adult = int(input("Enter the number of adult: "))

meal_subtotal = (children_meal_price * number_of_children) + (adult_meal_price * number_of_adult)
print(f'The meal subtotal is ${meal_subtotal:.2f}')

sales_tax_rate_percentage = float(input("Enter the percentage as such as 6, or 6.5: "))
sales_tax = (meal_subtotal * sales_tax_rate_percentage)/100
meal_price = sales_tax + meal_subtotal
print(f'The meal total is ${meal_price:.2f}')

amount_paid = float(input("Enter the amount paid: "))
balance = amount_paid - meal_price

print(f"Thanks for buying our food. Your balance is ${balance:.2f}")