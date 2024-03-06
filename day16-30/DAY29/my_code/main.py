from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    text3.insert(0, password)
    pyperclip.copy(password)


def save():
    websitet = text1.get()
    emailt = text2.get()
    passwordt = text3.get()

    if len(websitet) == 0 or len(passwordt) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=websitet, message=f"These are the details entered: \nEmail: {emailt} "
                                                      f"\nPassword: {passwordt} \nIs it ok to save?")
        if is_ok:
            with open("passwords.txt", "a") as file1:
                file1.write(f"website: {websitet} || email/username: {emailt} || pass: {passwordt}\n")
            text1.delete(0, END)
            text3.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password manager")
window.config(pady=35, padx=35)


canvas = Canvas(height=300, width=300)
myimg = PhotoImage(file='logo.png')
canvas.create_image(200, 200, image=myimg, anchor="center") #,anchor='nw')
canvas.grid(row=0, column=1)

label1 = Label(width=20, text="WEBSITE:")
label1.grid(row=1, column=0)

text1 = Entry(width=60)
text1.grid(row=1, column=1, columnspan=2)
text1.focus()

label2 = Label(width=20, text="EMAIL/UserName:")
label2.grid(row=2, column=0)

text2 = Entry(width=60)
text2.grid(row=2, column=1, columnspan=2)
text2.insert(END,"bandatharun74@gmail.com")
label3 = Label(width=20, text="Password:")
label3.grid(row=3, column=0)

text3 = Entry(width=39)
text3.grid(row=3, column=1)


button1 = Button(width=20, text="Generate Password", command=generate_password)
button1.grid(row=3, column=2)


button2 = Button(width=60, text="ADD",  command=save)
button2.grid(row=4, column=1, columnspan=2)

window.mainloop()