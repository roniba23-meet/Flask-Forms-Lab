from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app

	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY'] = 'super-secret-key'


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Judeh", "George", "Fouad", "Celina"]


@app.route('/', methods = ['GET', 'POST'])
def login():
	if request.method=='GET':
		return render_template('login.html')	
	else:
		if password == request.form['password'] and username==request.form['username']:
			return redirect(url_for('home'))

	  	


@app.route('/home', methods =['GET', 'POST'])
def home():
	if request.method=='GET':
		return render_template('home.html',list_f= facebook_friends)

	else:
		return render_template('home.html', list_f= facebook_friends)
	
@app.route('/friend_exists.html/<string:name>', methods=['GET', 'POST'])
def friend_exists(name):
		if request.method=='GET':
			if (name in facebook_friends):
				return render_template('friend_exists.html', name=name, facebook_friends=facebook_friends, bool="true")
			else:
				return render_template('friend_exists.html', name=name, facebook_friends=facebook_friends, bool="false")




if __name__ == "__main__":  # Makes sure this is the main process
	app.run(debug=True) # Starts the site
    
	