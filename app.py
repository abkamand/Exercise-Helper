from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("home.html")

# "Page 2 Routes"
@app.route("/arms")
def arms():
    return render_template("arms.html")

@app.route("/back")
def back():
    return render_template("back.html")

@app.route("/core")
def core():
    return render_template("core.html")

@app.route("/legs")
def legs():
    return render_template("legs.html")

@app.route("/chest")
def chest():
    return render_template("chest.html")

# "Page 3 Novice Routes"
@app.route("/novarms1")
def novarms1():
    return render_template("novarms1.html")

@app.route("/novback1")
def novback1():
    return render_template("novback1.html")

@app.route("/novcore1")
def novcore1():
    return render_template("novcore1.html")

@app.route("/novlegs1")
def novlegs1():
    return render_template("novlegs1.html")

@app.route("/novchest1")
def novchest1():
    return render_template("novchest1.html")

# "Page 3 Proficient Routes"
@app.route("/profarms1")
def profarms1():
    return render_template("profarms1.html")

@app.route("/profback1")
def profback1():
    return render_template("profback1.html")

@app.route("/profcore1")
def profcore1():
    return render_template("profcore1.html")

@app.route("/proflegs1")
def proflegs1():
    return render_template("proflegs1.html")

@app.route("/profchest1")
def profchest1():
    return render_template("profchest1.html")

# "Page 3 Expert Routes"
@app.route("/exparms1")
def exparms1():
    return render_template("exparms1.html")

@app.route("/expback1")
def expback1():
    return render_template("expback1.html")

@app.route("/expcore1")
def expore1():
    return render_template("expcore1.html")

@app.route("/explegs1")
def explegs1():
    return render_template("explegs1.html")

@app.route("/expchest1")
def expchest1():
    return render_template("expchest1.html")


if __name__ == "__main__":
    app.run(debug=True)