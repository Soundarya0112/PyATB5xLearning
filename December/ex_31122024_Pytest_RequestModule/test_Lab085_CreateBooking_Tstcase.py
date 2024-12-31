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
    full_url=base_url+base_path_post
    headers={
        "Content-Type":"application/json"
    }
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
    #status code verification
    assert response_data.status_code==200
    #booking id verification
    response_data_json=response_data.json() #converting everything into json data
    bookingid=response_data_json["bookingid"]
    print(bookingid)
    assert bookingid is not None
    assert bookingid >0
    assert type(bookingid)==int

    firstname=response_data_json["booking"]["firstname"]
    assert firstname=="Jim"
    assert type(firstname)==str
    print(firstname)

    lastname = response_data_json["booking"]["lastname"]
    assert lastname == "Brown"
    assert type(lastname) == str
    print(lastname)

    total_price=response_data_json["booking"]["totalprice"]
    assert total_price==111
    assert type(total_price)==int

    depositpaid=response_data_json["booking"]["depositpaid"]
    assert depositpaid==True

    checkin=response_data_json["booking"]["bookingdates"]["checkin"]
    checkout=response_data_json["booking"]["bookingdates"]["checkout"]
    assert checkin=="2018-01-01"
    assert checkout=="2019-01-01"

    time=response_data.elapsed.total_seconds()
    assert time<3

@allure.title("TC2- Create booking CRUD Negative")
@allure.description("Verify the create booking negative testcase")
@pytest.mark.crudnegative
def test_create_booking_negative_tc2():
    base_url="https://restful-booker.herokuapp.com"
    base_path_post="/booking"
    #base_path_put="/booking/1"
    full_url=base_url+base_path_post
    headers={
        "Content-Type":"application/json"
    }
    payload={}
    response_data = requests.post(url=full_url, headers=headers, json=payload)
    # status code verification
    assert response_data.status_code == 200
    assert response_data.text=="Internal Server Error"