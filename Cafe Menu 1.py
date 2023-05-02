#Version 1: Basic Cafe Menu
#13/04/23

#Welcome Message
print("Welcome to the Cafe Menu App!")

#User Login or Signup
existing_user = input("Do you have an account with us? (y/n): ")
if existing_user.lower() == 'y':
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    #TODO: Check username and password in index data
else:
    age = int(input("Please enter your age: "))
    if age < 13 or age > 18:
        print("Sorry, this app is only for students between the ages of 13 and 18.")
        exit()
    else:
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        #TODO: Save username and password in a list
    
#Display Cafe Menu
print("Here's our menu:")
print("1. Coffee - $2.50")
print("2. Tea - $1.50")
print("3. Sandwich - $3.00")
print("4. Muffin - $2.00")
print("5. Salad - $4.50")

#Place Order
order = []  #List to store the order items and quantities
while True:
    item = input("Enter the item number you would like to order (press q to quit): ")
    if item.lower() == 'q':
        break
    quantity = int(input("Enter the quantity: "))
    order.append((item, quantity))
    
#Generate Invoice
print("Invoice:")
total = 0
for item, quantity in order:
    if item == '1':
        item_name = "Coffee"
        item_price = 2.50
    elif item == '2':
        item_name = "Tea"
        item_price = 1.50
    elif item == '3':
        item_name = "Sandwich"
        item_price = 3.00
    elif item == '4':
        item_name = "Muffin"
        item_price = 2.00
    elif item == '5':
        item_name = "Salad"
        item_price = 4.50
    else:
        print(f"Invalid item number: {item}")
        continue
    print(f"{item_name} x {quantity} - ${quantity*item_price:.2f}")
    total += quantity*item_price
print(f"Total: ${total:.2f}")
