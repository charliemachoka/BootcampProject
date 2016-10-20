from flask import Flask,render_template
from flask import url_for 
from flask import request,redirect

app = Flask(__name__)


@app.route('/')
def  main():
	return render_template('homepage.html')

@app.route("/login/",methods=['POST','GET'])
def login():
	#CHECK whether the valid credentials have been supplied 
	return render_template("login.html",form=request.form)
	

if __name__ == '__main__':
	app.run(debug=True)



