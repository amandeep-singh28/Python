from flask import Flask, redirect , url_for, session, Response, request

app = Flask(__name__) # This intializes our application
app.secret_key = 'supersecretkey'

@app.route('/', methods = ['POST', 'GET'])

def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'amandeep' and password == '123':
            session['user'] = username
            return redirect(url_for('welcome'))
        else:
            return Response('Invalid credentials ', 401)
        
    return '''
        <h2> Login page </h2>
        <form method = "post">
            Username: <input type = "text" name = "username"><br>
            Password: <input type = "password" name = "password"><br>
            <input type = "submit" value = "Login">
        </form>
    '''

@app.route('/welcome')
def welcome():
    if 'user' in session:
        return f'''
        <h2>Wekcone, {session["user"]}!</h2>
        <a href = {url_for('logout')}>Logout</a>
        '''
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))