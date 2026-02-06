from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

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

@app.route('/students')
def students():
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


if __name__ == "__main__":
    app.run(debug=True)

