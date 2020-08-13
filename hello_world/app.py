import json
from aws_xray_sdk.core import xray_recorder

@xray_recorder.capture('hello world')
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        })
    }