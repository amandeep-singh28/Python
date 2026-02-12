#CODE 1
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

@app.route("/update", methods = ["POST", "GET"])
def update():
    if request.method == "POST":
        sno = request.form.get("sno")
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(sno = sno).first()
        if user:
            user.username = username
            user.password = password
            db.session.add(user)
            db.session.commit()
    return render_template("update.html")

@app.route("/delete", methods = ["POST", "GET"])
def delete():
    if request.method == "POST":
        sno = request.form.get("sno")
        user = User.query.filter_by(sno = sno).first()
        if user:
            db.session.delete(user)
            db.session.commit()
    return render_template("delete.html")


if __name__ == "__main__":
    app.run(debug = True)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Added Functionality of HASHED PASSWORD
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



app = Flask(__name__)
bcrypt = Bcrypt(app)

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
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username = username, password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
    return render_template('index.html')

@app.route("/update", methods = ["POST", "GET"])
def update():
    if request.method == "POST":
        sno = request.form.get("sno")
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(sno = sno).first()
        if user:
            user.username = username
            user.password = password
            db.session.add(user)
            db.session.commit()
    return render_template("update.html")

@app.route("/delete", methods = ["POST", "GET"])
def delete():
    if request.method == "POST":
        sno = request.form.get("sno")
        user = User.query.filter_by(sno = sno).first()
        if user:
            db.session.delete(user)
            db.session.commit()
    return render_template("delete.html")


if __name__ == "__main__":
    app.run(debug = True)


######
from flask import Flask, render_template, redirect, session, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # ✅ FIX

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    if 'user' in session:
        return f"Welcome {session['user']}!"
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['user'] = user.username  # ✅ FIX
            return redirect('/')

        flash("Invalid credentials")

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash("User already exists")
            return redirect('/register')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(
            username=username,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)


########
from flask import Flask, render_template, redirect, session, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy

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


# -------------------- LOGOUT (optional) --------------------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
