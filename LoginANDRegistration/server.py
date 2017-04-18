import re
from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt =Bcrypt(app)
mysql = MySQLConnector(app, "pythonlogin")
app.secret_key="thesecret"

@app.route("/")
def index():
	if "form" not in session:
		session["form"]={}
	return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
	if request.form["action"] == "login":
		email = request.form["email"]
		password = request.form["password"]
		login_query = "SELECT * FROM users WHERE email = :entered_email LIMIT 1"
		login_data = {'entered_email': email}
		user = mysql.query_db(login_query, login_data)
		if len(user) == 0:
			flash("User does not exist", 'login')
		if bcrypt.check_password_hash(user[0]['password'],password):
			return redirect("/success")
		else:
			flash("Password incorrect", 'login')
			return redirect("/")
	elif request.form["action"] == "register":
		first = request.form["first_name"]
		last = request.form["last_name"]
		email = request.form["email_reg"]
		password = request.form["password_reg"]
		cpassword = request.form["conf_password"]
		session["form"] = request.form
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if len(first) < 2 or len(last) < 2:
			flash("Name must be 2 or more characters" 'register')
			return redirect("/")
		elif len(email) < 1 or not EMAIL_REGEX.match(email):
			flash("Must provide a valid email",'register')
			return redirect("/")
		elif len(password) < 8:
			flash("Password must be 8 characters or longer", 'register')
			return redirect("/")
		elif password != cpassword:
			flash("Password and Confirm Password do not match", 'register')
			return redirect("/")
		else:
			session.pop("form")
			session["form"]={}
			pw_hash = bcrypt.generate_password_hash(password)
			# Enter encryption for password
			insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at, login_at) VALUES (:first, :last, :email, :password, NOW(), NOW(), NOW())"
			insert_data = {'first': first, 'last':last, 'email':email, 'password':pw_hash}
			mysql.query_db(insert_query,insert_data)
			#Enter mysql info to add input to database	
			return redirect("/success")
			# direct into logged in page
@app.route("/success")
def logged_in():
	render_template("success.html")

app.run(debug=True)