#Version 2: Cafe Menu with Improved Functionality
#20/04/23

#Welcome to the Café Menu app
print("Welcome to the Café Menu app for students aged 13-18.")

#List of existing users with usernames and passwords
users = [("jane_doe", "password123"), ("john_smith", "qwerty456")]

#Prompt user to log in or create an account
user_choice = input("Do you want to log in or create an account? Type 'log in' or 'create': ")

#Prompt user to enter login details
if user_choice == "log in":
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        #Check if username and password are correct
        if (username, password) in users:
            print("Login successful!")
            break
        else:
            print("Incorrect username or password. Please try again.")

#Prompt user to create a new account
else:
    while True:
        age = int(input("Please enter your age: "))
        #Check if user is within the age range
        if age < 13 or age > 18:
            print("Sorry, this app is only for students aged 13-18. Please try again later.")
        else:
            #Prompt user to create a new username and password
            username = input("Please enter a username: ")
            password = input("Please enter a password: ")
            #Add new user to the list of users
            users.append((username, password))
            print("Account created successfully!")
            break

#If the user has successfully logged in or created an account, display the menu and prices
if user_choice == "log in" or age >= 13 and age <= 18:
    #Café menu items and prices
    menu_items = {"Coffee": 2.50, "Tea": 1.50, "Sandwich": 3.00, "Muffin": 2.00 ,"Salad": 4.00}

    #Function to calculate order total
    def calculate_total(order):
        total = 0
        for item in order:
            total += menu_items[item] * order[item]
        return total

    #Function to print order details
    def print_order(order, menu_items):
        print("Order details:")
        for item in order:
            print(f"{item}: {order[item]} x ${menu_items[item]:.2f} = ${menu_items[item] * order[item]:.2f}")
        print(f"Total: ${calculate_total(order):.2f}")

    #Prompt user to place an order
    print("Here is the café menu:")
    for item in menu_items:
        print(f"{item}: ${menu_items[item]:.2f}")
    order = {}
    while True:
        item = input("What would you like to order? Type 'done' when finished: ")
        if item == "done":
            break
        elif item not in menu_items:
            print("Sorry, that item is not on the menu. Please try again.")
        else:
            quantity = int(input("How many would you like? "))
            order[item] = quantity

    #Print order details and thank user for using the app
    print_order(order, menu_items)
    print("Thank you for using the Café Menu app!")
else:
    print("Exiting the Café Menu app.") 
