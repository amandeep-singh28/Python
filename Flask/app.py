from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def feedback():
    error = None

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            error = "All fields are required"
        elif '@' not in email:
            error = "Invalid email address"
        else:
            print(name, email, message)
            print("Hello")
            return render_template('thankyou.html', name = name)

    return render_template('feedback.html', error = error)

