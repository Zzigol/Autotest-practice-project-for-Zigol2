from Functions.AuthPage import AuthPage
from ConfigReader import ConfigClass
import pytest
class TestUserAuth():
    def test_setup(self, browser):
        link = "https://kube-autotest01.nbt.dpr.norbit.ru/" '''ConfigClass.get_site_url()'''
        self.login_page = AuthPage(browser, link)
        self.login_page.open()        
        username = ConfigClass.get_second_user_login()
        password = ConfigClass.get_second_user_pass()
        self.login_page.auth_user(username, password)
        