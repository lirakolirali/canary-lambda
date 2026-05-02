#!/bin/bash
# 既存リソースの状態確認スクリプト
# 実行: bash poc/app/canary-lambda/infra/verify.sh

FUNCTION_NAME="cicd_test_lambda"
ALIAS_NAME="live"
REGION="ap-northeast-1"

echo "=== Lambda 関数 ==="
aws lambda get-function \
  --function-name $FUNCTION_NAME \
  --region $REGION \
  --query 'Configuration.{Name:FunctionName, Runtime:Runtime, Handler:Handler}' \
  --output table

echo ""
echo "=== バージョン一覧 ==="
aws lambda list-versions-by-function \
  --function-name $FUNCTION_NAME \
  --region $REGION \
  --query 'Versions[].{Version:Version, Modified:LastModified}' \
  --output table

echo ""
echo "=== Alias (live) の現在状態 ==="
aws lambda get-alias \
  --function-name $FUNCTION_NAME \
  --name $ALIAS_NAME \
  --region $REGION \
  --query '{StableVersion:FunctionVersion, Routing:RoutingConfig}' \
  --output table

echo ""
echo "=== 動作確認（live alias を invoke）==="
aws lambda invoke \
  --function-name "${FUNCTION_NAME}:${ALIAS_NAME}" \
  --payload '{"test": true}' \
  --cli-binary-format raw-in-base64-out \
  --region $REGION \
  /tmp/lambda_response.json > /dev/null

echo "Response:"
cat /tmp/lambda_response.json
echo ""
