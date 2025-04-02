import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Messages')

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        body = json.loads(event['body'])
        first_name = body.get('first_name')
        email = body.get('email')
        message = body.get('message')

        # Generate a unique ID for the message
        message_id = str(uuid.uuid4())

        # Store the message in DynamoDB
        table.put_item(
            Item={
                'id': message_id,
                'first_name': first_name,
                'email': email,
                'message': message
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Your message has been well received'})
        }

    return {
        'statusCode': 400,
        'body': json.dumps({'error': 'Invalid request'})
    }
