from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
	dojos = ["Dallas","San Jose","Chicago"]
	languages = ["Java","C#","Python"]
	return render_template("index.html", dojos=dojos, favs=languages)

@app.route('/results', methods=["POST"])
def form_submit():
	details1 = request.form["name"]
	details2 = request.form["local"]
	details3 = request.form["lang"]
	details4 = request.form["comment"]
	return render_template("results.html", name=details1, local=details2, lang=details3, com=details4)

app.run(debug=True)