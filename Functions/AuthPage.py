from selenium.webdriver.common.by import By
from BaseClass import BasePage
   
class AuthPageLocators():

    AUTH_FORM = (By.ID, "Username")
    AUTH_PASSWORD = (By.ID, "Password")    
    AUTH_BUTTON = (By.ID, "submitLoginForm")

class AuthPage(BasePage):

    def enter_login(self, username: str):
        username_field = self.find_element(AuthPageLocators.AUTH_FORM)
        username_field.click()
        username_field.send_keys(username)
        '''return username_field'''

    def enter_password(self, password: str):
        password_field = self.find_element(AuthPageLocators.AUTH_PASSWORD)
        password_field.click()
        password_field.send_keys(password)
        '''return password_field'''

    def click_submit(self):
        self.find_element(AuthPageLocators.AUTH_BUTTON).click()