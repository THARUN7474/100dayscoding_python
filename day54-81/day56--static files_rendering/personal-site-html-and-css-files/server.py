from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")
#keep all static things in static folder and static files


if __name__ == "__main__":
    app.run(debug=True)