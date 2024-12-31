import pytest
import allure
import requests
@allure.title("Tc1- Verifying the basic math testcase 2-2==0 ")
@allure.description("Basic positive test case")
@pytest.mark.positive
def test_sub1():
    assert 2-2==0
@allure.title("Tc2- Verifying the basic math testcase 2+2==5 ")
@allure.description("Basic negative test case")
@pytest.mark.negative
def test_add():
    assert 2+2==5
@allure.title("Tc3- Verifying the basic math testcase 2+2==4 ")
@allure.description("Basic positive test case")
@pytest.mark.positive
def test_add():
    assert 2+2==4
@pytest.mark.skip(reason="skip it")
def test_add2():
    assert 0+0!=0