
import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.conftest import setup
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddCustomerPage import AddCustomers
from pageObjects.SearchCustomerPage import SearchCustomer


class Test_004_SearchCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomer(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.addcust = AddCustomers(self.driver)

        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        searchCust = SearchCustomer(self.driver)
        searchCust.setFirstName("Victoria")
        searchCust.setLastName("Terces")
        searchCust.clickSearch()

        time.sleep(5)

        status = searchCust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.driver.close()