# enter the charge for the food
food_charge = float(input("Enter the charge for the food: $"))

# constants for tip and tax percentages
TIP_PERCENTAGE = 0.18
TAX_PERCENTAGE = 0.07

# calculate the tip and sales tax
tip = food_charge * TIP_PERCENTAGE
sales_tax = food_charge * TAX_PERCENTAGE

# calculate the total price
total_price = food_charge + tip + sales_tax

# display results
print(f"\nTotal Food Charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Total Food Price: ${total_price:.2f}")






