import json
import boto3
from botocore.exceptions import ClientError
from boto3.s3.transfer import TransferConfig
#===========================================================================#
# Create IAM User
def create_iam_user(user_name):
    try:
        iam_client = boto3.client('iam')
        response = iam_client.create_user(UserName=user_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
    return response
# TEST CODE IN SERVER
# responseObject = iam_functions.create_iam_user("Test1")
# print(responseObject)
#===========================================================================#
def add_user_to_default_group(user_name):
    try:
        iam_client = boto3.client('iam')
        iam_client.add_user_to_group(GroupName='Janitors', UserName=user_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
#===========================================================================#
# List all IAM users
def list_iam_users():
    try:
        iam_client = boto3.client('iam')
        paginator = iam_client.get_paginator('list_users')
        name_list = []
        for response in paginator.paginate():
            for user in response["Users"]:
                #print("Username: ", user["UserName"])
                name_list.append(user["UserName"])
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
    return name_list
# TEST CODE IN SERVER
#list_iam_users()
#===========================================================================#
# Update an IAM username
def update_iam_user(existing_username, new_username):
    try:
        iam_client = boto3.client('iam')
        iam_client.update_user(UserName=existing_username, NewUserName=new_username)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
# TEST CODE IN SERVER
#update_iam_user("Test1, "Test2")
#===========================================================================#
# Delete an IAM user
def delete_iam_user(existing_username):
    try:
        iam_client = boto3.client('iam')
        iam_client.delete_user(UserName=existing_username)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
# TEST CODE IN SERVER
#delete_iam_user("Test2")
#===========================================================================#
# Create Policy
def create_iam_policy(policy_name, policy_json):
    try:
        iam_client = boto3.client('iam')
        iam_client.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_json)
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
    return True
# TEST CODE IN SERVER
# custom_policy_json = {
#         "Version": "2022-10-3",
#         "Statement": [{
#             "Effect": "Allow",
#             "Action": [
#                 "ec2:*"
#             ],
#             "Resource": "*"
#         }]
#     }
# create_iam_policy("test_policy_1_by_max", custom_policy_json)
#===========================================================================#
# Attach custom policy to specific user
def attatch_custom_iam_policy_with_user(policy_name, username):
    try:
        sts = boto3.client('sts')
        account_id = sts.get_caller_identity()['Account']
        policy_arn = f'arn:aws:iam::{account_id}:policy/{policy_name}'
        iam_client = boto3.client('iam')
        iam_client.attach_user_policy(
            UserName=username,
            PolicyArn=policy_arn,
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
# TEST CODE IN SERVER
# create_iam_user("test100")
# attatch_custom_iam_policy_with_user("test_policy_1_by_max", "test100")
#===========================================================================#
# Detach custom policy from user
def detach_custom_policy_from_user(policy_name, username):
    try:
        sts = boto3.client('sts')
        account_id = sts.get_caller_identity()['Account']
        policy_arn = f'arn:aws:iam::{account_id}:policy/{policy_name}'
        iam_client = boto3.client('iam')
        iam_client.detach_user_policy(
            UserName=username,
            PolicyArn=policy_arn,
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
# TEST CODE IN SERVER
#detach_custom_policy_from_user("swag", "MAX")
#===========================================================================#
# Attatch Managed policy to user
def attatch_managed_iam_policy_with_user(policy_name, username):
    try:
        sts = boto3.client('sts')
        account_id = sts.get_caller_identity()['Account']
        policy_arn = f'arn:aws:iam::aws:policy/{policy_name}'
        iam_client = boto3.client('iam')
        iam_client.attach_user_policy(
            UserName=username,
            PolicyArn=policy_arn,
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
# TEST CODE IN SERVER
# attatch_managed_iam_policy_with_user("AWSMarketplaceFullAccess", "MAX")
#===========================================================================#
# Detach managed policy from user
def detach_managed_policy_from_user(policy_name, username):
    try:
        sts = boto3.client('sts')
        account_id = sts.get_caller_identity()['Account']
        policy_arn = f'arn:aws:iam::aws:policy/{policy_name}'
        iam_client = boto3.client('iam')
        iam_client.detach_user_policy(
            UserName=username,
            PolicyArn=policy_arn,
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
# TEST CODE IN SERVER
#detach_managed_policy_from_user("AWSMarketplaceFullAccess", "MAX")
#===========================================================================#
def get_user_info_iam(username):
    try:
        #sts = boto3.client('sts')
        #account_id = sts.get_caller_identity()['Account']
        #user_arn = f'arn:aws:iam::{account_id}:user/{username}'
        iam_client = boto3.client('iam')
        response = iam_client.get_user(
            UserName=username,
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
    return response

#===========================================================================#
def get_user_group(username):
    try:
        iam_client = boto3.client('iam')
        response = iam_client.list_groups_for_user(
            UserName=username,
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
    return response
#===========================================================================#
def remove_user_from_group(username, group):
    try:
        iam_client = boto3.client('iam')
        response = iam_client.remove_group(
            UserName=username,
            GroupName=group
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("Object already exists.")
        else:
            print(f"Unexpected error: '{e}'")
#===========================================================================#