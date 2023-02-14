# Aws Config
- Configurations are the most common security vulnerability. Can you find them all? Visit the URL 'http://spokane-ctf-iv-magic8ball.s3.us-west-2.amazonaws.com/website/index.html' to begin. 
- Hint: What is S3? 
- Hint: What are bucket permissions? 
- Hint: The S3 bucket name is spokane-ctf-iv-magic8ball
- Source code comes from here: 
	- https://github.com/vannguyen48/Magic-8-bit-Ball
	
## Challenge 1 
- List out the contents of the S3 bucket to find the game. 
- Hint: Use the aws S3 CLI or visit the S3 bucket at the URL

## Challenge 2 
- Can you find any hidden credentials in the files? Provide the access key as the flag.
- Hint: Use the aws S3 CLI or visit the S3 bucket at the URL 

## Challenge 3
- Can you execute any hidden lambda functions? 
- Hint: You MUST use the AWS cli for this one. 

## Challenge 4
- Are there any other S3 buckets you can escalate your privileges to view? 


# Setup 
- Setup your own AWS account. 
- Create an IAM user with all S3 and lambda permissions attached
- Set the access key information into 'final_launch.py' for the variables ``AccessKeyId`` and ``SecretKey``.
- Run the script ``final_launch.py`` to setup the bad S3 bucket and the bad lambda function. 
- Create an S3 bucket. 
- Add the code inside of ``Magic-8-bit-Ball`` into the bucket. 
- Set the bucket to be a website, be readable and listable.