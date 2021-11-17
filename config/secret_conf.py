import json

def get_secret_key() -> str:
    with open("secret.json", "r") as secret:
        key = json.load(secret)
    return key["secret_key"]

def get_aws_secret_key() -> dict:
    with open("secret.json", "r") as secret:
        key = json.load(secret)
    
    key_list = {}
    key_list['access_key_id'] = key["access_key_id"]
    key_list['secret_access_key'] = key["secret_access_key"]
    key_list['bucket_name'] = key["bucket_name"]

    return key_list