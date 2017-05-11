# VPC subnet
import boto3
ec2client = boto3.client('ec2')
for vpc in ec2client.describe_vpcs()["Vpcs"]:
# ["Vpcs"] identifier as is in the response syntax in the method called 
    for subnet in ec2client.describe_subnets(Filters=[{'Name':'vpc-id','Values':[vpc["VpcId"]]}])["Subnets"]:
        for rt in ec2client.describe_route_tables(Filters=[{'Name':'vpc-id','Values':[vpc["VpcId"]]}])["RouteTables"]:
            for det in rt['Routes']:
                print(vpc['VpcId'] +"," + vpc['State'] +"," + vpc['CidrBlock'] + "," + subnet['SubnetId']+ "," + str(subnet['DefaultForAz']) + ","+ subnet['CidrBlock']+ "," + subnet['AvailabilityZone']+ "," + str(subnet['AvailableIpAddressCount'])+","+" route table_id " + rt['RouteTableId']  + " route_tables " + det['GatewayId'])
