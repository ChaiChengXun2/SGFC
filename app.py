from flask import Flask, render_template 

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/infographics")
def infographics():
    return render_template("infographics.html")

@app.route("/meetus")
def meetus():
    return render_template("meetus.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")

