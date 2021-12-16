import boto3

dynamodb_client = boto3.client('dynamodb')
dynamodb_resource = boto3.resource('dynamodb')
table = dynamodb_resource.Table("Users")

def get_items(): ## ITEMS: Get all items
    return dynamodb_client.scan(
        TableName='Users'
    )
    
def get_item(email): ## ITEM: Get ONE specific result
    response = table.get_item(
        Key={
            'email': email
        }
    )    
    item = response['item']
    
    return item
    
def new_item(first_name, last_name, email, password):
    table.put_item(
        Item={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password
        }
    )

def update_item(email, val, type):
    table.update_item(
        Key={
            'email':email
        },
        UpdateExpression='SET ' + type + ' = :val1',
        ExpressionAttributeValues={
        ':val1': val
        }
    )
    
def delete_item(email):
    table.delete_item(
        Key={
            'email': email
        }
    )
