from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

def submit():
    username1 = user_text.get()
    password1 = user_pass.get()
    mobile1 = user_mob.get()
    language1 = combo.get()

    message = f"Hi, {username1}\n You are registered successfully.\n" \
              f"Student Name: {password1}\nMobile: {mobile1}\nLanguage: {language1}"

    messagebox.showinfo("Register Successful", message)

vinay = Tk()
vinay.title("Registration Form ")
vinay.geometry("600x400")

# Frame for username, password, and button
frame = Frame(vinay)
frame.pack()

# Username
username = Label(frame, text="Enrollment", foreground="blue", font=("Arial", 25))
user_text = Entry(frame)

# Name
password = Label(frame, text="Student Name", foreground="blue")
user_pass = Entry(frame)

# Mobile
mobile = Label(frame, text="Mobile", foreground="blue")
user_mob = Entry(frame)

# Language
course = Label(frame, text="Select Language:", foreground="blue")
combo = Combobox(values=["Python", "C", "C++", "Java"])
combo.grid(row=3, column=1, padx=5, pady=5)

# Button
submit_button = Button(frame, text="Submit", foreground="white", background="blue", command=submit)

# Grid layout for precise control
username.grid(row=0, column=0, padx=5, pady=5)
user_text.grid(row=0, column=1, padx=5, pady=5)

password.grid(row=1, column=0, padx=5, pady=5)
user_pass.grid(row=1, column=1, padx=5, pady=5)

mobile.grid(row=2, column=0, padx=5, pady=5)
user_mob.grid(row=2, column=1, padx=5, pady=5)

course.grid(row=3, column=0, padx=5, pady=5)
submit_button.grid(row=4, columnspan=2, pady=10)

vinay_label = Label(vinay, text="~ Designed by vinay kumar sharma")
vinay_label.pack()

vinay.mainloop()
