import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.conftest import setup
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        self.logger.info("***************** Test_001_Login **************************")
        self.logger.info("***************** Veify Title of Home Page **********************")
        self.driver = setup

        self.logger.info("***************** Home Page Title **************************")
        self.driver.get(self.baseUrl)
        act_title = self.driver.title

        if act_title == 'Your store. Login':
            assert True
            self.driver.close()
            self.logger.info("***************** Home Page Title is passed **************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.error("***************** Home Page Title is failed **************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
            self.logger.info("***************** Login Page Title is passed **************************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False

