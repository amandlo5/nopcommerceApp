import time
from selenium import webdriver

class SearchCustomer:

    txtemail_id = 'SearchEmail'
    txtfname_id = 'SearchFirstName'
    txtlname_id = 'SearchLastName'
    btnsearch_id = 'search-customers'
    tblsearchresults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    row_xpath = "//table[@id='customers-grid']//tbody/tr"
    column_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtemail_id).clear()
        self.driver.find_element_by_id(self.txtemail_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element_by_id(self.txtfname_id).clear()
        self.driver.find_element_by_id(self.txtfname_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_id(self.txtlname_id).clear()
        self.driver.find_element_by_id(self.txtlname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnsearch_id).click()

    def getRowsCount(self):
        return len(self.driver.find_element_by_xpath(self.row_xpath))

    def getColumnCount(self):
        return len(self.driver.find_element_by_xpath(self.column_xpath))

    def searchCustomerByEmail(self,email):
        flag = False
        for r in range(1,self.getRowsCount()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,Name):
        flag = False
        for r in range(1,self.getRowsCount()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag