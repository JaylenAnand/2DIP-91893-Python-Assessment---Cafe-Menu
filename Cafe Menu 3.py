#Version 3: GUI Cafe Menu
#27/04/23

import tkinter as tk

root = tk.Tk()

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
    username = login_username_entry.get()
    password = login_password_entry.get()
    if username in users and users[username] == password:
        login_username_entry.focus_set()
        #Switch to Order frame
        login_frame.pack_forget()
        order_frame.pack()
    else:
        #Show error message
        error_label.config(text="Invalid username or password")

#Define function to handle "Create Account" button click
def handle_create_account():
    username = create_username_entry.get()
    password = create_password_entry.get()
    age = age_entry.get()
    if int(age) >= 13 and int(age) <= 18:
        users[username] = password
        create_username_entry.focus_set()
        #Switch to Order frame
        login_frame.pack_forget()
        create_account_frame.pack_forget()
        order_frame.pack()
    else:
        #Show error message
        error_label.config(text="You must be between 13 and 18 years old")

#Define users dictionary
users = {}

#Create Login frame
login_frame = tk.Frame(root)

#Create label for username
username_label = tk.Label(login_frame, text="Username:", font=("Arial", 12))
username_label.pack()

#Create entry for username
login_username_entry = tk.Entry(login_frame, font=("Arial", 12))
login_username_entry.pack()

#Create label for password
password_label = tk.Label(login_frame, text="Password:", font=("Arial", 12))
password_label.pack()

#Create entry for password
login_password_entry = tk.Entry(login_frame, font=("Arial", 12), show="*")
login_password_entry.pack()

#Create button for Login frame
login_button = tk.Button(login_frame, text="Login", font=("Arial", 12), command=handle_login)
login_button.pack(pady=10)

#Create label for error messages
error_label = tk.Label(login_frame, text="", font=("Arial", 12), fg="red")
error_label.pack(pady=5)

#Create Intro frame
intro_frame = tk.Frame(root)

#Add Login and Create Account buttons to intro frame
login_button = tk.Button(intro_frame, text="Login", font=("Arial", 12), command=lambda: intro_frame.pack_forget() or login_frame.pack())
login_button.pack(pady=10)

create_account_button = tk.Button(intro_frame, text="Create Account", font=("Arial", 12), command=lambda: intro_frame.pack_forget() or create_account_frame.pack())
create_account_button.pack(pady=10)

#Create Create Account frame
create_account_frame = tk.Frame(root)

#Create label for username
create_username_label = tk.Label(create_account_frame, text="Username:", font=("Arial", 12))
create_username_label.pack()

#Create entry for username
create_username_entry = tk.Entry(create_account_frame, font=("Arial", 12))
create_username_entry.pack()

#Create label for password
create_password_label = tk.Label(create_account_frame, text="Password:", font=("Arial", 12))
create_password_label.pack()

#Create entry for password
create_password_entry = tk.Entry(create_account_frame, font=("Arial", 12), show="*")
create_password_entry.pack()

#Create label for age
age_label = tk.Label(create_account_frame, text="Age:", font=("Arial", 12))
age_label.pack()

#Create entry for age
age_entry = tk.Entry(create_account_frame, font=("Arial", 12))
age_entry.pack()

#Create button for Create Account frame
create_account_button = tk.Button(create_account_frame, text="Create Account", font=("Arial", 12), command=handle_create_account)
create_account_button.pack(pady=10)

#Create Order frame
order_frame = tk.Frame(root)

#Create listbox for menu items
listbox = tk.Listbox(order_frame, selectmode="multiple", font=("Arial", 12))
for item in menu_items:
    listbox.insert("end", item)
listbox.pack(side="left")

#Create scrollbar for listbox
scrollbar = tk.Scrollbar(order_frame, orient="vertical")
scrollbar.config(command=listbox.yview)
scrollbar.pack(side="left", fill="y")

#Create frame for quantities and labels
quantities_frame = tk.Frame(order_frame)
quantities_frame.pack(side="left")

#Create list of quantity variables
quantities = []
for item in menu_items:
    quantity = tk.StringVar()
    quantity.set("0")
    quantities.append(quantity)

#Create labels and entries for quantities
for i in range(len(menu_items)):
    label = tk.Label(quantities_frame, text=menu_items[listbox.get(i)], font=("Arial", 12))
    label.pack()
    entry = tk.Entry(quantities_frame, textvariable=quantities[i], font=("Arial", 12), width=5)
    entry.pack()

#Create button to calculate order total
order_button = tk.Button(order_frame, text="Order", font=("Arial", 12), command=handle_order)
order_button.pack(pady=10)

#Create text widget to display order details
order_text = tk.Text(order_frame, font=("Arial", 12), state="disabled", width=40, height=10)
order_text.pack()

#Pack intro frame
intro_frame.pack(pady=50)

#Run mainloop
root.mainloop()
