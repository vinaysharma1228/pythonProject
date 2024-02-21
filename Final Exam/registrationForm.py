from tkinter import *
from tkinter import messagebox


def submit():
    username1 = user_text.get()
    password1 = user_pass.get()
    mobile1 = user_mob.get()

    message = f"Hi, {username1}\n You are registered successfully.\n" \
              f"Student Name: {password1}\nMobile: {mobile1}"

    messagebox.showinfo("Register Successful", message)


vinay = Tk()
vinay.title("Registration Form ")
vinay.geometry("600x400")


frame = Frame(vinay)
frame.pack()


username = Label(frame, text="Enrollment", foreground="blue")
user_text = Entry(frame)


password = Label(frame, text="First Name", foreground="blue")
user_pass = Entry(frame)

last_nm = Label(frame, text="Last Name", foreground="blue")
last_name = Entry(frame)

email = Label(frame, text="Email ", foreground="blue")
email_txt = Entry(frame)

city = Label(frame, text="City ", foreground="blue")
city_txt = Entry(frame)


mobile = Label(frame, text="Mobile", foreground="blue")
user_mob = Entry(frame)


submit_button = Button(frame, text="Submit", foreground="white", background="blue", command=submit)


username.grid(row=0, column=0, padx=5, pady=5)
user_text.grid(row=0, column=1, padx=5, pady=5)

password.grid(row=1, column=0, padx=5, pady=5)
user_pass.grid(row=1, column=1, padx=5, pady=5)

last_nm.grid(row=2, column=0, padx=5, pady=5)
last_name.grid(row=2, column=1, padx=5, pady=5)

mobile.grid(row=3, column=0, padx=5, pady=5)
user_mob.grid(row=3, column=1, padx=5, pady=5)

email.grid(row=4, column=0, padx=5, pady=5)
email_txt.grid(row=4, column=1, padx=5, pady=5)

city.grid(row=5, column=0, padx=5, pady=5)
city_txt.grid(row=5, column=1, padx=5, pady=5)

submit_button.grid(row=5, columnspan=2, pady=10)

vinay_label = Label(vinay, text="~ Designed by vinay kumar sharma")
vinay_label.pack()

vinay.mainloop()
