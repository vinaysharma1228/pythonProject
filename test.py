# QN->1 create a frame with your name the bg color should be navy blue design thw frame size 550x550 insert label left middle
# bank infromation
# 4 text box in the center ,bank id ,bank name ,ifsc code ,city
# # at  the bottom need to submit button

from tkinter import *
from tkinter.ttk import Combobox

vinay = Tk()
vinay.title("Bank Details")
vinay.geometry("550x550")
vinay.configure(background="navy")

frame = Frame(vinay)
frame.configure(background="navy")
frame.pack()

b_label=Label(frame,text=" Enter Bank Details",foreground="white",background="navy")

# bank id
bank = Label(frame, text="Bank ID ", foreground="white",background="navy")
bank_id = Entry(frame)

# Name
bankName = Label(frame, text="Bank Name", foreground="white" ,background="navy")
bank_name = Entry(frame)

# salary
ifsc = Label(frame, text="IFSC Code", foreground="white" ,background="navy")
bank_ifsc = Entry(frame)



# emp city
city=Label(frame,text="Select City: ",foreground="white" ,background="navy")
combo = Combobox(frame,values=["Rajkot", "Ahmedabad", "Delhi", "Jaipur"])

# Button
submit_button = Button(frame, text="Submit", foreground="white", background="blue")

# Grid layout for precise control

b_label.grid(row=0, columnspan=2, padx=5, pady=5)
bank.grid(row=1, column=0, padx=5, pady=5)
bank_id.grid(row=1, column=1, padx=5, pady=5)

bankName.grid(row=2, column=0, padx=5, pady=5)
bank_name.grid(row=2, column=1, padx=5, pady=5)

ifsc.grid(row=3, column=0, padx=5, pady=5)
bank_ifsc.grid(row=3, column=1, padx=5, pady=5)


city.grid(row=4, column=0, padx=5, pady=5)
combo.grid(row=4, column=1, padx=5, pady=5)

submit_button.grid(row=5, columnspan=2, pady=10)

vinay.mainloop()
