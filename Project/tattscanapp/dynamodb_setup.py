# Creates the table for the DynamoDB. Only the identifying factors (id, email - both unique) are needed during creation
# @Ref: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.01.html

import boto3


def create_user_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName = "Users",
        KeySchema = [
            { 
                'AttributeName': 'id',
                'KeyType': 'HASH' },
            { 
                'AttributeName': 'email',
                'KeyType': 'RANGE' }
        ],
        AttributeDefinitions= [
            { 'AttributeName': 'id', 'AttributeType': 'N' }, # N is number
            { 'AttributeName': 'email', 'AttributeType': 'S' } # S is String
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    movie_table = create_user_table()
    print("Table status:", movie_table.table_status)