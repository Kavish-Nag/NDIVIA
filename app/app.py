from flask import Flask, render_template, request, redirect, url_for, flash
import subprocess

app = Flask(__name__)
app.secret_key = "123-34"  # Required if using flash messages

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        result = subprocess.run(["python", "backend/register.py", username, password], capture_output=True, text=True)

        if "Success" in result.stdout:
            return "Login Successful!"
        else:
            flash("Invalid username or password", "error")  # Show an error message
            return redirect(url_for("login"))  # Redirect back to login page
    
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

