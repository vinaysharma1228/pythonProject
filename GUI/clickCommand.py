
from tkinter import *
from tkinter import messagebox

vinay=Tk()
vinay.geometry("350x350")


def submit():

    message=f"Hi user,You are Register successfully."
    messagebox.showinfo("Login Successful", message)




def register():
    vinay.title("Register Here ")
    frame = Frame(vinay)
    frame.pack()

    # Username
    username = Label(frame, text="Name", foreground="blue")
    user_text = Entry(frame)

    # Password
    password = Label(frame, text="Email", foreground="blue")
    user_pass = Entry(frame)

    # mobile
    mobile = Label(frame, text="Mobile", foreground="blue")
    user_mob = Entry(frame)

    # mobile
    city = Label(frame, text="City", foreground="blue")
    user_city = Entry(frame)

    # Button
    submit_button = Button(frame, text="  Register  ", foreground="white", background="blue",command=submit)

    # Grid layout for precise control
    username.grid(row=0, column=0, padx=5, pady=5)
    user_text.grid(row=0, column=1, padx=5, pady=5)

    password.grid(row=1, column=0, padx=5, pady=5)
    user_pass.grid(row=1, column=1, padx=5, pady=5)

    mobile.grid(row=2, column=0, padx=5, pady=5)
    user_mob.grid(row=2, column=1, padx=5, pady=5)

    city.grid(row=3, column=0, padx=5, pady=5)
    user_city.grid(row=3, column=1, padx=5, pady=5)



    # Place the button below the password label and entry
    submit_button.grid(row=4, columnspan=2, pady=10)


Button(vinay,text="Click to register 👇 ",command=register).pack()

vinay.mainloop()