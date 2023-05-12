#Version 4: GUI Cafe Menu with Improved Functionality
#01/05/23

from tkinter import *

#Creating GUI Window
root = Tk()
root.title("Cafe Menu")
root.geometry("200x200")

#Creating Login Screen
def login_screen():
    global login_screen
    login_screen = Toplevel(root)
    login_screen.title("Login")

    # Creating Labels and Entries for Login Screen
    Label(login_screen, text="Please enter login details below").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username").pack()
    username_entry = Entry(login_screen)
    username_entry.pack()
    Label(login_screen, text="Password").pack()
    password_entry = Entry(login_screen, show="*")
    password_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", command=login).pack()

#Creating Function to Check Login Credentials
def login():
    global username_entry, password_entry
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        Label(login_screen, text="Please enter valid login details").pack()
    else:
        with open("users.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                login_info = line.strip().split(",")
                if login_info[0] == username and login_info[1] == password:
                    Label(login_screen, text="Login Successful!").pack()
                    login_screen.destroy()
                    menu_screen()
                    break
            else:
                Label(login_screen, text="Invalid login details!").pack()

#Creating Function to Register New Users
def register():
    global username_entry, password_entry, age_entry
    username = username_entry.get()
    password = password_entry.get()
    age = age_entry.get()

    if username == "" or password == "" or age == "":
        Label(register_screen, text="Please enter valid registration details").pack()
    elif int(age) < 13 or int(age) > 18:
        Label(register_screen, text="You are not eligible to use this app!").pack()
    else:
        with open("users.txt", "a") as f:
            f.write(f"{username},{password}\n")
        Label(register_screen, text="Registration Successful!").pack()
        register_screen.destroy()

#Creating Login Screen
def login_screen():
    global login_screen, username_entry
    login_screen = Toplevel(root)
    login_screen.title("Login")

    # Creating Labels and Entries for Login Screen
    Label(login_screen, text="Please enter login details below").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username").pack()
    username_entry = Entry(login_screen)
    username_entry.pack()
    Label(login_screen, text="Password").pack()
    password_entry = Entry(login_screen, show="*")
    password_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", command=login).pack()

#Creating Registration Screen
def register_screen():
    global register_screen, username_entry, password_entry, age_entry
    register_screen = Toplevel(root)
    register_screen.title("Register")

    #Creating Labels and Entries for Registration Screen
    Label(register_screen, text="Please enter registration details below").pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="Username").pack()
    username_entry = Entry(register_screen)
    username_entry.pack()
    Label(register_screen, text="Password").pack()
    password_entry = Entry(register_screen, show="*")
    password_entry.pack()
    Label(register_screen, text="Age").pack()
    age_entry = Entry(register_screen)
    age_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", command=register).pack()


#Creating Function to Register New Users
def register():
    username = username_entry.get()
    password = password_entry.get()
    age = age_entry.get()

    if username == "" or password == "" or age == "":
        Label(register_screen, text="Please enter valid registration details").pack()
    elif int(age) < 13 or int(age) > 18:
        Label(register_screen, text="You are not eligible to use this app!").pack()
    else:
        with open("users.txt", "a") as f:
            f.write(f"{username},{password}\n")
        Label(register_screen, text="Registration Successful!").pack()
        register_screen.destroy()

#Creating Menu Screen
def menu_screen():
    global menu_screen
    menu_screen = Toplevel(root)
    menu_screen.title("Menu")

    #Creating Labels and Entries for Menu Screen
    Label(menu_screen, text="Please choose your order").pack()
    Label(menu_screen, text="").pack()

    #Creating Menu Items
    menu_items = {
        "Coffee": 2.50,
        "Tea": 1.50,
        "Sandwich": 3.00,
        "Muffin": 2.00,
        "Salad": 4.00
    }

    #Creating Checkboxes for Menu Items
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()

    Checkbutton(menu_screen, text="Coffee - $2.50", variable=var1).pack()
    Checkbutton(menu_screen, text="Tea - $1.50", variable=var2).pack()
    Checkbutton(menu_screen, text="Sandwich - $3.00", variable=var3).pack()
    Checkbutton(menu_screen, text="Muffin - $2.00", variable=var4).pack()
    Checkbutton(menu_screen, text="Salad - $4.00", variable=var5).pack()

    #Creating Quantity Entry Fields for Menu Items
    Label(menu_screen, text="").pack()
    Label(menu_screen, text="Enter Quantity for Items Ordered").pack()
    coffee_qty = Entry(menu_screen)
    coffee_qty.pack()
    tea_qty = Entry(menu_screen)
    tea_qty.pack()
    sandwich_qty = Entry(menu_screen)
    sandwich_qty.pack()
    burger_qty = Entry(menu_screen)
    burger_qty.pack()
    pizza_qty = Entry(menu_screen)
    pizza_qty.pack()

    #Creating Buttons for Menu Screen
    Label(menu_screen, text="").pack()
    Button(menu_screen, text="Place Order", command=place_order).pack()
    Button(menu_screen, text="View Order History", command=view_orders).pack()

    #Function to Place Order
    def place_order():
        items = ""
        total = 0

        #Checking if Menu Items are Selected and Adding to Items
        if var1.get() == 1:
            items += f"Coffee x {coffee_qty.get()}, "
            total += 2.5 * int(coffee_qty.get())
        if var2.get() == 1:
            items += f"Tea x {tea_qty.get()}, "
            total += 1.5 * int(tea_qty.get())
        if var3.get() == 1:
            items += f"Sandwich x {sandwich_qty.get()}, "
            total += 3 * int(sandwich_qty.get())
        if var4.get() == 1:
            items += f"Muffin x {muffin_qty.get()}, "
            total += 4 * int(muffin_qty.get())
        if var5.get() == 1:
            items += f"Salad x {salad_qty.get()}, "
            total += 5.5 * int(salad_qty.get())

        #Displaying Order Summary
        order_summary = Toplevel(menu_screen)
        order_summary.title("Order Summary")
        Label(order_summary, text="Order Summary").pack()
        Label(order_summary, text="").pack()
        Label(order_summary, text=items).pack()
        Label(order_summary, text=f"Total: ${total:.2f}").pack()

        #Saving Order to Order History
        with open("orders.txt", "a") as f:
            f.write(f"{items},{total:.2f}\n")

    #Function to View Order History
    def view_orders():
        order_history = Toplevel(menu_screen)
        order_history.title("Order History")
        Label(order_history, text="Order History").pack()
        Label(order_history, text="").pack()

        #Reading Order History from File and Displaying
        with open("orders.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                order_info = line.strip().split(",")
                Label(order_history, text=f"{order_info[0]} - ${order_info[1]}").pack()

#Creating Buttons for Main Screen
Label(root, text="Welcome to Cafe Menu").pack()
Label(root, text="Please log in or register to continue").pack()
Button(root, text="Log In", command=login_screen).pack()
Button(root, text="Register", command=register_screen).pack()

#Running the GUI Window
root.mainloop()
