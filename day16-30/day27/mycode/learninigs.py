# import tkinter#if this is not there we have use belowline if we use this for everyclass we need mention like
#tkinter.tk() or tkinker.anyclassname

from  tkinter import *

window = Tk()
window.title("my 1st GUI project")
window.minsize(width=500, height=300)

#label

my_label = Label(text="i am label", font=("Arial", 24,"bold"))
my_label.pack()#this is must
# my_label.pack(expand= True)
# my_label.pack(side="left")
# my_label.pack(side="bottom")



def button_clicked():
    # print("i am used")
    # my_label["text"] =
    my_label.config(text=input.get())

#bottom
button = Button(text="use me", command=button_clicked)
button.pack()

#entry
input = Entry(width=10)
input.pack()# actually we are using pack everytime to give layout to make work its fun we need to keep it on screen
# so pack do that automatically
print(input.get())
my_label["text"]=input.get()





#arguments of funtion
# what is funtion
# parameters and attributes of python
# positional arguments and keyword arguments
# and feault arguments
# unlimited argments.....*args
# def add(*args):
#     for n in args:
#         print(n)#here * isimpt not args it can be *tharun too it will be tuple more to say it is  unlimted positional arguments


# unlimited keywords arguments -----**kwargs name doesnt matter its all ** it will be a dict
#
# def cal(**kwargs):
#     print(kwargs)
#     for key,value in kwargs.items():
#         print(key,value)
#     print(kwargs["math"])
#
#
# cal(math="hello",sum=5)


# *args: Positional Variable-Length Arguments
def add(*args):
    # print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(3, 5, 6, 2, 1, 7, 4, 3))


# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)



# while True:
#     pass...simply keep the screen on forever we have method for it
window.mainloop()