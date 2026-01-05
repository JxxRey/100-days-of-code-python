from tkinter import *
from tkinter.ttk import *


def change_label():
    miles = input.get()
    km = float(miles) * 1.6
    km_amount_label["text"] = km


window = Tk()
window.title("Mile to Km Converter")
window.minsize(750, 500)

#Label
miles_label = Label(text="miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_to_label.grid(column=0, row=1)

km_amount_label = Label(text=0, font=("Arial", 24, "bold"))
km_amount_label.grid(column=1, row=1)

km_label = Label(text="km", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)



#Button
button1 = Button(text="Calculate", command=change_label)
button1.grid(column=1, row=2)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)
input.get()







window.mainloop()