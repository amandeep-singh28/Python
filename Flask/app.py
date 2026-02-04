from flask import Flask

app = Flask(__name__) # This intializes our application

@app.route('/amandeep')
def home():
    return "Welcome to the Flask app!"