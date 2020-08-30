import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

class AddCustomers:

    lnkcustomer_path = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkcustomer2_path = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnaddnew_class = "/html/body/div[3]/div[3]/div/form[1]/div[1]/div/a"
    txtemail_xpath = "//input[@id='Email']"
    txtpassword_id = "//input[@id='Password']"
    txtcustomer_role_class = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstlistitem_administrator_xpath = "//li[contains(text(),'Administrators')]"
    lstlistitem_registered_xpath = "//li[contains(text(),'Registered')]"
    lstlistitem_guest_xpath = "//li[contains(text(),'Guests')]"
    lstlistitem_vendors_xpath = "//li[contains(text(),'Vendors')]"
    lstlistitem_forum_xpath = "//li[contains(text(),'Forum Moderators')]"
    drpmgr_vendor_id = "VendorId"
    rdgender_male_id = "Gender_Male"
    rdgender_female_id = "Gender_Female"
    txtfirst_name_xpath = "//input[@id='FirstName']"
    txtlast_name_xpath = "//input[@id='LastName']"
    txtdob_id = "DateOfBirth"
    txtcompany_name = "Company"
    txtadmin_comment_id = "AdminComment"
    btnsave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkcustomer_path).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkcustomer2_path).click()

    def ckickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnaddnew_class).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtemail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtpassword_id).send_keys(password)

    def setCustomerRole(self,role):
        self.driver.find_element_by_xpath(self.txtcustomer_role_class).click()
        time.sleep(3)
        if role == 'Registered':
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitems = self.driver.find_element_by_xpath(self.lstlistitem_registered_xpath)
        elif role == 'Administrator':
            self.listitems = self.driver.find_element_by_xpath(self.lstlistitem_administrator_xpath)
        elif role == 'Guests':

            self.listitems = self.driver.find_element_by_xpath(self.lstlistitem_guest_xpath)
        elif role == 'Vendors':
            self.listitems = self.driver.find_element_by_xpath(self.lstlistitem_vendors_xpath)
        elif role == 'Forum Moderators':
            self.listitems = self.driver.find_element_by_xpath(self.lstlistitem_forum_xpath)
        else:
            self.listitems = self.driver.find_element_by_xpath(self.lstlistitem_registered_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitems)

    def setManagetOfVendor(self,value):
        drp = Select(self.driver.find_element_by_id(self.drpmgr_vendor_id))
        drp.select_by_visible_text(value)

    def selectGender(self,gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdgender_male_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdgender_female_id).click()
        else:
            self.driver.find_element_by_id(self.rdgender_male_id).click()

    def setFirstName(self,fname):
        self.driver.find_element_by_xpath(self.txtfirst_name_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_xpath(self.txtlast_name_xpath).send_keys(lname)

    def setDob(self,dob):
        self.driver.find_element_by_id(self.txtdob_id).send_keys(dob)

    def setCompanyName(self,cname):
        self.driver.find_element_by_name(self.txtcompany_name).send_keys(cname)

    def setAdminComment(self,content):
        self.driver.find_element_by_id(self.txtadmin_comment_id).send_keys(content)

    def clickSave(self):
        self.driver.find_element_by_xpath(self.btnsave_xpath).click()
    

