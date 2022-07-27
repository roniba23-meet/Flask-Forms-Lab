from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app

	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY'] = 'super-secret-key'


accounts= {"roni":"123", "lia":"345", "tal":"565"}
facebook_friends=["Loai","Yonathan","Judeh", "George", "Fouad", "Celina"]


@app.route('/', methods = ['GET', 'POST'])
def login():
	flag= "false"
	if request.method=='GET':
		return render_template('login.html')	

	for i in accounts:
		print(i)
		if accounts[i]== request.form['password'] and i==request.form['username'] and flag=="false":
			flag="true"

	if (flag=="true"):
		return redirect(url_for('home'))
		
	else:
		return render_template('login.html')
		


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
    
	