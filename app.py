from flask import Flask, render_template, request, flash

app=Flask(__name__)
app.secret_key="fhddgs"

@app.route("/hello")
def index():
	flash("What is your name?")
	return render_template("index.html")

@app.route("/re", methods=["POST","GET"])
def re():
	flash("Hi " + str(request.form["name"] + ",Good Day"))
	return render_template("index.html")