from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def dashboard():
    user = {
        'name' : 'Alex',
        'logged_in' : True,
        'hobbies' : ['Reading', 'Cycling', 'Gaming']
    }

    number = 430
    return render_template('dashboard.html', user = user, number = number)


@app.route('/loop')
def loop():
    l1 = [1, 2, 3, 4, 5]
    return render_template('loop.html', l1 = l1)

@app.route('/if')
def if_condition():
    number = 430
    return render_template('if.html', number = number)

if __name__ == "__main__":
    app.run(debug=True)

