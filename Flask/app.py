from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(200), nullable = True)
    password = db.Column(db.String(200), nullable = True)

with app.app_context():
    db.create_all()

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        new_user = User(username = username, password = password)
        db.session.add(new_user)
        db.session.commit()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)