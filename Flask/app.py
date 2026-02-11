from flask import Flask, render_template, redirect, session, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import base64

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)

# -------------------- MODEL --------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    image = db.Column(db.LargeBinary, nullable=True)

with app.app_context():
    db.create_all()


# -------------------- HOME --------------------
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['email']
        image_file = request.files.get("image")  # ✅ Correct way

        if User.query.filter_by(username=username).first():
            flash("User already exists")
            return redirect('/')

        image_data = image_file.read() if image_file else None

        new_user = User(
            username=username,
            image=image_data
        )

        db.session.add(new_user)
        db.session.commit()

        flash("User registered successfully")
        return redirect('/')

    return render_template("index.html")

@app.route('/database')
def database():
    users = User.query.all()

    for user in users:
        if user.image:
            user.image = base64.b64encode(user.image).decode('utf-8')
        else:
            user.image = None

    return render_template("database.html", users=users)



# -------------------- LOGOUT (optional) --------------------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
