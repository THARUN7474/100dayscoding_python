from tkinter import *

def miles_km():
    miles = float(miles_input.get())
    km = miles * 1.689
    kilometer__result_label.config(text=f"{km}")

window = Tk()
window.title("MILES TO KM CONVERTER")
window.config(padx=200,pady=200)
window.minsize(width=500, height=300)

miles_input = Entry(width=100)
miles_input.grid(row=0,column=1)
miles_label = Label(text="miles")
miles_label.grid(row=0,column=1)

# equal_label = Label(text="is equal to")
# equal_label.grid(row=2, column=0)
equal_label = Label(text="equal to")
equal_label.grid(row=1,column=0)


kilometer__result_label = Label(text="0")
kilometer__result_label.grid(row=1,column=1)

km_label = Label(text="km")
km_label.grid(row=2,column=1)

cal_button = Button(text="calculate", command=miles_km)
cal_button.grid(row=2,column=0)




window.mainloop()