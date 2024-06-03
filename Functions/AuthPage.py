from selenium.webdriver.common.by import By
from BaseClass import BasePage
   
class AuthPageLocators():

    AUTH_FORM = (By.CSS_SELECTOR, "#Username")
    AUTH_PASSWORD = (By.CSS_SELECTOR, "#Password")    
    AUTH_BUTTON = (By.CSS_SELECTOR, "button['#submitLoginForm']")

class AuthPage(BasePage):

    def enter_login(self, username: str):
        username_field = self.find_element(*AuthPageLocators.AUTH_FORM)
        username_field.click()
        username_field.send_keys(username)
        return username_field

    def enter_password(self, password: str):
        password_field = self.find_element(*AuthPageLocators.AUTH_PASSWORD)
        password_field.click()
        password_field.send_keys(password)
        return password_field

    def click_submit(self):
        return self.find_element(*AuthPageLocators.AUTH_BUTTON).click()