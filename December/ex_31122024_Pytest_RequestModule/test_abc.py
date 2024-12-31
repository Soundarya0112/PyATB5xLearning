import pytest
import allure
import requests
@allure.title("TC1- Create booking CRUD postive")
@allure.description("Verify the create booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url="https://restful-booker.herokuapp.com"
    base_path_post="/booking"
    #base_path_put="/booking/1"
    payload = {
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
    response_data=requests.post(url=full_url,headers=headers,json=payload)
    full_url=base_url+base_path_post
    headers={
        "Content-Type":"application/json"
    }
    #status code verification
    assert response_data.status_code==500
    #booking id verification
    response_data_json= response_data.json()
    bookingid=response_data_json["bookingid"]
    print(bookingid)
    assert bookingid is not None
    assert bookingid >0
