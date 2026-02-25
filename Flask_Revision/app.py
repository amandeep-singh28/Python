from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        name = request.form.get("username")
        age = request.form.get("age")
        return f"Good morning {name}, you are {age} years old"
    
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug = True)