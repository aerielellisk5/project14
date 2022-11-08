#Foundational
# Scenario: Our DevOps engineering team often uses a development lab to test releases of our application. The Managers are complaining about the rising cost of our development 
# lab and need to save money by stopping our (for this example) 3 ec2 instances after all engineers are clocked out.

# **Create a Python script that you can run that will stop all instances.**


import boto3
import json
# this code will print a lot prettier!
# print(json.dumps(response, indent=2, default=str))

# NOTES
# Figure out why theres resource vs client when dealing with boto3


ec2_resource = boto3.resource("ec2")

new_resource = ec2_resource.create_instances(
    ImageId='ami-09d3b3274b6c5d4aa',
    InstanceType='t2.micro',
    MaxCount=2,
    MinCount=2,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            # 'capacity-reservation'|'client-vpn-endpoint'|'customer-gateway'|'carrier-gateway'|'coip-pool'|'dedicated-host'|'dhcp-options'|'egress-only-internet-gateway'|'elastic-ip'|'elastic-gpu'|'export-image-task'|'export-instance-task'|'fleet'|'fpga-image'|'host-reservation'|'image'|'import-image-task'|'import-snapshot-task'|'instance'|'instance-event-window'|'internet-gateway'|'ipam'|'ipam-pool'|'ipam-scope'|'ipv4pool-ec2'|'ipv6pool-ec2'|'key-pair'|'launch-template'|'local-gateway'|'local-gateway-route-table'|'local-gateway-virtual-interface'|'local-gateway-virtual-interface-group'|'local-gateway-route-table-vpc-association'|'local-gateway-route-table-virtual-interface-group-association'|'natgateway'|'network-acl'|'network-interface'|'network-insights-analysis'|'network-insights-path'|'network-insights-access-scope'|'network-insights-access-scope-analysis'|'placement-group'|'prefix-list'|'replace-root-volume-task'|'reserved-instances'|'route-table'|'security-group'|'security-group-rule'|'snapshot'|'spot-fleet-request'|'spot-instances-request'|'subnet'|'subnet-cidr-reservation'|'traffic-mirror-filter'|'traffic-mirror-session'|'traffic-mirror-target'|'transit-gateway'|'transit-gateway-attachment'|'transit-gateway-connect-peer'|'transit-gateway-multicast-domain'|'transit-gateway-policy-table'|'transit-gateway-route-table'|'transit-gateway-route-table-announcement'|'volume'|'vpc'|'vpc-endpoint'|'vpc-endpoint-connection'|'vpc-endpoint-service'|'vpc-endpoint-service-permission'|'vpc-peering-connection'|'vpn-connection'|'vpn-gateway'|'vpc-flow-log'|'capacity-reservation-fleet'|'traffic-mirror-filter-rule'|'vpc-endpoint-connection-device-type'|'vpn-connection-device-type',
            'Tags': [
                
                {
                    'Key': 'Environment',
                    'Value': 'Stage'
                },
            ]
        },
    ],

)

# print(len(new_resource))


# Basic
ec2_client = boto3.client("ec2")
x = ec2_client.describe_instances()
data = (x['Reservations'])
# print(data)
# print(json.dumps(data, indent=2, default=str))


li = []

for instances in data:
    variables = instances["Instances"]
    # print(json.dumps(variables, indent=2, default=str))
    # print(len(variables))
    for variable in variables:
        if (variable['State']['Name']) == 'running':
            instance_id = variable["InstanceId"]
            li.append(instance_id)
print(li)
    
# print(ec2_client.terminate_instances(InstanceIds=li))





        


