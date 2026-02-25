from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
    error = None
    
    if request.method == "POST":
        name = request.form.get("username")
        age = request.form.get("age")
        
        # Validation
        if not name:
            error = "Name is required"
        elif not age:
            error = "Age is required"
        else:
            return f"Hello {name}, you are {age} years old"
    
    return render_template("form.html", error = error)

if __name__ == "__main__":
    app.run(debug = True)