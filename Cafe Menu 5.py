#Version 5: GUI Cafe Menu
#08/05/23

from tkinter import *

#Create the main window
root = Tk()
root.geometry("700x500")
root.title("Cafe Menu App")

#Create two frames
frame_intro = Frame(root, bg="#FCE5CD", width=700, height=500)
frame_menu = Frame(root, bg="#FCE5CD", width=700, height=500)

#Create variables for username, password and age
username = StringVar()
password = StringVar()
age = IntVar()

#Define functions for login and create account
def login():
    if username.get() == "user" and password.get() == "password":
        frame_intro.pack_forget()
        frame_menu.pack()
    else:
        Label(frame_intro, text="Invalid Username or Password", fg="red", bg="#FCE5CD", font=("Arial", 16)).place(x=200, y=300)

def create_account():
    if age.get() > 18:
        Label(frame_intro, text="You are too old", fg="red", bg="#FCE5CD", font=("Arial", 16)).place(x=200, y=300)
    elif age.get() < 13:
        Label(frame_intro, text="You are too young", fg="red", bg="#FCE5CD", font=("Arial", 16)).place(x=200, y=300)
    else:
        #Add username and password to list
        user = [username.get(), password.get()]
        users.append(user)
        #Clear entry fields
        entry_username.delete(0, END)
        entry_password.delete(0, END)
        entry_age.delete(0, END)
        #Show success message
        Label(frame_intro, text="Account created successfully", fg="green", bg="#FCE5CD", font=("Arial", 16)).place(x=200, y=300)

#Define function for placing orders
def place_order():
    #Get user's order
    order = {
        "Coffee": 2.50,
        "Tea": 1.50,
        "Sandwich": 3.00,
        "Muffin": 2.00,
        "Salad": 4.00
    }
    user_order = {}
    for item in order:
        qty = item_qty[item].get()
        if qty:
            user_order[item] = qty
    #Calculate total
    total = sum([order[item]*qty for item, qty in user_order.items()])
    #Display invoice
    invoice = f"{'Item':<15}{'Quantity':<15}{'Price':<15}\n"
    for item, qty in user_order.items():
        price = order[item]*qty
        invoice += f"{item:<15}{qty:<15}{price:<15}\n"
    invoice += f"\n{'Total':<30}{total:>10}"
    Label(frame_menu, text=invoice, fg="black", bg="#FCE5CD", font=("Arial", 16)).place(x=200, y=200)

#Create list to hold user accounts
users = []

#Add widgets to the intro frame
Label(frame_intro, text="Welcome to the Cafe Menu App", fg="#8B0000", bg="#FCE5CD", font=("Arial", 24)).place(x=150, y=50)

Label(frame_intro, text="Username:", fg="black", bg="#FCE5CD", font=("Arial", 16)).place(x=200, y=150)
entry_username = Entry(frame_intro, textvariable=username, font=("Arial", 16))
entry_username.place(x=350, y=150)

Label(frame_intro, text="Password:", fg="black", bg="#FCE5CD", font=("Arial", 16)).place(x=200, y=200)
entry_password = Entry(frame_intro, textvariable=password, show="*", font=("Arial", 16))
entry_password.place(x=350, y=200)

Button(frame_intro, text="Login", bg="#8B0000", fg="white", font=("Arial", 16), command=login).place(x=350, y=250)

Label(frame_intro, text="Don't have an account?", fg="#8B0000", bg="#FCE5CD", font=("Arial", 16)).place(x=200, y=350)

Label(frame_intro, text="Username:", fg="black", bg="#FCE5CD", font=("Arial", 16)).place(x=200, y=400)
entry_username = Entry(frame_intro, textvariable=username, font=("Arial", 16))
entry_username.place(x=350, y=400)

Label(frame_intro, text="Password:", fg="black", bg="#FCE5CD", font=("Arial", 16)).place(x=200, y=450)
entry_password = Entry(frame_intro, textvariable=password, show="*", font=("Arial", 16))
entry_password.place(x=350, y=450)

Label(frame_intro, text="Age:", fg="black", bg="#FCE5CD", font=("Arial", 16)).place(x=200, y=500)
entry_age = Entry(frame_intro, textvariable=age, font=("Arial", 16))
entry_age.place(x=350, y=500)

Button(frame_intro, text="Create Account", bg="#8B0000", fg="white", font=("Arial", 16), command=create_account).place(x=350, y=550)

#Add widgets to the menu frame
Label(frame_menu, text="Cafe Menu", fg="#8B0000", bg="#FCE5CD", font=("Arial", 24)).place(x=300, y=50)

Label(frame_menu, text="Item", fg="black", bg="#FCE5CD", font=("Arial", 16)).place(x=150, y=150)
Label(frame_menu, text="Quantity", fg="black", bg="#FCE5CD", font=("Arial", 16)).place(x=350, y=150)

#Create variables for item quantities
item_qty = {}
for i, item in enumerate(["Coffee", "Tea", "Sandwich", "Muffin", "Salad"]):
    Label(frame_menu, text=item, fg="black", bg="#FCE5CD", font=("Arial", 16)).place(x=150, y=200+i*50)
    item_qty[item] = IntVar()
    Entry(frame_menu, textvariable=item_qty[item], font=("Arial", 16), width=5).place(x=350, y=200+i*50)

Button(frame_menu, text="Place Order", bg="#8B0000", fg="white", font=("Arial", 16), command=place_order).place(x=350, y=450)

#Pack the intro frame
frame_intro.pack()

#Start the main event loop
root.mainloop()