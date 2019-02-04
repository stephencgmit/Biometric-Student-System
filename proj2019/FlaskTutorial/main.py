from flask import Flask, render_template

app = Flask(__name__)


@app.route("/login/<name>")
def profile(name):
    return render_template("login.html",name=name)


# @app.route("/bacon", methods=['GET', 'POST'])
# def bacon():
#    if request.method == 'GET':
#        return "You are using POST"
#    else:
#        return "You are probably using GET"
# @app.route("/")
# @app.route("/<user>")
# def index(user=None):
#     return render_template("user.hmtl", user=user)

@app.route("/")
@app.route("/<user>")
def index(user=None):
    return render_template("user.html", user=user)


if __name__ == "__main__":

    app.run()
