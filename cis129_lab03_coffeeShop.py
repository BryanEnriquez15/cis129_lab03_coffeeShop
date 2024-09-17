#cis129_lab03_coffeeShop

# Set Price to coffee and muffin and tax rate
coffee_price = 5.00
muffin_price = 4.00
tax_rate = 0.06


#Get user input for the number of coffee and muffins bought
print("Welcome To My Coffee and Muffin Shop")
num_coffees = int(input("Number of coffees bought?"))
num_muffins = int(input("Number of muffins bought?"))


#Calculate cost before tax
coffee_total = num_coffees * coffee_price
muffin_total = num_muffins * muffin_price
subtotal = coffee_total + muffin_total


#Calculate the tax and total                  
tax = subtotal * tax_rate
total = subtotal + tax


#Print The Recipt
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at ${coffee_price:.2f} each: $ {coffee_total:.2f}")
print(f"{num_muffins} Muffins at ${muffin_price:.2f} each: $ {muffin_total:.2f}")
print("6% tax: $ {tax:.2f}")
print(f"Total: $ {total:.2f}")