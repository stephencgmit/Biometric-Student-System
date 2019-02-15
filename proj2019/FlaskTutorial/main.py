from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home(user=None):
    return render_template("homepage.html", user=user)


@app.route("/")
@app.route("/login")
def login(user=None):
    return render_template("login.html", user=user)


@app.route("/")
@app.route("/homepage")
def homepage(user=None):
    return render_template("homepage.html", user=user)


@app.route("/")
@app.route("/register")
def index(user=None):
    return render_template("register.html", user=user)


# @app.route("/")
# @app.route("/login")
# def index(user=None):
#     return render_template("login.html", user=user)


if __name__ == "__main__":
    app.run()
