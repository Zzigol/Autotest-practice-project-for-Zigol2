from selenium.webdriver.common.by import By
from BaseClass import BasePage
import pytest
   
class DefaultButtonsLocators():

    # Раскрыть выпадающий список "Разделы"
    MENU_SELECTOR_BUTTON = (By.XPATH, "//*[@data-testid = 'section']")

    # В разделах выбрать раздел "Конфигурирование"
    CONFIGURATION_BUTTON = (By.XPATH, "(//span[contains(text(),'Конфигурирование')])[2]")

    # Выбрать группу реестров "Администрирование"
    ADMIN_MENU_BUTTON = (By.XPATH, "//span[contains(text(),'Администрирование')]")

    # Выбрать реестр "Роли"
    ROLE_MENU_BUTTON = (By.XPATH, "//span[contains(text(),'Роли')]")

    # Открыть контекстное меню записи
    CONTEXT_MENU_LOCATORS = (By.XPATH, '//*[@data-testid="context-menu-buttons"]/li')

    # Прикрепить в ссылке на коллекцию 
    LINK_MENU_BUTTON = (By.XPATH, "//button[@id='fab-link']")

    # Проставить чекбокс выбрать всё
    CHECKBOX_GET_ALL = (By.XPATH, "//span[@value='partial']//*[name()='svg']")

    # Подтвердить выбранные роли
    OK_MENU_BUTTON = (By.XPATH, "//button[contains(text(),'ОК')]")

    # Сохранить изменения в роли
    SAVE_MENU_BUTTON = (By.XPATH, "//button[@id='fab-check']")

    # Кнопка контекстного меню (ввиде трех точек)
    DOTS_BUTTON = (By.XPATH, '//span[contains(@id, "cell-context-menu-col-")]')

    # Окно об успешном сохранении
    SAVE_WINDOW = (By.XPATH, '//strong')






class DefaultButtonsPage(BasePage):

    def click_menu_selector(self):
        """Функция нажимает кнопку выпадающего списка "Разделы"""
        self.find_element(DefaultButtonsLocators.MENU_SELECTOR_BUTTON).click()

    def click_configuration(self):
        """Функция нажимает кнопку "Конфигурация" в выпадающем списке "Разделы"""
        self.find_element(DefaultButtonsLocators.CONFIGURATION_BUTTON).click()

    def click_menu_administration(self):
        """Функция нажимает кнопку "Администрирование" в меню"""
        self.find_element(DefaultButtonsLocators.ADMIN_MENU_BUTTON).click()

    def click_menu_role(self):
        """Функция нажимает кнопку "Роли" в меню"""
        self.find_element(DefaultButtonsLocators.ROLE_MENU_BUTTON).click()

    def click_context_button(self, button_name):
        """Функция нажимает кнопку контекстного меню, название которой было передано в параметре функции

        Args:
            - button_name - название кнопки
        """
        self.simple_pause(2)
        self.buttons = self.find_elements(DefaultButtonsLocators.CONTEXT_MENU_LOCATORS)
        for button in self.buttons:
            if button.text == button_name:
                return button.click()
        pytest.fail('Не найдена кнопка переданная в функцию')

    def click_link(self):
        """Функция нажимает кнопку "Прикрепить" в ссылке на коллекцию"""
        self.find_element(DefaultButtonsLocators.LINK_MENU_BUTTON).click()

    def click_checkbox_getall(self):
        """Функция нажимает чекбокс выделить всё в ссылке на коллекцию"""
        self.find_element(DefaultButtonsLocators.CHECKBOX_GET_ALL).click()

    def click_menu_ok(self):
        """Функция нажимает "ОК" в ссылке на коллекцию при прикреплении записей"""
        self.find_element(DefaultButtonsLocators.OK_MENU_BUTTON).click()

    def click_save_button(self):
        """Функция нажимает "Сохранить" при сохранении изменений в роли"""
        self.find_element(DefaultButtonsLocators.SAVE_MENU_BUTTON).click()

    def click_dots_button(self, row: int):
        """Нажать на контекстное меню в указанной строке реестра (начиная с 0)

        Args:
            - row - номер строки в реестре (начиная с 0)
        """
        self.buttons = self.find_elements(DefaultButtonsLocators.DOTS_BUTTON)
        return self.buttons[row].click()    
                            
    def save_window(self):
        """Функция находит подтверждение сохранения"""
        self.find_element(DefaultButtonsLocators.SAVE_WINDOW)                        