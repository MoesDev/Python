from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "blah"

# Monet Harkin

@app.route('/')
def index():
	if "count" not in session:
		session['count'] = 0
	session['count'] += 1
	return render_template('index.html')

@app.route('/ninja', methods=["POST"])
def ninja():
	session['count'] += 1
	return redirect ('/')

@app.route('/hacker')
def hacker():
	session['count'] = 0
	return redirect ('/')




app.run(debug=True)