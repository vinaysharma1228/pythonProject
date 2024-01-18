from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


def open_login_frame(vinay):
    vinay.destroy()
    root = Tk()
    root.title("BCA6")
    root.geometry("600x400")

    # Logo panel
    logo = PhotoImage(file="rk.png")
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

    vinay = Label(root, text="~ Designed by vinay kumar sharma")
    vinay.pack()

    root.mainloop()


def submit():
    username1 = emp_name.get()
    password1 = emp_id.get()
    mobile1 = emp_mobile.get()

    message = f"Hi, {username1}\n You are registered successfully.\n" \
              f"Employee ID: {password1}\nMobile: {mobile1}"

    messagebox.showinfo("Register Successful", message)
    open_login_frame(vinay)

vinay = Tk()
vinay.title("Registration Form ")
vinay.geometry("650x450")
vinay.configure(background="cyan")

# Frame for username, password, and button
frame = Frame(vinay)
frame.configure(background="cyan")
frame.pack()

# Username
username = Label(frame, text="Employee ID ", foreground="blue",background="cyan")
emp_id = Entry(frame)

# Name
password = Label(frame, text="Employee Name", foreground="blue" ,background="cyan")
emp_name = Entry(frame)

# salary
sal = Label(frame, text="Employee Salary", foreground="blue" ,background="cyan")
emp_saly = Entry(frame)

# emp_mobile
mobile = Label(frame, text="Employee mobile", foreground="blue" ,background="cyan")
emp_mobile = Entry(frame)

# emp city
city=Label(frame,text="Select City: ",foreground="blue" ,background="cyan")
combo = Combobox(frame,values=["Rajkot", "Ahmedabad", "Delhi", "Jaipur"])

# Button
submit_button = Button(frame, text="Submit", foreground="white", background="blue", command=submit)

# Grid layout for precise control
username.grid(row=0, column=0, padx=5, pady=5)
emp_id.grid(row=0, column=1, padx=5, pady=5)

password.grid(row=1, column=0, padx=5, pady=5)
emp_name.grid(row=1, column=1, padx=5, pady=5)

sal.grid(row=2, column=0, padx=5, pady=5)
emp_saly.grid(row=2, column=1, padx=5, pady=5)

mobile.grid(row=3, column=0, padx=5, pady=5)
emp_mobile.grid(row=3, column=1, padx=5, pady=5)

city.grid(row=4, column=0, padx=5, pady=5)
combo.grid(row=4, column=1, padx=5, pady=5)

submit_button.grid(row=5, columnspan=2, pady=10)

vinay_label = Label(vinay, text="~ Designed by vinay kumar sharma" ,background="cyan")
vinay_label.pack()

vinay.mainloop()
