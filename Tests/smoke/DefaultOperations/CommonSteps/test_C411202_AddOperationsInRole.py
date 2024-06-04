from Functions.AuthPage import AuthPage
from ConfigReader import ConfigClass
import pytest
from pytest_testrail.plugin import pytestrail
from Functions.DefaultButtons import DefaultButtonsPage
from Functions.FilterButtons import FilterButtonsPage


def test_C411202_AddOperationsInRole(browser):
        "Добавление операций в роль пользователя https://test-rail.norbit.ru/index.php?/cases/view/411202"
        
        login_page = AuthPage(browser)
        menu_page = DefaultButtonsPage(browser)
        filter_page = FilterButtonsPage(browser)


        # Auth
        login_page.go_to_site()      
        login_page.enter_login(ConfigClass().get_second_user_login())
        login_page.enter_password(ConfigClass().get_second_user_pass()) 
        login_page.click_submit()
        menu_page.simple_pause(2)
        
        
        # add operation
        menu_page.click_menu_selector()
        menu_page.simple_pause(2)
        menu_page.click_configuration()
        menu_page.click_menu_administration()
        menu_page.simple_pause(2)
        menu_page.click_menu_role()
        menu_page.simple_pause(2)
        filter_page.click_add_filter_role()
        menu_page.simple_pause(2)      
        filter_page.input_input_name_field("Наименование роли")
        menu_page.simple_pause(2)
        filter_page.input_search_input_name_object("zigol2")
        menu_page.simple_pause(2)
        filter_page.click_apply_filter_role()
        menu_page.simple_pause(6)
        menu_page.click_dots_button(0)
        menu_page.click_context_button("Изменить")
        menu_page.simple_pause(2)
        menu_page.click_link()
        menu_page.simple_pause(4)
        filter_page.click_add_filter_operation()
        menu_page.simple_pause(2)
        filter_page.input_input_name_field_operation("Наименование")
        filter_page.input_search_input_name_object_operation("contact")
        filter_page.click_apply_filter_operation()
        menu_page.simple_pause(6)
        menu_page.click_checkbox_getall()
        menu_page.click_menu_ok()
        menu_page.simple_pause(2)
        menu_page.click_save_button()
        menu_page.simple_pause(10)





