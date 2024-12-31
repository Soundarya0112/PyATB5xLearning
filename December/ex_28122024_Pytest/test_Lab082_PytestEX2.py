import pytest
import allure
@allure.title("Create booking test cases")
@allure.description("postive test case checking ")
@pytest.mark.positive
def test_create_booking_positive1():
    print("positive test case 1")
    assert 5 == 5

@pytest.mark.positive
def test_create_booking_positive2():
    print("positive test case 2")
    assert True==1
@allure.title("Create booking test cases")
@allure.description("postive test case checking ")
@pytest.mark.negative
def test_create_negative1():
    print("Negative test case 1")
    assert 1+1==0
@pytest.mark.negative
def test_create_booking_Negative2():
    print("Negative test case 2")
    assert True==0
