import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from lambda_function import lambda_handler


def test_status_200():
    response = lambda_handler({}, None)
    assert response["statusCode"] == 200


def test_body_has_version():
    response = lambda_handler({}, None)
    body = json.loads(response["body"])
    assert "version" in body


def test_body_has_message():
    response = lambda_handler({}, None)
    body = json.loads(response["body"])
    assert body["message"] == "Hello from canary Lambda"


def test_event_passthrough():
    response = lambda_handler({"key": "value"}, None)
    assert response["statusCode"] == 200
