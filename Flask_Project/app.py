from flask import Flask, render_template, redirect, session, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# -------------------------
# Models
# -------------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref='blogs')


with app.app_context():
    db.create_all()

# -------------------------
# Routes
# -------------------------

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash("User already exists")
            return redirect(url_for('register'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))

        flash("Invalid credentials")

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    blogs = Blog.query.all()
    return render_template('dashboard.html', blogs=blogs)


@app.route('/create', methods=['GET', 'POST'])
def create_blog():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        new_blog = Blog(
            title=title,
            content=content,
            user_id=session['user_id']
        )

        db.session.add(new_blog)
        db.session.commit()

        return redirect(url_for('dashboard'))

    return render_template('create.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_blog(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    blog = Blog.query.get_or_404(id)

    if blog.user_id != session['user_id']:
        return "Unauthorized", 403

    if request.method == 'POST':
        blog.title = request.form['title']
        blog.content = request.form['content']
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('edit.html', blog=blog)


@app.route('/delete/<int:id>')
def delete_blog(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    blog = Blog.query.get_or_404(id)

    if blog.user_id != session['user_id']:
        return "Unauthorized", 403

    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
