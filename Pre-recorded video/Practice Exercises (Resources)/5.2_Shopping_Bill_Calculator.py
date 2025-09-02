#Exercise 5.2: Shopping Bill Calculator 
# Task: Calculate total bill with discount and tax. 
# Given: item_prices = [25.99, 12.50, 8.75, 45.00] 
# discount_percent = 15 # 15% discount 
# tax_percent = 8.5 # 8.5% tax 
# Calculation Steps: 
# Calculate subtotal 
# Apply discount 
# Apply tax on discounted amount 
# Expected Output: 
# Item prices: [25.99, 12.5, 8.75, 45.0] 
# Subtotal: $92.24 
# After 15% discount: $78.40 
# After 8.5% tax: $85.06 
# Final bill: $85.06,
# item_prices = [25.99, 12.50, 8.75, 45.00] 
# discount_percent = 15 # 15% discount 
# tax_percent = 8.5 # 8.5% tax 
# # Your solution here: 
# # Step 1: Sum all prices 
# # Step 2: Subtract discount (subtotal * discount_percent / 100) 
# # Step 3: Add tax (discounted_amount * tax_percent / 100)

item_prices = [25.99, 12.50, 8.75, 45.00]
discount_percent = 15  # 15% discount
tax_percent = 8.5      # 8.5% tax

# Subtotal
subtotal = sum(item_prices)
print(f"Item prices: {item_prices}")
print(f"Subtotal: ${subtotal:.2f}")

# Apply discount
discounted_amount = subtotal * (1 - discount_percent/100)
print(f"After {discount_percent}% discount: ${discounted_amount:.2f}")

# Apply tax
final_bill = discounted_amount * (1 + tax_percent/100)
print(f"After {tax_percent}% tax: ${final_bill:.2f}")
print(f"Final bill: ${final_bill:.2f}")

