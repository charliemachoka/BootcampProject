from flask import Flask 
from flask import render_template, redirect, url_for
from flask import request
from models import User

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('homepage.html')


@app.route("/login/",methods=["POST","GET"])
def login():
	if request.method == "POST":
		return render_template("login.html")

	return render_template("login.html")

@app.route("/signup/", methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	elif request.method =='POST':
		username = request.form['username']
		email = request.form['email']
		password = request.form['pwd']
		user = User()
		user.username = username
		user.email_address = email
		user.password = password
		return redirect(url_for('optionspage'))

@app.route("/optionspage/")
def optionspage():
	return render_template("optionspage.html")


if __name__ == '__main__':
	app.run(debug=True)