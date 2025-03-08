from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/signup")
def signup():
        return render_template('signup.html')

app.run(host='127.0.0.1', port=5000, debug=True)
