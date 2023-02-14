## Challenge 

There's a secret passcode that is 8 digits long, making it impossible to completely brute force.   
Is there a way we can leak some information about the passcode through the program? Side Channels! :) 

How to use: 
- Compile the client file with ``gcc client.c -o client``.
- The passcode is the flag for this challenge. 
- ./client IP PORT PASSCODE
	- i.e: ``./client 127.0.0.1 8080 987654321``

- Hint: https://linux.die.net/man/2/time
- Hint: The passcode has 8 characters 
- Hint: Can you spot the difference between the passcodes 987654321 and 19999999?

Given: client.c 
Given server.c with the passcode removed. 
