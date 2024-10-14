from flask import Flask
import random

print(random.__name__)#gives like ---> present parent module --here random
app = Flask(__name__)#here it giives __main__

@app.route("/")#here this is decorater one ---that code part is defined by flask library
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def say_bye():
    return "Bye"


if __name__ == "__main__":
    app.run()

# flask - -app  main  run  ---actualy we use this to run in terminal or seting up envi and falsk run
# but with above if statement we can run simple