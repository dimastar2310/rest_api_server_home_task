import json
import logging

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamodbTableName = 'customers_ids'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTableName)
""""defining methods"""
getMedthod = 'GET'
putMethod = 'PUT'

""""defining paths"""
healthPath = '/health'
productPath = '/product'


def lambda_handler(event, context):
    logger.info(event)  # we can see it in logger watcher
    httpMethod = event['httpMethod']
    path = event['path']
    if httpMethod == getMedthod and path == healthPath:
        response = buildRespons(200)
    elif httpMethod == getMedthod and path == productPath:
        response = getProduct(event['queryStringParameters']['_id'])

    elif httpMethod == putMethod and path == productPath:
        response = saveProdcut(json.loads(event['body']))  # event['body'] is string turning to python dict

    else:
        response = buildRespons(404, 'Not Found')
    return response


def getProduct(_id):
    try:
        response = table.get_item(
            Key={
                '_id': _id

            }
        )
        if 'Item' in response:  # means not null
            return buildRespons(200, response['Item'])  # we passing string
        else:
            return buildRespons(404, {'Message': '_id: %s not found' % _id})
    except:
        logger.exception('maby connection failed!')


def saveProdcut(requestBody):  # we sending dict here
    try:
        table.put_item(Item=requestBody)
        body = {
            'Operation': 'Put',
            'Message': 'SUCCES',
            'Item': requestBody
        }
        return buildRespons(200, body)
    except:
        logger.exception('maby server is down')


# body can be string or dict
def buildRespons(statusCode, body=None):  # we might build response from Postman
    # allowing frontent crossRegion Integration with acces-Controll
    response = {
        'statusCode': statusCode,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origini': '*'
        }
    }

    if body is not None:
        response['body'] = json.dumps(body)  # taking dict turning to string
    return response
