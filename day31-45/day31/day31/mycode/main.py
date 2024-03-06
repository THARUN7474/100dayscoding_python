from tkinter import *
import pandas
import random

# from tkinter import messagebox
import time

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/to_learn_words.csv")
except:
    data = pandas.read_csv("data/french_words.csv")
    data_dict1 = data.to_dict(orient="records")
else:
    data_dict1 = data.to_dict(orient="records")


# print(data_dict1)
# data_dict = data.to_dict()
# l = list(data_dict.values())
# g = [x for x in l[0].values()]
# print(g)
# print(l)
# # new_data_dict = [value for (key,value) in data_dict]
# print(data_dict)
# # print(new_data_dict)
def generate_card():
    global ran, flip_timer
    window.after_cancel(flip_timer)
    ran = random.choice(data_dict1)
    text1 = ran["French"]
    # print(text1)
    canvas.itemconfig(title1, text="FRENCH", fill="black")
    canvas.itemconfig(word, text=text1, fill="black")
    canvas.itemconfig(img, image=card1_img)
    flip_timer = window.after(3000, change_card_side)


def change_card_side():
    canvas.itemconfig(title1, text="English", fill="white")
    canvas.itemconfig(word, text=ran["English"], fill="white")
    canvas.itemconfig(img, image=card2_img)


def generate_remove_card():
    global ran
    data_dict1.remove(ran)
    dataa = pandas.DataFrame(data_dict1)
    dataa.to_csv("data/to_learn_words.csv", index=False)
    generate_card()


window = Tk()
window.title("FLASH_CARD")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=change_card_side)

canvas = Canvas(height=600, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card1_img = PhotoImage(file="images/card_front.png")
img = canvas.create_image(400, 300, image=card1_img)
title1 = canvas.create_text(400, 180, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 300, text="Word", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

card2_img = PhotoImage(file="images/card_back.png")
# canvas.create_image(400, 300, image=card2_img)

card3_img = PhotoImage(file="images/wrong.png")
# canvas.create_image(400, 300, image=card3_img)

card4_img = PhotoImage(file="images/right.png")
# canvas.create_image(400, 300, image=card4_img)

wrong = Button(image=card3_img, highlightthickness=0, command=generate_remove_card)
wrong.grid(row=1, column=0)

correct = Button(image=card4_img, command=generate_card)
correct.grid(row=1, column=1)

# label1 = Label(text="Title", font=("Arial",40,"italic"), bg="white")
# label1.grid(row=0, column=0)
# label2 = Label(text="Word", font=("Arial",40,"bold"), bg="white")
# label2.grid(row=0, column=1)


generate_card()

window.mainloop()
