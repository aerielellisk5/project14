import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('New_Movies')


# 1) Query the DB

from boto3.dynamodb.conditions import Key
response = table.query(
    KeyConditionExpression=Key('year').eq(2011)
)

# print(json.dumps(response, indent=2, default=str))

# 2) Remove a table
dynamodb_client = boto3.client('dynamodb')

# deleted_table = dynamodb_client.delete_table(
#     TableName='try_again'
# )

# print(json.dumps(deleted_table, indent=2, default=str))


# 3) Remove an item from the table
# In this case I needed to use the parition and sort key here.

delete_table = table.delete_item(
    Key={
        "year" : 2017,
        "title": "MovieH"
        }
    )
print(json.dumps(delete_table, indent=2, default=str))