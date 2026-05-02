import json
import os

# デプロイのたびに変えてカナリアの動作を確認する
VERSION = "v4"

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from canary Lambda",
            "version": VERSION,
            "stage": os.environ.get("STAGE", "prod"),
        }),
    }
