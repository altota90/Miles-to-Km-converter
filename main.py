from tkinter import *

#Creating a new Windows

window = Tk()
window.title("Converter Miles to Km")
window.minsize(width=220 , height=100)

# Labels

label_result = Label(text="0 km")
label_result.grid(column=1, row=3)

label_miles = Label(text="Miles:")
label_miles.grid(column=0, row=1)

label_km = Label(text="Km:")
label_km.grid(column=0, row=3)

# Button
def miles_to_km():
    miles = float(entry.get())
    km = miles * 1.60934
    print(label_result)
    label_result.config(text=f"{km:.2f} km")

# Calls actions when pressed

button = Button(text = "Convert", command = miles_to_km)
button. grid(column = 1, row = 0 )

# entries

entry = Entry(width = 10)
entry.grid(column = 1, row = 1)

window.mainloop()