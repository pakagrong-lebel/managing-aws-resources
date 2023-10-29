# Python script to manage AWS resources using Boto3
import boto3
def create_ec2_instance(instance_type, image_id, key_name, security_group_ids):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=security_group_ids,
        MinCount=1,
        MaxCount=1
    )
    return instance[0].id




