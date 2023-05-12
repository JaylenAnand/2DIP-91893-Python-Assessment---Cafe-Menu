#Version 1: Basic Cafe Menu
#13/04/23

#Credentials Data
credentials_data = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

#Welcome Message
print("Welcome to the Cafe Menu App!")

#User Login or Signup
while True:
    existing_user = input("Do you have an account with us? (y/n): ")
    if existing_user.lower() == 'y':
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if credentials_data.get(username) == password:
            print("Login successful.")
            break
        else:
            print("Invalid Username or Password.")
    else:
        age = int(input("Please enter your age: "))
        if age < 13 or age > 18:
            print("Sorry, this app is only for students between the ages of 13 and 18.")
        else:
            while True:
                username = input("Please enter a username: ")
                if username in credentials_data:
                    print("Username already exists. Please choose a different username.")
                else:
                    password = input("Please enter a password: ")
                    credentials_data[username] = password
                    print("Account created successfully.")
                    break

#Display Cafe Menu
print("Here's our menu:")
print("1. Coffee - $2.50")
print("2. Tea - $1.50")
print("3. Sandwich - $3.00")
print("4. Muffin - $2.00")
print("5. Salad - $4.50")

#Place Order
order = [] #List to store the order items and quantities
while True:
    item = input("Enter the item number you would like to order (press q to quit): ")
    if item.lower() == 'q':
        break
    elif item not in ['1', '2', '3', '4', '5']:
        print("Invalid item number. Please enter a number between 1 and 5.")
        continue
    quantity = int(input("Enter the quantity: "))
    if quantity <= 0:
        print("Invalid quantity. Please enter a positive integer.")
        continue
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

