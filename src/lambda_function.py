import json
import os

# デプロイのたびに変えてカナリアの動作を確認する
VERSION = "v4"

def lambda_handler(event, context):
    # AWS_EXECUTION_ENV は Lambda runtime にのみ存在する変数
    # → pytest では通過、Lambda 上では例外が発生する（unit test が拾えないバグの再現）
    if os.environ.get("AWS_EXECUTION_ENV"):
        raise Exception("Intentional canary failure for rollback demo")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from canary Lambda",
            "version": VERSION,
            "stage": os.environ.get("STAGE", "prod"),
        }),
    }
