from tkinter import *
from tkinter import messagebox
window = Tk()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def get_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    entry_password.insert(0,string=f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = entry_website.get()
    email = entry_email.get()
    password =entry_password.get()

    if len(website) == 0 and len(password) == 0:
        messagebox.showerror(title="error" , message="Please enter your details")
    else:
        is_ok =messagebox.askokcancel(title=website , message= f"Your details are :\n email : {email}\n password : {password} \n\nSelect ok to save ")
        if is_ok:
            with open("file.txt", "a") as file1:
                file1.write(f"website: {website} | email: {email} | password: {password}\n")
                entry_email.delete(0,END)
                entry_website.delete(0,END)
                entry_password.delete(0,END)
    
    
# ---------------------------- UI SETUP ------------------------------- #

# window
window.title("Password Manager")
window.config(padx=20 , pady =20)


#canvas
canvas = Canvas(height=200 , width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(row=0, column = 1)


# creating some widget

label_webiste = Label(text="Website:")
label_webiste.grid(row=1 ,column=0)

lablel_email = Label(text= "Email/Username:")
lablel_email.grid(row=2 , column=0)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)
#entry
entry_website = Entry(width=51)
entry_website.focus()
entry_website.grid(row=1 , column=1 , columnspan=2)


entry_email = Entry(width=51)
entry_email.insert(END, "someone@gmail.com")
entry_email.grid(row=2 ,column=1,columnspan=2)


entry_password = Entry(width=33)
entry_password.grid( row=3, column=1)


# button
generate_pass_button = Button(text="Generate Password" , command=get_pass)
generate_pass_button.grid(row=3 , column=2)

add_button = Button(text="Add", width=43,command=add_data)
add_button.grid(row=4,column=1, columnspan=2)
window.mainloop()


    
   