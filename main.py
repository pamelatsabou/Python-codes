from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for char in range(randint(8, 10))]
    symbols_list = [choice(symbols) for char in range(randint(2, 4))]
    numbers_list = [choice(numbers) for char in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    # join together elements from the password_list and separate by empty string
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # password = ""
    # for char in password_list:
    #    password += char

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) != 0 and len(password) != 0:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\n"
                                                              f"Password: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Error", message="Make sure you haven't left any field empty")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg='white')
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
# timer_text = canvas.create_text(80, 100, text="MyPass", fill="white", font=("Times new roman", 25, "bold"))
canvas.grid(column=1, row=0)

# Labels
website_text = Label(text="Website:", bg="white", font=("", 10))
website_text.grid(column=0, row=1)
email_text = Label(text="Email/Username:", bg="white", font=("", 10))
email_text.grid(column=0, row=2)
password_text = Label(text="Password:", bg="white", font=("", 10))
password_text.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "reinepamela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# buttons
password_button = Button(text="Generate Password", bg="white", command=generate_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, bg="white", command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
