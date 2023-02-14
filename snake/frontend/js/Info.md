## Client Side Badness
- Three bugs right now: 
	- Lack of user check - can submit scores for other users:
		- http://localhost:5000/submit_score?new_score=500&username=admin
	- Can submit ludercious high scores
		- http://localhost:5000/submit_score?new_score=100000000000&username=maxwell
	- XSS on the error message for the logging in with a duplicate user:
		- http://localhost:5000/submit_score?new_score=1&username=%3Cimg%20src%20onerror=alert(1)%3E
- Based on https://github.com/patorjk/JavaScript-Snake