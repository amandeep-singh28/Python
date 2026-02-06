from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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


students_data = []

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        course = request.form.get('course')

        # 🔴 Email validation
        if '@' not in email:
            error = "Invalid email address. '@' is required."

        else:
            student = {
                'name': name,
                'email': email,
                'course': course
            }

            students_data.append(student)
            return redirect(url_for('students'))

    return render_template('register.html')


@app.route('/students')
def students():
    return render_template('students.html', students=students_data)




if __name__ == "__main__":
    app.run(debug=True)

