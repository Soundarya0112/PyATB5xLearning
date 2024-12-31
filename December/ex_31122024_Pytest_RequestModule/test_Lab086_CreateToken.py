import pytest
import allure
import requests

base_url="https://restful-booker.herokuapp.com"  #global
headers={
        "Content-Type":"application/json"
    }
#@allure.title("TC1- Create token")
#@allure.description("Verify the create token")
#@pytest.mark.positivee

def test_create_token_tc1():
    base_path="/auth"
    full_path=base_url+base_path
    json_payload_auth={
        "username": "admin",
        "password": "password123"
    }
    response_path=requests.post(url=full_path,headers=headers,json=json_payload_auth)
    print(response_path)

    response_path_json=response_path.json()
    token=response_path_json["token"]
    print(token)
    assert response_path.status_code == 200
    assert type(token)==str
    assert len(token)<0