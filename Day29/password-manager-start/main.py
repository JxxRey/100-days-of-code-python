import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random









# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_text = web_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    all_text = f"{web_text} | {email_text} | {password_text}"

    if web_text or email_text or password_text is None:
        messagebox.showinfo(title="Oops", message="Please don't leave any empty fields!")
    else:
        is_ok = messagebox.askokcancel(title=web_text, message=f"These are the details entered: \nEmail: {email_text} "
                                                               f"\nPassword: {password_text} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as saved_txt:
                saved_txt.write(f"{all_text}\n")
                web_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)



# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
lock_image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= lock_image)
canvas.grid(column=1, row=0)


#Labels
website_label = tk.Label(text="Website")
website_label.grid(column=0, row=1, sticky=EW)

email_label = tk.Label(text="Email/Username")
email_label.grid(column=0, row=2, sticky=EW)

password_label = tk.Label(text="Password")
password_label.grid(column=0, row=3, sticky=EW)

#Buttons
generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky=EW)

add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW)

#Entries
web_entry = tk.Entry(width=52)
web_entry.grid(column=1, row=1, columnspan=2, sticky=E, padx=5, pady=5)
web_entry.focus()

email_entry = tk.Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2, sticky=E, padx=5, pady=5)
email_entry.insert(0, "MyPass@gmail.com")

password_entry = tk.Entry()
password_entry.grid(column=1, row=3, columnspan=1, sticky=EW, padx=5, pady=5)

window.mainloop()











