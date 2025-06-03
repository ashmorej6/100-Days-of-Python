from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(index=0, string=password)
    pyperclip.copy(password)

 # ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if not website_entry.get() or not password_entry.get():
        messagebox.showerror(title="No data entered", message="Website or password field is emtpy")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nWebsite: {website} \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website}, {email}, {password}\n")
            clear_text()

def clear_text():
    website_entry.delete(0, "end")
    password_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=51)
website_entry.grid(row=1, column=1, columnspan=2, pady=2)

email_entry = Entry(width=51)
email_entry.grid(row=2, column=1, columnspan=2, pady=2)
email_entry.insert(0, "testing@email.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, pady=2)

generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(row=3, column=2,pady=2)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()