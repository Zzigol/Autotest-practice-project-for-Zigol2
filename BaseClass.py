import random
import string
import time
import psycopg2
import pyautogui
import pyperclip
import requests
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ConfigReader import ConfigClass
import keyboard
import mouse
import uuid

class BasePage:

     # Локатор всей страницы для прокрутки
    global LOCATOR_PAGE
    LOCATOR_PAGE = (By.TAG_NAME,'html')
    
    def __init__(self, driver):
        self.driver = driver
        self.base_url = ConfigClass().get_site_url()


    def find_element(self, locator,time=20):
        """Ищет один элемент, подходящий по условию"""
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")


    def find_elements(self, locator,time=10):
        """Ищет все элементы, подходящие по условию"""
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")


    def simple_pause(self, _time):
        """Пауза, необходимо в метод передавать число секунд, которое нужно ожидать"""
        return time.sleep(_time)


    def go_to_site(self):
        """Переходит на сайт указанный в settings.ini"""
        self.driver.get(self.base_url)
        # Проверяем наличие JS алерта и закрываем
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            True
        self.simple_pause(4)


    def delete_cookies(self):
        """Удаляем все куки в текущей сессии браузера. Можно использовать чтобы быстро разлогинится без необходимости прожимать кнопки"""
        self.driver.get('chrome://settings/clearBrowserData')
        # Проверяем наличие JS алерта и закрываем
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            True
        self.simple_pause(1)
        self.find_element((By.XPATH, '//body')).send_keys(Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.SPACE)
        self.simple_pause(2)
        return self.driver.delete_all_cookies()


    def hidden_to_visible_elem(self, elem):
        """Функция превращает невидимый элемент для загрузки в файла в видимый, чтобы селениум мог с ним взаимодействовать. Написано для теста с загрузкой сертификатов"""
        return self.driver.execute_script("arguments[0].removeAttribute('hidden'); arguments[0].classList.remove('uppy-Dashboard-input');return true;", elem)


    def send_select_sql(self, sql):
        """Делает селект из базы. Принимает параметр в виде запроса SQL"""
        try:
            connection = psycopg2.connect(
                                    user = ConfigClass().get_sql_username(),
                                    password = ConfigClass().get_sql_password(),
                                    host = ConfigClass().get_sql_host(),
                                    port = ConfigClass().get_sql_port(),
                                    database = ConfigClass().get_database_name())
            cursor = connection.cursor();
            cursor.execute(sql)
            record = cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            record = f"Ошибка при работе с PostgreSQL: {error}"
        finally:
            cursor.close()
            connection.close()
            return record


    def send_update_sql(self, sql):
        """Делает апдейт в базу. Принимает параметр в виде запроса SQL"""
        try:
            connection = psycopg2.connect(
                                    user = ConfigClass().get_sql_username(),
                                    password = ConfigClass().get_sql_password(),
                                    host = ConfigClass().get_sql_host(),
                                    port = ConfigClass().get_sql_port(),
                                    database = ConfigClass().get_database_name())
            cursor = connection.cursor();
            cursor.execute(sql)
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Ошибка при работе с PostgreSQL!", error)
        finally:
            cursor.close()
            connection.close()
            return


    def refresh_site(self):
        """Обновляет веб страницу"""
        self.driver.refresh()
        # Проверяем наличие JS алерта и закрываем
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            True
        self.simple_pause(3)
        return


    def generation_unic_string(self):
        """Генератор уникальных наименований"""
        str1 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        ls1 = list(str1) # Преобразуем строку в список
        random.shuffle(ls1) # Перемешиваем список
        unic_name = ''.join([random.choice(ls1) for x in range(10)]) # Извлекаем из списка 10 (можно любое число) произвольных значений
        return unic_name


    def generate_unic_letters_string(self):
        """Генератор уникальных наименований (только буквы)"""
        unic_letters = ''.join((random.choice(string.ascii_lowercase) for x in range(7)))
        return unic_letters


    def go_to_window(self, number):
        """Перейти на указанную вкладку"""
        window_after = self.driver.window_handles[number]
        return self.driver.switch_to.window(window_after)


    def close_window(self):
        """Закрыть текущую вкладку"""
        return self.driver.close()
    

    def open_new_tab(self, address):
        """Открываем новую вкладку
        
        Args:
            - address - адрес ссылки
        """
        self.driver.execute_script("window.open();")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(address)


    def get_windows_count(self):
        """Получить количество открытых вкладок"""
        return len(self.driver.window_handles)


    def click_page_up(self):
        """Прокрутка страницы вверх"""
        page_element = self.find_element(LOCATOR_PAGE)
        page_element.send_keys(Keys.HOME)


    def click_page_down(self):
        """Прокрутка страницы вниз"""
        page_element = self.find_element(LOCATOR_PAGE)
        page_element.send_keys(Keys.END)


    def click_half_page_down(self):
        """Частичная прокрутка вниз"""
        page_element = self.find_element(LOCATOR_PAGE)
        page_element.send_keys(Keys.PAGE_DOWN)
        

    def upload_bpmn_file(self, file_name:str, deployment_name:str):
        """Загружает файл BPMN из папки business_processes в камунду, урл которой указан в конфиг файле в разделе SITE, под ключом camunda.
        В консоли выводится результат загрузки

        Args:
            - file_name - название файла в папке(без расширения .bpmn)
            - deployment_name - название процесса
        """
        camunda_url = ConfigClass().get_camunda_url() + 'engine-rest'
        _deployment_name = deployment_name
        bpmn_file_path = "business_processes/" + file_name + ".bpmn"

        response = requests.post(
            camunda_url + "/deployment/create",
            data={"deployment-name": _deployment_name},
            files={"data": open(bpmn_file_path, 'rb')},
            verify=False
            )
        
        if response.status_code == 200:
            pass
        else:
            pytest.fail(f"Не удалось загрузить файл bpmn по пути {bpmn_file_path}")


    def get_page_url(self):
        """Возвращает URL открытой страницы в виде текстовой строки"""
        x = self.driver.current_url
        return x
    

    def send_select_warehouse_sql(self, sql):
        """Делает селект из базы warehouse. Принимает параметр в виде запроса SQL"""
        try:
            connection = psycopg2.connect(
                                    user = ConfigClass().get_sql_username(),
                                    password = ConfigClass().get_sql_password(),
                                    host = ConfigClass().get_sql_host(),
                                    port = ConfigClass().get_sql_port(),
                                    database = ConfigClass().get_database_warehouse_name())
            cursor = connection.cursor();
            cursor.execute(sql)
            record = cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            record = f"Ошибка при работе с PostgreSQL: {error}"
        finally:
            cursor.close()
            connection.close()
            return record


    def click_tab(self):
        """Нажать Tab"""
        keyboard.send('tab')


    def click_down(self):
        """Нажать стрелку вниз"""
        keyboard.send('down')
    

    def get_token(self):
        """Получение токена доступа для работы с api"""
        auth_url = ConfigClass().get_auth_url()
        client_id = ConfigClass().get_auth_client_id()
        client_secret = ConfigClass().get_auth_client_secret()
        username = ConfigClass().get_admin_login()
        password = ConfigClass().get_admin_pass()
        scope = ConfigClass().get_auth_scope()
        grant_type = ConfigClass().get_auth_grant_type()
        data = {
            "Client_Id": f"{client_id}",
            "Client_Secret": f"{client_secret}",
            "UserName": f"{username}",
            "Password": f"{password}",
            "Scope": f"{scope}",
            "grant_type": f"{grant_type}"
            }
        response = requests.post(
            auth_url,
            data=data,
            verify=False
            )
        
        token_data = response.json()
        headers_data = token_data["access_token"]
        headers = {
            'Authorization' : f'Bearer {headers_data}',
            'Content-Type' : 'application/json'
        }
        
        if response.status_code == 200:
            return headers
        else:
            pytest.fail("Не удалось получить токен доступа")


    def check_windows_count(self):
        """Проверить количество открытых вкладок браузера"""
        window_count = len(self.driver.window_handles)
        return window_count


    def save_unverified_file(self):
        """Сохранить непроверенный файл"""
        self.driver.get('chrome://downloads/')
        self.simple_pause(1)
        self.find_element((By.XPATH, '//body')).send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER)
        self.simple_pause(2)
        keyboard.send('tab')
        self.simple_pause(2)
        keyboard.send('enter')
        self.simple_pause(2)


    def dropdown_scroll(self, dx: int = 0, dy=80):
        """Прокручивает скролл в выпадающих списках
        
        Args:
            - dx: значение скроллинга по x
            - dy: значение скроллинга по y
        """
        POPUP_SCROLL = (By.XPATH, '//*[@id="virtuoso-scroller"]//*[@data-testid="thumbVerticalScrollBar"]')
        scroll = self.find_element(POPUP_SCROLL)
        scrollbar_x = scroll.location.get('x') + dx
        scrollbar_y = scroll.location.get('y') + 140
        scrollbar_x2 = scrollbar_x
        scrollbar_y2 = scrollbar_y + dy
        pyautogui.moveTo(scrollbar_x, scrollbar_y)
        pyautogui.dragTo(scrollbar_x2, scrollbar_y2, 2, button='left')


    def dropdown_scroll_wheel(self, scl: int = -1):
        """Прокручивает скролл в выпадающих списках
        
        Args:
            - scl: количество скролов (минус - вниз)
        """
        POPUP_SCROLL = (By.XPATH, '//*[@id="virtuoso-scroller"]//*[@data-testid="thumbVerticalScrollBar"]')
        scroll = self.find_element(POPUP_SCROLL)
        scrollbar_x = scroll.location.get('x') -30
        scrollbar_y = scroll.location.get('y') + 200
        pyautogui.moveTo(scrollbar_x, scrollbar_y)
        mouse.wheel(scl)

    def generate_guid(self):
        """Генератор уникальных GUID"""
        return str(uuid.uuid4())