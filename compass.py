from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'I4q9MhK3PDhfdi5j7KP2qaqfawzTtRWH'

# Flask-Bootstrap requires this line
Bootstrap(app)

#test list to test form GET and POST
CARS = ['911','914','944']

# I should move this to a modules.py, which can store all the functions I'll need for the compass app
def get_car(source):
	the_car = []
	for row in source:
		carz = row
		the_car.append(carz)
	return the_car

class NameForm(FlaskForm):
	name = StringField('Which car is your favorite?', validators=[DataRequired()])
	submit = SubmitField('Submit')

@app.route("/")
def index():
	greetings = "Hello World"
	return render_template("home.html", greetings=greetings)

@app.route('/form_1')
def foobar():
	return '<h1>Hi there, User!</h1>'

@app.route('/form_2', methods=['GET', 'POST'])
def form_function():
	car = get_car(CARS)
	form = NameForm()
	message = ""
	if form.validate_on_submit():
		name = form.name.data
		if name in names:
			form.name.data = ""
			return name
		else:
			message = "That car is not in our database."
	return render_template('index.html', names=the_car, form=form, message=message) # the_car is not being properly assigned. Next steps should be to test that function.

if __name__ == "__main__":
	app.run(debug=True, host='127.0.0.1', port=5000)
	app.directory='./'
