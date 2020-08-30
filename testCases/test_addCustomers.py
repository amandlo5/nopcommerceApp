import string
import random
import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.conftest import setup
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddCustomerPage import AddCustomers


class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
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
        self.addcust.ckickOnAddNew()
        self.mail = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.mail)
        time.sleep(5)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRole("Guests")
        self.addcust.setManagetOfVendor("Vendor 2")
        time.sleep(3)
        self.addcust.selectGender("Male")
        time.sleep(3)
        self.addcust.setFirstName("Amol")
        time.sleep(3)
        self.addcust.setLastName("Mandloi")

        self.addcust.setDob("03/15/1993")

        self.addcust.setCompanyName("Mandlois")

        self.addcust.setAdminComment("This is for testing...")
        time.sleep(3)
        self.addcust.clickSave()

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "customer has been added succesfully." in self.msg:
            assert True == True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addcust_scr.png")
            assert True == False
        self.driver.close()

def random_generator(size=9, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
