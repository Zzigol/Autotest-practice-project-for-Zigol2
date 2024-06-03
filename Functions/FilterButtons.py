from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from BaseClass import BasePage
   
class FilterButtonsLocators():

    # Добавить фильтр в реестре
    ADD_FILTER_ROLE_BUTTON = (By.XPATH, "//*[name()='rect' and contains(@opacity,'0.2')]")

    # Нажать "Выбрать" в поле фильтры в реестре
    CHOOSE_FILTER_ROLE_BUTTON = (By.XPATH, "//div[@data-testid='field']//div[@role='button']//div//div[1]//*[name()='svg']")

    # Нажать "Название поля" в поле фильтра в реестре
    ROLE_NAME_BUTTON = (By.XPATH, "(//input[@id='search-select-field-fieldName']") 

    # Выбрать поле "Значение поля" в реестре
    ROLE_FILD_VALUE_BUTTON = (By.XPATH, "//input[@id='text-field-fieldValue']")

    # Применить фильтр в реестре
    APPLY_FILTER_BUTTON = (By.XPATH, "//button[@data-testid='apply-filter']")

    # Добавить фильтр в ссылке на коллекцию
    ADD_FILTER_OPERATION_BUTTON = (By.XPATH, "//button[@data-testid='add-condition']")

    # Нажать "Название поля" в поле фильтры в ссылке на коллекцию
    CHOOSE_FILTER_OPERATION_BUTTON = (By.XPATH, "//input[@id='search-select-field-fieldName']")

    # Выбрать поле "Значение поля" в ссылке на коллекцию
    OPERATION_FILD_VALUE_BUTTON = (By.XPATH, "//input[@id='text-field-fieldValue']")

    # Применить фильтр в ссылке на коллекцию
    APPLY_OPERATION_FILTER_BUTTON = (By.XPATH, "//button[@data-testid='apply-filter']")




class FilterButtonsPage(BasePage):

    def click_add_filter_role(self):
        """Функция добавляет фильтр в роли"""
        self.find_element(FilterButtonsLocators.ADD_FILTER_ROLE_BUTTON).click()

    def click_choose_filter_role(self):
        """Функция добавляет фильтр в роли"""
        self.find_element(FilterButtonsLocators.CHOOSE_FILTER_ROLE_BUTTON).click()

    def input_input_name_field(self, name_field: str) -> str:
        """Нажать в поле Название поля и ввести значение

        Args:
            - name_field - название поля
        """
        inputnamefield = self.find_element(FilterButtonsLocators.ROLE_NAME_BUTTON)
        FIELD_LOCATOR = (By.XPATH, f'//div[@data-testid="menuitem"]//*[text()="{name_field}"]')
        inputnamefield.click()
        inputnamefield.send_keys(Keys.CONTROL + 'a')
        inputnamefield.send_keys(name_field)
        self.simple_pause(1)
        return self.find_element(FIELD_LOCATOR).click()  

    def input_search_input_name_object(self, name_object: str) -> str:
        """Нажать в поле Значение поля и ввести значение

        Args:
            - name_object - значение поля для фильтрации
        """
        inputnamefilter = self.find_element(FilterButtonsLocators.ROLE_FILD_VALUE_BUTTON,time=5)
        inputnamefilter.click()
        inputnamefilter.send_keys(Keys.CONTROL + 'a')
        inputnamefilter.send_keys(name_object)
        fact_filter = inputnamefilter.get_attribute('value')
        assert fact_filter == name_object, f'Текущее значение заполнено {fact_filter} вместо {name_object}'
        return inputnamefilter    


    def click_apply_filter_role(self):
        """Функция применяет фильтр в роли"""
        self.find_element(FilterButtonsLocators.APPLY_FILTER_BUTTON).click()

    def click_add_filter_operation(self):
        """Функция добавляет фильтр в ссылке на коллекцию"""
        self.find_element(FilterButtonsLocators.ADD_FILTER_OPERATION_BUTTON).click()    

    def input_input_name_field_operation(self, name_field: str) -> str:
        """Нажать в поле Название поля и ввести значение

        Args:
            - name_field - название поля
        """
        inputnamefield = self.find_element(FilterButtonsLocators.CHOOSE_FILTER_OPERATION_BUTTON)
        FIELD_LOCATOR = (By.XPATH, f'//div[@data-testid="menuitem"]//*[text()="{name_field}"]')
        inputnamefield.click()
        inputnamefield.send_keys(Keys.CONTROL + 'a')
        inputnamefield.send_keys(name_field)
        self.simple_pause(1)
        return self.find_element(FIELD_LOCATOR).click()    
      
    def input_search_input_name_object_operation(self, name_object: str) -> str:
        """Нажать в поле Значение поля и ввести значение

        Args:
            - name_object - значение поля для фильтрации
        """
        inputnamefilter = self.find_element(FilterButtonsLocators.OPERATION_FILD_VALUE_BUTTON,time=5)
        inputnamefilter.click()
        inputnamefilter.send_keys(Keys.CONTROL + 'a')
        inputnamefilter.send_keys(name_object)
        fact_filter = inputnamefilter.get_attribute('value')
        assert fact_filter == name_object, f'Текущее значение заполнено {fact_filter} вместо {name_object}'
        return inputnamefilter    
    
    def click_apply_filter_operation(self):
        """Функция применяет фильтр в ссылке на коллекцию"""
        self.find_element(FilterButtonsLocators.APPLY_OPERATION_FILTER_BUTTON).click()   
                                    