from tkinter import *
import requests
THEME_COLOR = "#375362"

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()

    data = response.json()
    kanye_quote = data['quote']
    print(kanye_quote)
    canvas.itemconfig(quote_text, text=f"{kanye_quote}")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg=THEME_COLOR)

canvas = Canvas(width=300, height=414, bg=THEME_COLOR, highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=280, font=("Arial", 30, "bold"),
                                fill="brown")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, bg=THEME_COLOR)
kanye_button.grid(row=1, column=0)

window.mainloop()
