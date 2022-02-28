import json
 
def lambda_handler(event, context):
    # TODO implement
    keyword = event['queryStringParameters']['keyword']
    return {
        'statusCode': 200,
        'body': 'Abhiram Reddy say ' + keyword
    }
