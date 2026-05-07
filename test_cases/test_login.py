import pytest
import requests
from utils.config import BASE_URL

def test_valid_login_returns_token(login_data):

    print(login_data)   # debug

    response = requests.post(f"{BASE_URL}/login", json=login_data)

    print(response.status_code)
    print(response.text)

    assert response.status_code == 200, \
        f"Login Failed. Response: {response.text}"

    token = response.json().get("authToken")

    assert token is not None, \
        "Auth token is not in response"