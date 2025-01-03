import pytest
import requests
from allure_commons import fixture
from dotenv import load_dotenv
import os


#writing the common functions--so that by using fixture we can reuse in other programs

@pytest.fixture()
def create_token():
    load_dotenv()
    username=os.getenv("USERNAME")
    password=os.getenv("PASSWORD")
    print(username, password)
    base_url = "https://restful-booker.herokuapp.com"  # global
    headers = {
        "Content-Type": "application/json"
    }
    base_path = "/auth"
    full_path = base_url + base_path
    json_payload_auth = {
        "username": username,
        "password": password
    }
    response_path = requests.post(url=full_path, headers=headers, json=json_payload_auth)
    print(response_path)
    #assert response_path.status_code==200
    response_path_json = response_path.json()
    token = response_path_json["token"]
    print(token)
@pytest.fixture()
def create_booking_id():
    base_path = "/booking"
    base_url = "https://restful-booker.herokuapp.com"
    full_url = base_url + base_path
    json_pay_load = {
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
    headers = {
        "Content-Type": "application/json"
    }
    response_data = requests.post(url=full_url, headers=headers, json=json_pay_load)
    #assert response_data.status_code == 200
    response_data_json = response_data.json()  # converting everything into json data
    bookingid = response_data_json["bookingid"]
    return bookingid

@pytest.fixture()
def read_csv_file_data():
    pass
@pytest.fixture()
def read_mysql_file_database():
    pass
@pytest.fixture()
def read_url_testdata_excel():
    pass
