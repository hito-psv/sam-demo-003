import json
import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch
from datetime import datetime

patch(['boto3'])

@xray_recorder.capture('put_item ddb')
def lambda_handler(event, context):
    event_body = json.loads(event["body"])
    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("Demo")
    table.put_item(
        Item={
            "Key": event_body["key"],
            "CreateDate": datetime.utcnow().isoformat()
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "succeeded",
        }),
    }