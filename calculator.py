
# q2-> design 350x350 frame with 2 text_box and 4 button
from tkinter import *

def add():
    a=firstNumber.get()
    b=secondNumber.get()
    a=int(a)
    b=int(b)
    sum=a+b

    ans2=Label(frame,text=f"Addition : {sum}",foreground="white",background="navy",font=("Arial",16))
    ans2.grid(row=3, columnspan=3, pady=5)


def sub():
    a=firstNumber.get()
    b=secondNumber.get()
    a=int(a)
    b=int(b)
    sb=a-b

    ans2=Label(frame,text=f"Subrtaction : {sb}",foreground="white",background="navy",font=("Arial",16))
    ans2.grid(row=3, columnspan=3, pady=5)

vinay = Tk()
vinay.title("Calculator")
vinay.geometry("350x350")
vinay.configure(background="navy")

frame = Frame(vinay)
frame.configure(background="navy")
frame.pack()


# first number
first = Label(frame, text="First Number ", foreground="white",background="navy")
firstNumber = Entry(frame)

# second
second = Label(frame, text="Second Number ", foreground="white" ,background="navy")
secondNumber = Entry(frame)

# show result:

# Plus Button
plus_button = Button(frame, text="+", foreground="white", background="blue",font=("Arial",16),command=add)
minus_button = Button(frame, text="-", foreground="white", background="blue",font=("Arial",16),command=sub)
multiplication_button = Button(frame, text="x", foreground="white", background="blue",font=("Arial",16))
division_button = Button(frame, text="/", foreground="white", background="blue",font=("Arial",16))

# Grid layout for precise control

first.grid(row=0, column=1, padx=5, pady=5)
firstNumber.grid(row=0, column=2, padx=5, pady=5)

second.grid(row=1, column=1, padx=5, pady=5)
secondNumber.grid(row=1, column=2, padx=5, pady=5)


plus_button.grid(row=2, column=0, pady=5)
minus_button.grid(row=2, column=1, pady=5)
multiplication_button.grid(row=2, column=2, pady=5)
division_button.grid(row=2, column=3, pady=5)

vinay.mainloop()