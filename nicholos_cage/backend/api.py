"""
Maxwell Dulin 
Super Secure login 
filename: api.py
"""

from flask import Flask, jsonify
from abstract_database_connection import AbstractDatabaseConnection
from flask_cors import CORS
from flask import request
import database
import sqlite3
import secrets

login = Flask(__name__)
CORS(login)


@login.route('/auth', methods=['GET'])
def session():
	"""
	Checks for a valid session. 
	If the session is valid, a flag is returned. 
	Otherwise, return a 404. 
	
	Parameters: None 
	Expects a session token set as a cookie. 
	"""
	with AbstractDatabaseConnection('login.db') as conn:
		cursor = conn.cursor()
		session = request.cookies.get('session') 
		if(session == None):
			return build_result([],403) 
			
		# Checks to see if this is a valid session
		cursor.execute("""
		SELECT * 
		FROM session as s
		WHERE s.session = '%s'
		""" % (session))	

		# If the session is valid, then keep going. 
		# Otherwise, exit. 
		if(len(cursor.fetchall()) == 0):
			return build_result("False :(", 400)
			
		return build_result(get_flag(),200) 
		

@login.route('/login', methods=['POST'])
def login_call():
	"""
	Does the login process
	If valid login, a cookie is set for the session 
	Otherwise,
	
	Parameters: Username, Password 
	Returns:
		Response message with HTTP code.
	"""
	with AbstractDatabaseConnection('login.db') as conn:
		cursor = conn.cursor()
		
		username = request.args.get('username')
		password = request.args.get('password')
		
		# Check for the login in a secure way :) 
		# This is where the vulnerability is at. 
		query = """
		SELECT * FROM login WHERE username = '%s' AND password = '%s'; 
		""" % (username, password)
		

		# Catches all errors and prints the query out. 
		try: 
			cursor.execute(query)
		except Exception as e: 

			error_message = "<p>Query: " + query + "</p>"
			error_message += "<p>Error from SQL: " + str(e) + "</p>"
			return build_result(error_message,400),400
			
		# Handles the authorization; correct versus incorrect.
		result = cursor.fetchall()
		if(len(result) == 0 ):
			return build_result("<p>Query: " + query + "</p>",403),403
		else: 
		
			# Get a safe and secure token for the session
			session = secrets.token_urlsafe(120)

			# Set the session
			cursor.execute("""
			INSERT INTO session(session)
			VALUES ('%s')
			""" % session)	
			conn.commit()
	
			return build_result(get_flag(),200),200

def list_result(result_set):
	"""
	Turn a result set into comma delimited list.

	Args:
		result_set: database result set.
	Returns:
		A comma delimited list of results.
	"""
	result = ', '.join([r[0] for r in result_set])
	return result

def build_result(content, http_status):
	"""
	Build API response.

	Args:
		content: message content.
		http_status: HTTP status code.
	Returns:
		API response with message and HTTP code.
	"""
	success = True if (http_status == 200) else False
	if (success):
		return jsonify({
			"success": 'true',
			"response": content,
			"code": http_status
		})
	else:
		return jsonify({
			"success": 'false',
			"error": {
				"code": http_status,
				"message": "Error: {}".format(content)
			}
		})

# Get the flag
def get_flag(): 
	with open('../flag.txt') as f:
		contents = f.read()
		return contents	

if __name__ == '__main__':
	# TODO: Turn off debugging on production.
	login.run(debug=True, port=8081, host="0.0.0.0") 
