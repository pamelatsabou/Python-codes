from tkinter import *
import requests

window = Tk()
window.title("Kanye Says...")
window.config(padx=30, pady=30, bg="white")


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    print(quote)
    canvas.itemconfig(quote_text, text=quote)

canvas = Canvas(width=300, height=414, bg="white")
image1 = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=image1)
canvas.grid(column=0, row=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Times new roman", 30, "bold"), fill="white")



window.mainloop()
