from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    greetings = "Hello World"
    return render_template("home.html", greetings=greetings)

@app.route('/jacko')
def foobar():
    return '<h1>Hi there, Jacko!</h1>'

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
    app.directory='./'
