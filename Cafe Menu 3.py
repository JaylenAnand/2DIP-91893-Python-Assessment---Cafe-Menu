#Version 3: Basic GUI Cafe Menu
#27/04/23

import tkinter as tk

#Define menu items and prices
menu_items = {"Coffee": 2.50, "Tea": 1.50, "Sandwich": 3.00, "Muffin": 2.00, "Salad": 4.00}

#Define function to calculate order total
def calculate_total(order):
    total = 0
    for item in order:
        total += menu_items[item] * order[item]
    return total

#Define function to print order details
def print_order(order, menu_items, total):
    order_str = ""
    for item in order:
        order_str += f"{item}: {order[item]} x ${menu_items[item]:.2f} = ${menu_items[item] * order[item]:.2f}\n"
    order_str += f"Total: ${total:.2f}"
    return order_str

#Define function to handle "Order" button click
def handle_order():
    #Get selected items and quantities from listbox
    selections = listbox.curselection()
    order = {}
    for i in selections:
        item = listbox.get(i)
        quantity = int(quantities[i].get())
        order[item] = quantity
    #Calculate order total and display order details
    total = calculate_total(order)
    order_str = print_order(order, menu_items, total)
    order_text.config(state="normal")
    order_text.delete("1.0", "end")
    order_text.insert("end", order_str)
    order_text.config(state="disabled")

#Define function to handle "Login" button click
def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        #Switch to Order frame
        login_frame.pack_forget()
        order_frame.pack()
    else:
        #Show error message
        error_label.config(text="Invalid username or password")

#Define function to handle "Create Account" button click
def handle_create_account():
    username = username_entry.get()
    password = password_entry.get()
    age = age_entry.get()
    if int(age) >= 13 and int(age) <= 18:
        users[username] = password
        #Switch to Order frame
        login_frame.pack_forget()
        order_frame.pack()
    else:
        #Show error message
        error_label.config(text="You must be between 13 and 18 years old")

#Create main window
root = tk.Tk()
root.title("Café Menu")

#Create Introduction frame
intro_frame = tk.Frame(root)
intro_frame.pack()

#Create Introduction label
intro_label = tk.Label(intro_frame, text="Welcome to the School Café Click and Collect App!", font=("Arial", 16))
intro_label.pack(pady=20)

#Create "Log In" button
login_button = tk.Button(intro_frame, text="Log In", font=("Arial", 12), command=lambda:[intro_frame.pack_forget(), login_frame.pack()])
login_button.pack(pady=10)

#Create "Create Account" button
create_account_button = tk.Button(intro_frame, text="Create Account", font=("Arial", 12), command=lambda:[intro_frame.pack_forget(), create_account_frame.pack()])
create_account_button.pack()

#Create Login frame
login_frame = tk.Frame(root)

#Create label for username
username_label = tk.Label(login_frame, text="Username:", font=("Arial", 12))
username_label.pack()

#Create Order frame
order_frame = tk.Frame(root)

#Create label for menu
menu_label = tk.Label(order_frame, text="Menu", font=("Arial", 16, "underline"))
menu_label.pack()

#Create listbox for menu items
listbox = tk.Listbox(order_frame, font=("Arial", 12), selectmode="multiple")
for item in menu_items:
listbox.insert("end", item)
listbox.pack()

#Create label and entry for quantities
quantity_label = tk.Label(order_frame, text="Quantity", font=("Arial", 12))
quantity_label.pack()
quantities = []
for item in menu_items:
quantity_entry = tk.Entry(order_frame, font=("Arial", 12), width=5)
quantity_entry.insert("end", "0")
quantity_entry.pack()
quantities.append(quantity_entry)

#Create "Order" button
order_button = tk.Button(order_frame, text="Order", font=("Arial", 12), command=handle_order)
order_button.pack()

#Create text widget for order details
order_text = tk.Text(order_frame, font=("Arial", 12), state="disabled")
order_text.pack()

#Create label for error message
error_label = tk.Label(root, text="", font=("Arial", 12), fg="red")
error_label.pack()

#Define dictionary to store usernames and passwords
users = {"Alice": "1234", "Bob": "5678"}

#Create Introduction frame
intro_frame = tk.Frame(root)
intro_frame.pack()

#Create label for introduction message
intro_label = tk.Label(intro_frame, text="Welcome to Café Menu App", font=("Arial", 16))
intro_label.pack()

#Create "Login" button in Introduction frame
login_button = tk.Button(intro_frame, text="Login", font=("Arial", 12), command=lambda: intro_frame.pack_forget() or login_frame.pack())
login_button.pack()

#Create "Create Account" button in Introduction frame
create_account_button = tk.Button(intro_frame, text="Create Account", font=("Arial", 12), command=lambda: intro_frame.pack_forget() or login_frame.pack())
create_account_button.pack()

#run mainloop
root.mainloop()
