from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def find_password():
    """
    Search for stored login credentials for the entered website.

    Retrieves the website name from the input field, then looks it up in 'data.json'.
    If found, displays the stored email and password in a messagebox.
    If the file or website entry is missing, shows an appropriate error message.
    """
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Not Found", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title="Login Information Found",
                                message=f"{website}\nEmail: {data[website]["email"]}\nPassword: {data[website]["password"]}")
        else:
            messagebox.showerror(title="Not Found", message="No details for the website exists")

    ###This was my original solution to creating the find_password function, was recommended to use if/else as preference
    ###instead of raising exceptions.
    # try:
    #     with open("data.json", mode="r") as file:
    #         data = json.load(file)
    #         messagebox.showinfo(title="Login Information Found", message=f"{website}\nEmail: {data[website]["email"]}\nPassword: {data[website]["password"]}")
    # except FileNotFoundError:
    #     messagebox.showerror(title="Not Found", message="No Data File Found")
    # except KeyError:
    #     messagebox.showerror(title="Not Found", message="No details for the website exists")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    """
    Generate a random secure password and copy it to the clipboard.

    Creates a password using a random combination of letters, symbols, and numbers.
    Inserts the generated password into the password entry field and copies it to the clipboard.
    """
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
    """
    Save the entered website, email, and password to a JSON file.

    Validates the input fields, confirms with the user, and then:
    - Updates the existing data in 'data.json' if the file exists.
    - Creates a new file if it does not exist.
    Displays an error if required fields are empty or if the user cancels.
    Clears the input fields after successful save.
    """
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
                "password": password
        }
    }
    if not website_entry.get() or not password_entry.get():
        messagebox.showerror(title="No data entered", message="Website or password field is empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nWebsite: {website} \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                clear_text()

def clear_text():
    """
    Clear the website and password entry fields.

    Resets the input fields to be empty after saving or when needed.
    """
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

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()