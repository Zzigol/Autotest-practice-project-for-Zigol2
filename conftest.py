import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def browser():
    opt = webdriver.ChromeOptions()
    '''pathToExtension = 'test_files\CryptoPRO_plugin.crx'
    opt.add_extension(pathToExtension)'''
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()