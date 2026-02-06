from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/dashbord')

def dashboard():
    user = {
        'name' : 'Alex',
        'logged_in' : True,
        'hobbies' : ['Reading', 'Cycling', 'Gaming']
    }

    return render_template('dashboard.html', user = user)


@app.route('/loop')
def loop():
    l1 = [1, 2, 3, 4, 5]
    return render_template('loop.html', l1 = l1)

@app.route('/if')
def if_condition():
    number = 430    
    return render_template('if.html', number = number)

@app.route('/student')
def student():
    students = ['Alex', 'Bob', 'Charlie']
    return render_template('students.html', students=students)

@app.route('/marks')
def marks():
    score = 50
    return render_template('marks.html', score=score)

@app.route('/products')
def products():
    products = [
        {'name': 'Laptop', 'price': 50000},
        {'name': 'Phone', 'price': 20000},
        {'name': 'Tablet', 'price': 30000}
    ]
    return render_template('products.html', products=products)

@app.route('/filters')
def filters():
    name = "amandeep"
    skills = ['Python', 'Flask', 'SQL']
    return render_template('filters.html', name=name, skills=skills)


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# ---------- REGISTER PAGE ----------
@app.route('/', methods=['GET', 'POST'])
def register():
    error = None

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        # Email validation
        if '@' not in email:
            error = "Invalid email address. '@' is required."

        else:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (name, email)
            )
            conn.commit()
            conn.close()

            return redirect(url_for('students'))

    return render_template('register.html', error=error)


# ---------- STUDENTS PAGE ----------
@app.route('/students')
def students():
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM users").fetchall()
    conn.close()

    return render_template('students.html', students=students)


if __name__ == "__main__":
    app.run(debug=True)