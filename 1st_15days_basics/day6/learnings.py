# functions code blocks while loops

def myfun():
    print("heklo")
    print("hello")

myfun()   #calling fun


# resourses-----reeborg's world
# ctrl +] for tab front and ctrl+[ for tab back 
# 4 spaces for idenetation or edut in code editer seetings 
# pep 8 and style guide for python code go refer it 
def turn_left():
    a+2
def move():
    a+1
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#for i in range(0,6):
    #jump()
a=6
while a>0:
    jump()
    a=-1

    # variable height problem
"""
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump(): 
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()
"""



