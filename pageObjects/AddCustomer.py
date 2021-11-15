import time
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

class AddCustomer():
    #linkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    #//a[@href='#']//p[contains(text(), 'Customers')]
    linkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(), 'Customers')]"
    linkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtCustomerRoles_xpath  = "//span[@title='delete']"
    listitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    listitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    listitemGuests_xpath = "//li[contains(text(),'Guests')]"
    listitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drmgrOfVendor_id = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"


    #to initialize test case we need to intialtize driver

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.linkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.linkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(1)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.listitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.listitemRegistered_xpath)
        elif role == 'Guests':
            time.sleep(1)
            self.listitem = self.driver.find_element_by_xpath(self.listitemGuests_xpath)
        elif role == 'Vendors':
            time.sleep(1)
            self.listitem = self.driver.find_element_by_xpath(self.listitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.listitemGuests_xpath)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerofVendor(self,value):
        drp=self.driver.find_element_by_xpath(self.drmgrOfVendor_id).click()
        #drp.select_by_visible_text(value)

        if value == "Vendor 1":
            self.driver.find_element_by_xpath("//*[@id='VendorId']/option[2]").click()
        else:
            self.driver.find_element_by_xpath("//*[@id='VendorId']/option[3]").click()
        #WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
         #   (By.XPATH, self.drmgrOfVendor_id))).click()

    def setGender(self,gender):
        if gender =='Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender =='Female':
            self.driver.find_element_by_id(self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setFirstName(self,fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setDob(self,dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)


    def setAdminContent(self,content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).click()

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()







