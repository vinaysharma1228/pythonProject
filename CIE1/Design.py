from tkinter import *
from tkinter import messagebox


def submit():
    username1 = user_text.get()
    password1 = user_pass.get()

    message = f"Hi, {username1}\n You are login successfully."

    messagebox.showinfo("Login Successful", message)


root = Tk()
root.title("BCA6")
root.geometry("600x400")

# Logo panel
logo = PhotoImage(file="../GUI/rk.png")
logo_label = Label(root, image=logo)
logo_label.pack(pady=10)

# Frame for username, password, and button
frame = Frame(root)
frame.pack()

# Username
username = Label(frame, text="Roll No", foreground="blue")
user_text = Entry(frame)

# Password
password = Label(frame, text="Name", foreground="blue")
user_pass = Entry(frame)

# Button
submit_button = Button(frame, text="  Submit  ", foreground="white", background="blue", command=submit)

# Grid layout for precise control
username.grid(row=0, column=0, padx=5, pady=5)
user_text.grid(row=0, column=1, padx=5, pady=5)

password.grid(row=1, column=0, padx=5, pady=5)
user_pass.grid(row=1, column=1, padx=5, pady=5)

# Place the button below the password label and entry
submit_button.grid(row=2, columnspan=2, pady=10)

vinay=Label(root,text="~ Designed by vinay kumar sharma")
vinay.pack()


root.mainloop()
