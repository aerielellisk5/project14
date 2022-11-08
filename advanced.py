
# ADVANCED
# We want to ensure that only our Development instances are stopped to make sure nothing in Production is accidentally stopped. Add logic to your script that only stops **running**
#  instances that have the **Environment: Dev** tag.

import boto3
import json
# print(json.dumps(response, indent=2, default=str))


ec2_client = boto3.client("ec2")
x = ec2_client.describe_instances()
data = (x['Reservations'])



li = []
# wondering f I can make that instance_id part into a function? so I can just resuse it, and it just returns something back to me? idk
for instances in data:
    variables = instances["Instances"]
    for variable in variables:
        if (variable['State']['Name']) == 'running':
            tags = (variable['Tags'])
        else:
            print("THIS EC2 INSTANCE IS NOT RUNNING : ")
            instance_id = variable["InstanceId"]
            li.append(instance_id)
            for tag in tags:
                if tag['Value'] == 'Stage':
                    instance_id = variable["InstanceId"]
                    li.append(instance_id)
                else:
                    print("THIS EC2 IS RUNNING BUT DOES NOT HAVE THE RIGHT TAG")
                    instance_id = variable["InstanceId"]
                    li.append(instance_id)

print(li)
# print(ec2_client.terminate_instances(InstanceIds=li))