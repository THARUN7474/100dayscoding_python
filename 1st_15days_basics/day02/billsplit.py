#data types numbers operations type conv f strings
 
# round(678/87,2)....rounding up to 2 decimal places...............%.2f

# type(a);
# +,-,/,//,%...........op
#f_string
# a=1
# b=2
# print(f"your a is {a},your b is {b}")

print("welcome to the bill splitter with tip\n")
a=float(input("what was the total bill?\n"))
b=float(input("what % tip you would like to give ?\n"))
c=float(input("how many persons should share the bill?\n"))
d=(a*(b/100))+a
print("THE each person should pay"+str(round(d/c,2)))
