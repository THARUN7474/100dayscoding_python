names_string=input()
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
i=random.randint(0,len(names)-1)
print(f"{names[i]} is going to buy the meal today!")

print("\ntreasure map below one\n")

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
p1=int(position[1])-1
p2=position[0].lower()
l=['a','b','c']
p2index=l.index(p2)
map[p1][p2index]="X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")