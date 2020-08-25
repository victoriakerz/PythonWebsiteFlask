from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=5)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


# @app.route("/second/")
# def second():
#     return render_template("second.html")
#
#
# @app.route("/scheduling/")
# def scheduling():
#     return render_template("scheduling.html")
#
#
# @app.route("/contact/")
# def contact():
#     return render_template("contact.html")


# @app.route("/<name>/")
# def user(name):
#     return f"Hello {name}!"
#
#
# @app.route("/user/")
# def admin():
#     return redirect(url_for("home"))
#
#
# @app.route("/admin2/")
# def admin2():
#     return redirect(url_for("user", name="Admin!"))


if __name__ == "__main__":
    app.run(debug=True)
