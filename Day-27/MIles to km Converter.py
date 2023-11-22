from tkinter import *

window = Tk()
window.title("Miles to Km Converter!")
window.config(padx=20, pady=20)


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_value.config(text=f"{km}")

# Enteries

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

# Labels

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

miles_middle_var = Label(text="is equal to")
miles_middle_var.grid(row=1, column=0)

km_result_value = Label(text="0")
km_result_value.grid(row=1, column=1)

label_km = Label(text="km")
label_km.grid(row=1, column=3)


# Button

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()
