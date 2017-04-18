from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
	return render_template("templates.html", phrase="Hello", times=5)
app.run(debug=True)