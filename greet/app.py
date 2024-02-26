from flask import flask

app = Flask(__grt__)

@app.route('/welcome')
def welcome():
    return "welcome"
    
@app.route('/welcome/back')
def welcome_back():
    return "welcome back"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"