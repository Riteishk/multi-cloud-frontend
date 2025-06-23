def lambda_handler(event, context):
    name = event.get('queryStringParameters', {}).get('name', 'Guest')
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': f'Hello {name}, from AWS Lambda!'
    }
