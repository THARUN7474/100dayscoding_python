# import other
#
# print("hello")
# print(f"i am from other module and i am her by importing {other.a}")
# # import turtle
# # ben = turtle.Turtle()
# # here ben is object a thing of blueprint(class) that is Turtle which is in turtle module
# # every object or class as 2 things such as methods and attributes(variables)
# # this all can be written as___--
#
# from turtle import Turtle, Screen
# ben = Turtle()
# my_screen = Screen()
# print(ben)
# print("str")
# print(ben.shape("turtle"))
# ben.color("red")
# ben.forward(100)
# ben.circle(5)
# print(my_screen.canvasheight)
# print(my_screen.exitonclick())
# print("there is diff btw packages(install from pypy) and in pycharm
#    settings>project>projectintrepeter>name>install--is something which is collection of alot of code and modules and
# modules --a file " "we can say some code which has some classes")

# ................................................................................................................

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("pokemon name",["pikachu", "squrital" , "charmindar"])
table.add_column("type" , ["electric","water","fire"])
table.align = "l"
print(table._align)
print(table)

