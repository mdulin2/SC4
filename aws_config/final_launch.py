import boto3 
import os
import json 

# Get raw contents of zip file
def aws_file(ZIPNAME):
    with open(ZIPNAME, 'rb') as file_data:
        bytes_content = file_data.read()
    return bytes_content


## Get creds for account - 284991136387
AccessKeyId = "AKIAUEWWLUKBRHXONOOO"
SecretKey = "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" 

'''
Put IAM policy for user HERE
'''

# Lambda functions client
lambda_client = boto3.client(
    'lambda',
    aws_access_key_id=AccessKeyId, 
    aws_secret_access_key=SecretKey,
    region_name="us-west-2"
)

# Deploy lambda function
response = lambda_client.create_function(
    FunctionName='Flag3',
    Runtime='python3.9',
    Role="arn:aws:iam::284991136387:role/8BallLambdaRole", 
    Handler='flag3.lambda_handler',
    Code=dict(ZipFile=aws_file("./flag3.zip")), 
    Timeout=300, # Maximum allowable timeout
    # Set up Lambda function environment variables
    Environment={
        'Variables': {
            'Name': 'helloWorldLambda',
            'Environment': 'gamma'
        }
    },
)

print(response) 

'''
{'ResponseMetadata': {'RequestId': 'f8d3e04d-763a-4046-b20a-4c022678b878', 'HTTPStatusCode': 201, 'HTTPHeaders': {'date': 'Mon, 21 Nov 2022 22:35:55 GMT', 'content-type': 'application/json', 'content-length': '1050', 'connection': 'keep-alive', 'x-amzn-requestid': 'f8d3e04d-763a-4046-b20a-4c022678b878'}, 'RetryAttempts': 0}, 'FunctionName': 'Magic8BallLambda', 'FunctionArn': 'arn:aws:lambda:us-west-2:284991136387:function:Magic8BallLambda', 'Runtime': 'python3.9', 'Role': 'arn:aws:iam::284991136387:role/8BallLambdaRole', 'Handler': 'api.lambda_handler', 'CodeSize': 555, 'Description': '', 'Timeout': 300, 'MemorySize': 128, 'LastModified': '2022-11-21T22:35:55.112+0000', 'CodeSha256': 'UYyl7KWh8ifUc4vfFDZChBrQ9fBvyYRcNKL5ua9mqw4=', 'Version': '$LATEST', 'Environment': {'Variables': {'Environment': 'gamma', 'Name': 'helloWorldLambda'}}, 'TracingConfig': {'Mode': 'PassThrough'}, 'RevisionId': 'ce4bf5d4-3a51-4b8a-9757-eb25d8c89ad5', 'State': 'Pending', 'StateReason': 'The function is being created.', 'StateReasonCode': 'Creating', 'PackageType': 'Zip', 'Architectures': ['x86_64'], 'EphemeralStorage': {'Size': 512}} 
'''

# Lambda functions client
s3_client = boto3.client(
    's3',
    aws_access_key_id=AccessKeyId,
    aws_secret_access_key=SecretKey,
    region_name="us-west-2"
)

# Create S3 bucket
#s3_client.create_bucket(Bucket='nathan-super-secret-bucket', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})

cmd = 'AWS_ACCESS_KEY_ID="{}" AWS_SECRET_ACCESS_KEY={} aws s3 cp ./flag4.txt s3://nathan-super-secret-bucket/flag.txt'.format(AccessKeyId, SecretKey)
print(cmd) 
os.system(cmd) 



