from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///details.db'
db = SQLAlchemy(app)

class Student(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(200), nullable = True)
    age = db.Column(db.Integer, nullable = True)

with app.app_context():
    db.create_all()

@app.route("/", methods = ["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        name = request.form.get("username")
        age = request.form.get("age")
        
        if not name:
            error = "Name is required"
        elif not age:
            age = "Age is required"
        else:
            student = Student(username = name, age = int(age))
            db.session.add(student)
            db.session.commit()
            return redirect(url_for("students"))
        
    return render_template("form.html", error = error)

@app.route("/students")
def students():
    student = Student.query.all()
    return render_template("student.html", student = student)