# Spokane Cyber Cup IV
- These are the CTF challenges from the Spokane Cyber Cup in 2022. 
- There are four types: 
	- Web: Connect via localhost. 
	- SSH: SSH into the machine to solve the challenge.
	- Custom client: Run a client to interact with the challenge.
	- Stand alone: A file, prompt or something that is static for interactions.
- For everything but the standalone challenges do the following: 
	- Go into the directory
	- ``./docker_run.sh`` - this will build, start and go into the container. 
	- Do setup steps defined in ``Challenge.md`` for a given folder.
- SolutionGuideYear4.docx:
	- Contains the coaches solution guide from the CTF
- Have fun! :)

# Challenges
## Web 
- **Facial recognition bypass**: 
	- Use picture to bypass the facial recognition. 
	- https://github.com/RajarsiGit/Login-System-using-Face-Recognition
- **SQL Injection** (nicholos_cage):
	- Login page SQL injection
- **cats1**:
	- Insecure file upload for code execution via PHP
- **cats2**:
	- Local file inclusion to retrieve flag
- **cats3**:
	- Directory traversal to retrieve flag
- **snake**:
	- Lack of client side validation on scores. 
	- Improper authentication setup
	- https://github.com/patorjk/JavaScript-Snake
- **GPTech Support** (gptech-support):
	- Prompt injection on a web app with GPT-3 backend.
- View source:
	- Not in repo
	- Just a comment in the HTML of the scoreboard

## Binary 
- Basic memory corruption series: 
	- Corrupting a variable
	- Controlling the variable
	- Hijacking the control flow
- **fault_in_our_codes**:
	- Fault injection challenge on a binary
	
## Linux 
- Linux usage basics:
	- First SSH
	- First grep
- **sudo privilege escalation** (3):
	- Firsty
	- Lesser
	- vim pops a shell
- **Timing Based side channel** (time_me_up): 
	- Use the side channel of `time` in order to figure out the passcode. 

## Reverse Engineering 
- **Game Hacking** (pokemon_game): 
	- Finding the configuration file
	- Editing money
	- Editing pokemon 
	- Editing map location (extra) - unused
	- Unintended code execution

## Blue Team 
- **Wireshark packet analysis** (pcap)
	- Extracting the password
	- Extracting files from packet capture
- **Log Analysis** (log-analysis-apache)
	- Grepping Apache server access logs

## Cryptography
- Cesar Cipher
- learning_rsa:
	- loops1 
	- loops2
	- loops3


## Other Categories
- **Cloud Configuration (IAM, S3, EC2, lambda)**:
	- Wide open S3 bucket on website
	- Key in source code
	- View other S3 bucket via CLI
	- Invorke lambda function via CLI (extra) - unused
- **osint_hackerman_finding (6)**:
- **Braille**
- Hack the planet: 
	- Just know the term!


# Challenge Authors
- Ken Price: 
	- Ticket Swipey
	- gpetch-support
	- pcap 
	- log-analysis-apache
- Fabian Vilela:
	- Privilege escalation challenges
- Juan Ford: 
	- OSINT challenges
- Max Arnold: 
	- learning rsa
- All others: 
	- Maxwell Dulin