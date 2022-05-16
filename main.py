from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Label

my_label = Label(text="I am a Label", font=("Times New Roman", 24, ""))
my_label.pack()

# change my_label text
my_label["text"] = "New Text"   # or
my_label.config(text="New Text")

# button
def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()



window.mainloop()
