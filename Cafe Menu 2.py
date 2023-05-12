#Version 2: Cafe Menu with Improved Functionality
#20/04/23

#Menu Data
menu_data = {
    "1": {"name": "Coffee", "price": 2.50},
    "2": {"name": "Tea", "price": 1.50},
    "3": {"name": "Sandwich", "price": 3.00},
    "4": {"name": "Muffin", "price": 2.00},
    "5": {"name": "Salad", "price": 4.50}
}

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
            print("Invalid username or password.")
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
for item_num, item_data in menu_data.items():
    print(f"{item_num}. {item_data['name']} - ${item_data['price']:.2f}")

#Place Order
order = [] #List to store the order items and quantities
while True:
    item = input("Enter the item number you would like to order (press q to quit): ")
    if item.lower() == 'q':
        break
    elif item not in menu_data:
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
    item_data = menu_data[item]
    item_name = item_data["name"]
    item_price = item_data["price"]
    print(f"{item_name} x {quantity} - ${quantity*item_price:.2f}")
    total += quantity*item_price
print(f"Total: ${total:.2f}")
