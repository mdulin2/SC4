import random

def lambda_handler(event, context): 
    # Lambda handler function.
    return {
        'statusCode': 200,
        'body': {"body" : get_response()}
    }

def get_response():
    # Get response from the 8 ball.
    responses = [
        'It is certain.', 
        'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'My reply is no.',
        'My resources say no.',
        'Outlook not so good.',
        'Very doubtful.'
    ]
    return random.choice(responses)
