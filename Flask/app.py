from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def dashboard():
    user = {
        'name' : 'Alex',
        'logged_in' : True,
        'hobbies' : ['Reading', 'Cycling', 'Gaming']
    }
    return render_template('dashboard.html', user = user)



