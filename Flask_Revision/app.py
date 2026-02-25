from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "amandeep"

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
            session["username"] = name
            session["age"] = age
            return redirect(url_for("details"))
    
    return render_template("form.html", error = error)

@app.route("/details")
def details():
    if "username" in session and "age" in session:
        name = session.get("username")
        age = session.get("age")
        return f"Hello {name}, you are {age} years old!"
    

if __name__ == "__main__":
    app.run(debug = True)