#Version 3: Basic GUI Cafe Menu
#27/04/23

import tkinter as tk

#Define menu items and prices
menu = {"Coffee": 2.50, "Tea": 1.50, "Sandwich": 3.00, "Muffin": 2.00, "Salad": 4.00}

#Define functions for login, account creation, and order placement
def create_account():
    username = create_username_entry.get()
    password = create_password_entry.get()
    age = create_age_entry.get()
    if username in users:
        create_error_label.config(text="Username already exists")
    elif not age.isnumeric():
        create_error_label.config(text="Please enter a valid age")
    elif int(age) > 18:
        create_error_label.config(text="You are too old")
    elif int(age) < 13:
        create_error_label.config(text="You are too young")
    else:
        users[username] = {"password": password, "age": age}
        create_success_label.config(text="Account created successfully")
        create_account_frame.pack_forget()
        login_frame.pack()

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username not in users:
        error_label.config(text="Username not found")
    elif users[username]["password"] != password:
        error_label.config(text="Incorrect password")
    else:
        login_frame.pack_forget()
        menu_frame.pack()

def place_order():
    order = []
    for item, price in menu.items():
        if item in var_dict and var_dict[item].get() > 0:
            order.append(f"{item}: {var_dict[item].get()} x ${price:.2f}")
    if order:
        order_label.config(text="\n".join(order))
        total_label.config(text=f"Total: ${sum([menu[item]*var_dict[item].get() for item in var_dict])}")
    else:
        error_label.config(text="Please select at least one item")

#Create root window
root = tk.Tk()
root.geometry("400x400")
root.title("Café Menu App")

#Create intro and login frame
users = {"user": {"password": "pass", "age": "25"}}
login_frame = tk.Frame(root)
login_label = tk.Label(login_frame, text="Welcome to the Café Menu app!\nPlease log in to continue:")
username_label = tk.Label(login_frame, text="Username:")
username_entry = tk.Entry(login_frame)
password_label = tk.Label(login_frame, text="Password:")
password_entry = tk.Entry(login_frame, show="*")
login_button = tk.Button(login_frame, text="Log In", command=login)
error_label = tk.Label(login_frame, text="")
create_account_button = tk.Button(login_frame, text="Create Account", command=lambda: [login_frame.pack_forget(), create_account_frame.pack()])
login_label.pack(pady=20)
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack(pady=10)
error_label.pack()
create_account_button.pack(pady=10)

#Create create account frame
create_account_frame = tk.Frame(root)
create_username_label = tk.Label(create_account_frame, text="Username:")
create_username_entry = tk.Entry(create_account_frame)
create_password_label = tk.Label(create_account_frame, text="Password:")
create_password_entry = tk.Entry(create_account_frame, show="*")
create_age_label = tk.Label(create_account_frame, text="Age:")
create_age_entry = tk.Entry(create_account_frame)
create_button = tk.Button(create_account_frame, text="Create Account", command=create_account)
create_error_label = tk.Label(create_account_frame, text="")
create_success_label = tk.Label(create_account_frame, text="")
create_username_label.pack()
create_username_entry.pack()
create_password_label.pack()
create_password_entry.pack()
create_age_label.pack()
create_age_entry.pack()
create_button.pack(pady=10)
create_error_label.pack()
create_success_label.pack()
create_back_button = tk.Button(create_account_frame, text="Back", command=lambda: [create_account_frame.pack_forget(), login_frame.pack()])
create_back_button.pack()

#Create menu frame
var_dict = {}
menu_frame = tk.Frame(root)
menu_label = tk.Label(menu_frame, text="Please select your items:")
for item, price in menu.items():
    var_dict[item] = tk.IntVar()
    item_checkbutton = tk.Checkbutton(menu_frame, text=f"{item} (${price:.2f})", variable=var_dict[item])
    item_checkbutton.pack()
order_button = tk.Button(menu_frame, text="Place Order", command=place_order)
order_label = tk.Label(menu_frame, text="")
total_label = tk.Label(menu_frame, text="")
back_button = tk.Button(menu_frame, text="Back", command=lambda: [menu_frame.pack_forget(), login_frame.pack()])
menu_label.pack(pady=20)
order_button.pack(pady=10)
order_label.pack()
total_label.pack()
back_button.pack()

#Pack login frame
login_frame.pack()

root.mainloop()
