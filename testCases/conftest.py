import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path='C:/Users/mumu/PycharmProjects/nopcommerceApp/chromedriver.exe')
        driver.implicitly_wait(5)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path='C:/Users/mumu/PycharmProjects/nopcommerceApp/geckodriver.exe')

    return driver

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

def pytest_configure(config):
    config._metadata['Project Name'] = 'non commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Amol'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Java_Home',None)
    metadata.pop('Plugins',None)




