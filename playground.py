from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play/<int:x>/<color>')
def play(x,color):
    return render_template("squares.html", x = x, color = color)

@app.route('/play/<int:x>')
def play1(x):
    return render_template("squares.html", x = x, color = "blue")

@app.route('/play')
def play2():
    return render_template("squares.html", x = 3, color = "red")


if __name__ == '__main__':
    app.run(debug = True)