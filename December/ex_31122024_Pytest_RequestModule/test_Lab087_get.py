from http.client import responses

import pytest
import allure
import requests

base_url="https://restful-booker.herokuapp.com"  #global
headers={
        "Content-Type":"application/json"
    }

def get_token():
    base_path="/auth"
    full_path=base_url+base_path
    json_payload_auth={
        "username": "admin",
        "password": "password123"
    }
    response_path=requests.post(url=full_path,headers=headers,json=json_payload_auth)
    print(response_path)
    assert response_path.status_code == 200
    response_path_json=response_path.json()
    token=response_path_json["token"]
    #print(token)
    assert type(token)==str
    assert len(token)>0
    return token
def get_booking_id():
    base_path="/booking"
    full_url=base_url+base_path
    json_pay_load={
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,  # This will be automatically converted to `true` in the JSON request
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data=requests.post(url=full_url,headers=headers,json=json_pay_load)
    assert response_data.status_code==200
    response_data_json = response_data.json()  # converting everything into json data
    bookingid = response_data_json["bookingid"]
    assert bookingid is not None
    assert bookingid>0
    return bookingid

def test_put_request():
    token=get_token()
    booking_id=get_booking_id()
    print(token)
    print(booking_id)