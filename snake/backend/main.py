from flask import Flask, render_template, request, url_for, redirect, Blueprint, send_from_directory
import os 
from flask_cors import CORS

main = Blueprint('main', __name__)
secret_key = str(os.urandom(24))

app = Flask(__name__)
CORS(app) # Allow any site to get the data
app.config['TESTING'] = False
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'deployment'
app.config['SECRET_KEY'] = secret_key

# Global variable for scores
scores = []
users = ['admin'] 

# Add score in descending order
def add_score(new_score, user): 
	index = 0 

	while(index < len(scores)):
		if(scores[index]['score'] < new_score):
			break 
		index += 1

	scores.insert(index, {"name" : user, "score" : new_score})

# 'new_score' parameter
@app.route('/submit_score', methods=['GET'])
def submit_score():
	if('new_score' not in request.args or 'username' not in request.args): 
		return "Invalid Parameters" 

	new_score = request.args['new_score']
	new_user = request.args['username']

	if(new_score.isnumeric() == False): 
		return "Invalid Number" 

	add_score(int(new_score), new_user)

	if(int(new_score) > 10000):
		return get_flag(1) 

	# Flag #2 - IDOR like bug
	if(new_user == "admin"): 
		return get_flag(2) 

	return "Score Added" 

@app.route('/get_leaderboard', methods=['GET'])
def get_score():
	return scores 


@app.route('/add_user', methods=['GET'])
def add_user(): 
	if('username' not in request.args): 
		return "Invalid Parameters" 

	new_user = request.args['username']

	if(new_user == 'admin' or new_user in users):
		return "Invalid User" 

	users.append(new_user) 
	return "User Added"

# Get the flag :) 
def get_flag(no): 
	with open('flag' + str(no) + '.txt') as f:
		contents = f.read()
		return contents	


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')