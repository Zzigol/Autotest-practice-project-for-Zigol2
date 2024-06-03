from Functions.AuthPage import AuthPage
from ConfigReader import ConfigClass
import pytest
from pytest_testrail.plugin import pytestrail


def test_Auth(browser):
        
        login_page = AuthPage(browser)
        login_page.go_to_site()      
        login_page.enter_login(ConfigClass().get_second_user_login())
        login_page.enter_password(ConfigClass().get_second_user_pass()) 
        login_page.clic_submit()
        