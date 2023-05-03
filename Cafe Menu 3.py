#Version 3: GUI Cafe Menu
#27/04/23

import tkinter as tk

# Define menu items and prices
menu_items = {"Coffee": 2.50, "Tea": 1.50, "Sandwich": 3.00, "Muffin": 2.00, "Salad": 4.00}

# Define function to calculate order total
def calculate_total(order):
    total = 0
    for item in order:
        total += menu_items[item] * order[item]
    return total

# Define function to print order details
def print_order(order, menu_items, total):
    order_str = ""
    for item in order:
        order_str += f"{item}: {order[item]} x ${menu_items[item]:.2f} = ${menu_items[item] * order[item]:.2f}\n"
    order_str += f"\nTotal: ${total:.2f}"
    return order_str

# Define function to handle "Order" button click
def handle_order():
    # Get selected items and quantities from listbox
    selections = listbox.curselection()
    order = {}
    for i in selections:
        item = listbox.get(i)
        quantity = int(quantities[i].get())
        order[item] = quantity
    # Calculate order total and display order details
    total = calculate_total(order)
    order_str = print_order(order, menu_items, total)
    order_text.config(state="normal")
    order_text.delete("1.0", "end")
    order_text.insert("end", order_str)
    order_text.config(state="disabled")

# Define function to handle "Login" button click
def handle_login():
    username = login_username_entry.get()
    password = login_password_entry.get()
    if username in users and users[username] == password:
        login_username_entry.focus_set()
        # Switch to Order frame
        login_frame.grid_forget()
        order_frame.grid()
    else:
        # Show error message
        error_label.config(text="Invalid username or password")

# Define function to handle "Create Account" button click
def handle_create_account():
    username = create_username_entry.get()
    password = create_password_entry.get()
    age = age_entry.get()
    if int(age) >= 13 and int(age) <= 18:
        users[username] = password
        create_username_entry.focus_set()
        # Switch to Order frame
        login_frame.grid_forget()
        create_account_frame.grid_forget()
        order_frame.grid()
    else:
        # Show error message
        error_label.config(text="You must be between 13 and 18 years old")

# Define users dictionary
users = {}

# Create root window
root = tk.Tk()
root.title("Cafe Menu App")

# Create Login frame
login_frame = tk.Frame(root)
login_frame.grid(row=0, column=0, pady=20)

# Add widgets to Login frame
username_label = tk.Label(login_frame, text="Username:", font=("Arial", 12))
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
login_username_entry = tk.Entry(login_frame, font=("Arial", 12))
login_username_entry.grid(row=0, column=1, padx=10, pady=10)
password_label = tk.Label(login_frame, text="Password:", font=("Arial", 12))
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
login_password_entry = tk.Entry(login_frame, font=("Arial", 12), show="*")
login_password_entry.grid(row=1, column=1, padx=10, pady=10)
login_button = tk.Button(login_frame, text="Login", font=("Arial", 12), command=handle_login)
login_button.grid(row=2, column=0, columnspan=2, pady=20)
error_label = tk.Label(login_frame, text="", font=("Arial", 12), fg="red")
error_label.grid(row=3, column=0, columnspan=2)

# Create Intro frame
intro_frame = tk.Frame(root)

# Add widgets to Intro frame
intro_label = tk.Label(intro_frame, text="Welcome to the Cafe Menu App", font=("Arial", 20))
intro_label.grid(row=0, column=0, padx=10, pady=10)
login_button = tk.Button(intro_frame, text="Login", font=("Arial", 12), command=lambda: intro_frame.grid_forget() or login_frame.grid())
login_button.grid(row=1, column=0, padx=10, pady=10)
create_account_button = tk.Button(intro_frame, text="Create Account", font=("Arial", 12), command=lambda: intro_frame.grid_forget() or create_account_frame.grid())
create_account_button.grid(row=2, column=0, padx=10, pady=10)

# Create Create Account frame
create_account_frame = tk.Frame(root)

# Add widgets to Create Account frame
create_username_label = tk.Label(create_account_frame, text="Username:", font=("Arial", 12))
create_username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
create_username_entry = tk.Entry(create_account_frame, font=("Arial", 12))
create_username_entry.grid(row=0, column=1, padx=10, pady=10)
create_password_label = tk.Label(create_account_frame, text="Password:", font=("Arial", 12))
create_password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
create_password_entry = tk.Entry(create_account_frame, font=("Arial", 12), show="*")
create_password_entry.grid(row=1, column=1, padx=10, pady=10)
age_label = tk.Label(create_account_frame, text="Age:", font=("Arial", 12))
age_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
age_entry = tk.Entry(create_account_frame, font=("Arial", 12))
age_entry.grid(row=2, column=1, padx=10, pady=10)
create_account_button = tk.Button(create_account_frame, text="Create Account", font=("Arial", 12), command=handle_create_account)
create_account_button.grid(row=3, column=0, columnspan=2, pady=20)
error_label = tk.Label(create_account_frame, text="", font=("Arial", 12), fg="red")
error_label.grid(row=4, column=0, columnspan=2)

# Create Order frame
order_frame = tk.Frame(root)

# Add widgets to Order frame
menu_label = tk.Label(order_frame, text="Menu", font=("Arial", 18))
menu_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
quantity_label = tk.Label(order_frame, text="Quantity", font=("Arial", 18))
quantity_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")
listbox = tk.Listbox(order_frame, selectmode="multiple", font=("Arial", 16), height=5)
for item in menu_items:
    listbox.insert("end", item)
listbox.grid(row=1, column=0, padx=10, pady=10)
scrollbar = tk.Scrollbar(order_frame, orient="vertical")
scrollbar.config(command=listbox.yview)
scrollbar.grid(row=1, column=0, padx=(0, 10), pady=10, sticky="nse")
quantities_frame = tk.Frame(order_frame)
quantities_frame.grid(row=1, column=1, padx=10, pady=10)
quantities = []
for item in menu_items:
    quantity = tk.StringVar()
    quantity.set("0")
    quantities.append(quantity)
for i in range(len(menu_items)):
    label = tk.Label(quantities_frame, text="${:.2f}".format(menu_items[listbox.get(i)]), font=("Arial", 16))
    label.grid(row=i, column=0, padx=10, pady=10)
    entry = tk.Entry(quantities_frame, textvariable=quantities[i], font=("Arial", 16), width=5)
    entry.grid(row=i, column=1, padx=10, pady=10)
order_button = tk.Button(order_frame, text="Order", font=("Arial", 16), command=handle_order)
order_button.grid(row=2, column=0, columnspan=2, padx=10, pady=20)
order_text = tk.Text(order_frame, font=("Arial", 16), state="disabled", width=40, height=10)
order_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Pack Intro frame
intro_frame.grid(row=0, column=0, pady=50)

# Run mainloop
root.mainloop()
