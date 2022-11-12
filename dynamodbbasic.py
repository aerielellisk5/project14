# All code should be inline commented.

# Create a DynamoDB table for something of your choosing (e.g. movies, food, games).
# Using the Gist (https://gist.github.com/zaireali649/0ec6b90155120cf508223788b7b86efc) as a starting point, use boto3 and Python to add 10 or more items to the table.
# Use boto3 and Python to scan the DynamoDB table.
import boto3
import json

dynamodb = boto3.resource('dynamodb',
region_name='us-east-1')

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


# table = dynamodb.create_table(
#     TableName='again',
#     KeySchema=[
#         {
#             'AttributeName': 'year',
#             'KeyType': 'HASH'  #Partition key
#         },
#         {
#             'AttributeName': 'title',
#             'KeyType': 'RANGE'  #Sort key
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'year',
#             'AttributeType': 'N'
#         },
#         {
#             'AttributeName': 'title',
#             'AttributeType': 'S'
#         },

#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )

# print(table.item_count)

# print(json.dumps(response, indent=2, default=str))





# lets add some data to the dynamodb with the put_item method
table = dynamodb.Table('New_Movies')

dateandtime = table.creation_date_time
# print(json.dumps(dateandtime, indent=2, default=str))

table.put_item(
     Item={
        'year': 2018,
        'title': 'BlackPanther',
    }
)


# now lets return (or get) the Item

response = table.get_item(
    Key={
        'year': 2018,
        'title': 'BlackPanther',
    }
)

item = response['Item']
# print(json.dumps(response, indent=2, default=str))

# Let's add 10 items to the table

# with table.batch_writer() as batch:
#     batch.put_item(
#         Item={
#             'year':2010,
#             'title': "MovieA",
#         }
#     )
#     batch.put_item(
#         Item={
#             'year': 2011,
#             'title': "MovieB",
#         }
#     )
#     batch.put_item(
#         Item={
#             'year': 2012,
#             'title': "MovieC",
#         }
#     )
#     batch.put_item(
#         Item={
#             'year': 2013,
#             'title': "MovieD",
#         }
#     )
#     batch.put_item(
#         Item={
#             'year': 2014,
#             'title': "MovieE",
#         }
#     )
#     batch.put_item(
#         Item={
#             'year': 2015, 
#             'title': "MovieF",
#         }
#     )
#     batch.put_item(
#         Item={
#             'year': 2016,
#             'title': "MovieG",
#         }
#     )
#     batch.put_item(
#         Item={
#             'year': 2017,
#             'title': "MovieH",
#         }
#     )
#     batch.put_item(
#         Item={
#             'year': 2018,
#             'title': "MovieI",
#         }
#     )
#     batch.put_item(
#         Item={
#             'year': 2019,
#             'title': "MovieJ"
#         }
#     )

# Time to scan the table - filter with year?

response = table.scan(
    ProjectionExpression="title"
)

print(json.dumps(response, indent=2, default=str))

item = response['Items']

print(json.dumps(item, indent=2, default=str))