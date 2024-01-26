# with open("hehe.txt") as f1:
#     f1.readlines()
# #this throws error liek filenotfound error
# we need to know type of errors ..we will with the journey and we need to control the flow using
# exceptional handling we can raise our own error statements to validate user input



#Exception Handling

# import sys
#
# try:
#   some code that may raise an exception
# except Exception as e:
#   exc_type, exc_obj, exc_tb = sys.exc_info()
#   print("Exception Type: ", exc_type.__name__)
#   print("Error Message: ", e.args[0])

# To determine the type of exception that occurred, you can use the sys.exc_info() function inside the except block.
# This function returns a tuple of three values that give information about the exception that is currently being
# handled 1. This will print the name of the exception that occurred. You can also print the error message by
# accessing the args attribute of the exception object:
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except Exception as e:
    print(f"An error occurred: {e}")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up.")

#BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)



# json:
#
# javascript obeject notion a popular data formate used to send data over internet
# json.dump
# jsom.load
# json.update










