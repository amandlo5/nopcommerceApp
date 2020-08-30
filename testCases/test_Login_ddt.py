import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.conftest import setup
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')

        print('No: of rows: ',self.rows)

        lst_status = []
        for r in range(2,self.rows+1):
            self.user = XLUtils.getReadData(self.path,'Sheet1',r,1)
            self.password = XLUtils.getReadData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.getReadData(self.path, 'Sheet1', r, 3)
            time.sleep(3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.lp.clickLogout()
                    lst_status.append('Pass')

                elif self.exp == 'Fail':
                    self.lp.clickLogout()
                    lst_status.append('Fail')

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.lp.clickLogout()
                    lst_status.append('Fail')

                elif self.exp == 'Fail':
                    self.lp.clickLogout()
                    lst_status.append('Pass')

        if 'Fail' not in lst_status:
            self.driver.close()

            assert True
        else:
            self.driver.close()
            assert False