import tkinter as tk

def move_text():
    canvas.move(text_id, 5, 0)
    canvas.after(100, move_text)

root = tk.Tk()
root.title("Happy Birthday Animation")

canvas = tk.Canvas(root, width=400, height=200, bg="lightblue")
canvas.pack()

# Set the initial position of the text
text_id = canvas.create_text(0, 100, text="Happy Birthday!", font=("Helvetica", 20), anchor="w")

# Call the move_text function to create animation
move_text()

root.mainloop()
