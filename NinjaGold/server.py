import random
from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
		if not 'gold' in session:
				session['gold'] = 0
		if not 'activities' in session:
				session['activities'] = []
		session['buildings'] = {
				'farm':random.randint(5,10),
				'casino':random.randint(-50,50),
				'cave':random.randint(0,30),
				'house':random.randint(0,5)
		}
		print session["buildings"]['farm']
		return render_template('index.html', buildings=session['buildings'])

@app.route('/process_money', methods = ['POST'])
def process():
		site = request.form['place']
		if site == 'farm':
			
		
		return redirect('/')

@app.route('/answer', methods = ['POST'])
def answer():
		if request.form['place']=='farm':
				run = session[activities].root
				while run != null:
						run = run.next
				session['activities'].val="farm"
				session['gold']+= session['buildings'].farm.val




if __name__ == '__main__':
	app.run(debug = True)


"""
Will this work?
"""
