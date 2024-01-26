import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#f7305b"
ORANGE = "#ffa500"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    label2.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


# import time
# this works in normal consel based thinking so here we are making for GUI
# count = 100
# while True:
#     time.sleep(1)
#     count -=1

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)

                                       #countdown

def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        sec = f"0{sec}"  # we used dynamic typing
    # python is strongly typed and also it is dynamically typed(to change varaibale like a = 3 and later a = "hello"
    # then it shows no error but if now pow(a,2) throws error here strongly typed )
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "👍"
        label2.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("CONCENTRATION HACK")
# window.geometry("1000x1000")
window.config(padx=100, pady=100, bg=YELLOW)

# def say_some(arg):
#     print(arg)
# window.after(1000, say_some, "hello")

canvas = Canvas(width=200, height=236, bg=YELLOW, highlightthickness=0)
bg_img = PhotoImage(file="tomato.png")  # remember path and file paths giving
canvas.create_image(100, 118, image=bg_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, "38", "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, "40", "bold"), bg=YELLOW, highlightthickness=0)
label.grid(row=0, column=1)

start = Button(text="start", highlightthickness=0, width=10, bg=ORANGE, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="reset", highlightthickness=0, width=10, command=reset_timer)
reset.grid(row=2, column=2)

label2 = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
label2.grid(row=3, column=1)

window.mainloop()
