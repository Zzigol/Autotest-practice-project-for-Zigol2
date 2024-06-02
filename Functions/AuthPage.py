from selenium.webdriver.common.by import By

   
class AuthPageLocators():

    AUTH_FORM = (By.CSS_SELECTOR, "#Username")
    AUTH_PASSWORD = (By.CSS_SELECTOR, "#Password")    
    AUTH_BUTTON = (By.CSS_SELECTOR, "button['#submitLoginForm']")

class AuthPage():
    def auth_user(self, username, password):        
        username_field = self.browser.find_element(*AuthPageLocators.AUTH_FORM)
        username_field.send_keys(username)
        password_field = self.browser.find_element(*AuthPageLocators.AUTH_PASSWORD)
        password_field.send_keys(password)        
        button_submit = self.browser.find_element(*AuthPageLocators.AUTH_BUTTON)
        button_submit.click()    