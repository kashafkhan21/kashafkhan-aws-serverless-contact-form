import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('kashafcontact-messages')  # <-- change this to your exact table name if different

def lambda_handler(event, context):
    try:
        # Parse the request body
        body = json.loads(event['body'])
        name = body['name']
        email = body['email']
        message = body['message']

        # Save data in DynamoDB
        table.put_item(
            Item={
                'id': str(uuid.uuid4()),
                'name': name,
                'email': email,
                'message': message
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Data saved successfully!'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})}