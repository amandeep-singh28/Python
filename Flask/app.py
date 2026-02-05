from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def printHello():
    return render_template("hello.html")
    # return "Hello World"