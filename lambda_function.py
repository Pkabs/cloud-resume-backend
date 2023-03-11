import boto3
import os
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor_stats')

#Get count funtion that gets and returns the latest value
def get_count():
    response = table.get_item(Key={'record_id':'resumesite'})
    count = response['Item']['visitor_count']
    print(count)
    return count

#Increment the fetched value & update table
def lambda_handler(event, context):
    new_visitor_count = get_count() + 1
    updateItem = table.put_item(Item={
        'record_id':'resumesite',
        'visitor_count': new_visitor_count,    
    })
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': get_count()
    }
    return response
    

""" 
#returns the latest value
def get_count():
    latestvalue = table.get_item(Key={'record_id':'0'})
    count = latestvalue['Item']['visitor_count']
    print(count)
    return count
""" 
#BACKUPS
"""
#Increment the fetched value & update table
def lambda_handler(event, context):
    new_visitor_count = get_count() + 1
    updateItem = table.put_item(Item={
        'record_id':'resumesite',
        'visitor_count': new_visitor_count,    
    })
    return new_visitor_count


# Headers for API calls
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Credentials': 'true',
            'Content-Type': 'application/json'
        },
        'body': get_count()
    }
"""     