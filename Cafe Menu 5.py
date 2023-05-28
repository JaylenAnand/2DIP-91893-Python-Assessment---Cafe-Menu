#Version 5: GUI Cafe Menu
#11/05/23

import tkinter as tk
from PIL import ImageTk, Image

#Define menu items and prices
menu = {
    "Coffee": 2.50,
    "Tea": 1.50,
    "Sandwich": 3.00,
    "Muffin": 2.00,
    "Salad": 4.00
}

#Define quantity
quantity_dict = {}

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
        #Display "Username not found" error message
        username_error_label.config(text="Username not found")
        password_error_label.config(text="")
    elif users[username]["password"] != password:
        #Display "Password incorrect" error message
        username_error_label.config(text="")
        password_error_label.config(text="Password incorrect")
    else:
        login_frame.pack_forget()
        menu_frame.pack()

def place_order():
    menu_frame.pack_forget()  #Clear previous selection
    order = []
    total = 0

    for item, price in menu.items():
        if item in quantity_dict:
            quantity_entry = quantity_dict[item]
            quantity = quantity_entry.get().strip()  #Get the quantity entered by the user

            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                order.append(f"{item}: {quantity} x ${price:.2f}")
                total += price * quantity

    if order:
        order_label.config(text="\n".join(order))
        total_label.config(text=f"Total: ${total:.2f}")
        order_frame.pack()  #Display the order frame
    else:
        error_label.config(text="Please select at least one item")

#Create root window
root = tk.Tk()
root.geometry("400x500")
root.title("Café Menu App")
root.configure(bg="#F7F3E9")

#Create intro and login frame
users = {"user": {"password": "pass", "age": "25"}}
login_frame = tk.Frame(root, bg="#F7F3E9")
login_label = tk.Label(login_frame, text="Welcome to the Cafe Menu app!\nPlease log in to continue:", bg="#F7F3E9", fg="#605F5E", font=("Arial", 14, "bold"))
username_label = tk.Label(login_frame, text="Username:", bg="#F7F3E9", fg="#605F5E", font=("Arial", 12))
username_entry = tk.Entry(login_frame, font=("Arial", 12))
password_label = tk.Label(login_frame, text="Password:", bg="#F7F3E9", fg="#605F5E", font=("Arial", 12))
password_entry = tk.Entry(login_frame, show="*", font=("Arial", 12))
login_button = tk.Button(login_frame, text="Log In", command=login, bg="#D8D0D1", fg="#605F5E", font=("Arial", 12, "bold"))
error_label = tk.Label(login_frame, text="", bg="#F7F3E9", fg="#FF0000", font=("Arial", 12, "bold"))
create_account_button = tk.Button(login_frame, text="Create Account", command=lambda: [login_frame.pack_forget(), create_account_frame.pack()], bg="#D8D0D1", fg="#605F5E", font=("Arial", 12, "bold"))
login_label.pack(pady=20)
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack(pady=10)
error_label.pack()
create_account_button.pack(pady=10)
username_error_label = tk.Label(login_frame, text="", bg="#F7F3E9", fg="#FF0000", font=("Arial", 12, "bold"))
password_error_label = tk.Label(login_frame, text="", bg="#F7F3E9", fg="#FF0000", font=("Arial", 12, "bold"))
username_error_label.pack()
password_error_label.pack()


#Create create account frame
create_account_frame = tk.Frame(root, bg="#F7F3E9")
create_username_label = tk.Label(create_account_frame, text="Username:", bg="#F7F3E9", fg="#605F5E", font=("Arial", 12))
create_username_entry = tk.Entry(create_account_frame, font=("Arial", 12))
create_password_label = tk.Label(create_account_frame, text="Password:", bg="#F7F3E9", fg="#605F5E", font=("Arial", 12))
create_password_entry = tk.Entry(create_account_frame, show="*", font=("Arial", 12))
create_age_label = tk.Label(create_account_frame, text="Age:", bg="#F7F3E9", fg="#605F5E", font=("Arial", 12))
create_age_entry = tk.Entry(create_account_frame, font=("Arial", 12))
create_button = tk.Button(create_account_frame, text="Create Account", command=create_account, bg="#D8D0D1", fg="#605F5E", font=("Arial", 12, "bold"))
create_error_label = tk.Label(create_account_frame, text="", bg="#F7F3E9", fg="#FF0000", font=("Arial", 12, "bold"))
create_success_label = tk.Label(create_account_frame, text="", bg="#F7F3E9", fg="#008000", font=("Arial", 12, "bold"))
create_username_label.pack()
create_username_entry.pack()
create_password_label.pack()
create_password_entry.pack()
create_age_label.pack()
create_age_entry.pack()
create_button.pack(pady=10)
create_error_label.pack()
create_success_label.pack()
create_back_button = tk.Button(create_account_frame, text="Back", command=lambda: [create_account_frame.pack_forget(), login_frame.pack()], bg="#D8D0D1", fg="#605F5E", font=("Arial", 12, "bold"))
create_back_button.pack()

#Create menu frame
var_dict = {}
menu_frame = tk.Frame(root, bg="#F7F3E9")
menu_label = tk.Label(menu_frame, text="Please select your items:", bg="#F7F3E9", fg="#605F5E", font=("Arial", 14, "bold"))
menu_label.pack(pady=10)
for item, price in menu.items():
    var_dict[item] = tk.IntVar()
    item_frame = tk.Frame(menu_frame, bg="#F7F3E9")
    
    #Load and display menu item image
    img = ImageTk.PhotoImage(Image.open(f"{item.lower()}.png").resize((50, 50)))
    item_image_label = tk.Label(item_frame, image=img, bg="#F7F3E9")
    item_image_label.image = img
    item_image_label.pack(side="left")
    
    item_checkbutton = tk.Checkbutton(item_frame, text=f"{item} (${price:.2f})", variable=var_dict[item], bg="#F7F3E9", font=("Arial", 12))
    item_checkbutton.pack(side="left")
    
    quantity_entry = tk.Entry(item_frame, width=4, font=("Arial", 12))
    quantity_entry.pack(side="left")
    
    quantity_dict[item] = quantity_entry  #Store quantity entry in a dictionary
    
    item_frame.pack(pady=5)
    
order_button = tk.Button(menu_frame, text="Place Order", command=place_order, bg="#D8D0D1", fg="#605F5E", font=("Arial", 12, "bold"))
order_button.pack(pady=10)
error_label = tk.Label(menu_frame, text="", bg="#F7F3E9", fg="#FF0000", font=("Arial", 12, "bold"))
error_label.pack()

#Create order frame
order_frame = tk.Frame(root, bg="#F7F3E9")
order_label = tk.Label(order_frame, text="", bg="#F7F3E9", fg="#605F5E", font=("Arial", 12))
order_label.pack(pady=10)
total_label = tk.Label(order_frame, text="", bg="#F7F3E9", fg="#605F5E", font=("Arial", 12, "bold"))
total_label.pack()
back_button = tk.Button(order_frame, text="Back to Menu", command=lambda: [order_frame.pack_forget(), menu_frame.pack()], bg="#D8D0D1", fg="#605F5E", font=("Arial", 12, "bold"))
back_button.pack(pady=10)

#Display login frame
login_frame.pack()

root.mainloop()
