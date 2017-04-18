import random

from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key="secretNumber"

@app.route('/')
def index():
	if 'somekey' not in session:
		session['somekey']=random.randrange(0,101)
	if 'answer' not in session:
		session['answer']=""
	ans=session['answer']
	return render_template('index.html',ans=ans)

@app.route('/guess', methods=["POST"])
def guess():
	guess = int(request.form["number"])
	if guess==session['somekey']:
		session['answer']= str(guess) +" was the number"
		return render_template('won.html', ans=session['answer'])
	elif guess > session['somekey']:
		session['answer']= "Too High!"
		return redirect('/')
	elif guess < session['somekey']:
		session['answer']= "Too Low!"
		return redirect('/')
@app.route('/won')
def won():
	session['answer']=""
	session.pop('somekey')
	session['somekey']=random.randrange(0,101)
	return redirect('/')
app.run(debug=True)