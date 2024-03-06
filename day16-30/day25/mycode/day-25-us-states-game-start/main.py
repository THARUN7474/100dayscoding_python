# turtle works only with gif formate pics

import turtle

screen = turtle.Screen()
screen.title("GUESSING STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# def get_mouse_co-ordinates(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_co-ordinates)
# turtle.mainloop()
# used this to gather co-ordinates of all the states from map of turtle screen to use later

import pandas

data = pandas.read_csv("50_states.csv")

l = data.state.to_list()# l = list(data.state)
g = []
# print(l)
while len(g) < 50:
    answer_state = (turtle.textinput(title=f"{len(g)}/50-GUEESED CORRECT", prompt="enter name")).capitalize()
    # print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in l:
            if state not in g:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in l:
        g.append(answer_state)
        output = turtle.Turtle()
        output.hideturtle()
        output.penup()
        x_cor = int(data[data.state == answer_state].x.iloc[0])
        y_cor = int(data[data.state == answer_state].y.iloc[0])
        output.goto(x_cor, y_cor)
        output.write(answer_state)  # state_data.state.item() we can use to get direct state name
        # , align = "center", font = ("Arial", 10, "Normal")


# screen.mainloop()
# screen.exitonclick()
