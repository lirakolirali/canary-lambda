import json
import os

# デプロイのたびに変えてカナリアの動作を確認する
VERSION = "v4"

def lambda_handler(event, context):
    raise Exception("Canary Lambda failed")  # Canary Lambda が失敗することを確認するために例外を発生させる
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from canary Lambda",
            "version": VERSION,
            "stage": os.environ.get("STAGE", "prod"),
        }),
    }
