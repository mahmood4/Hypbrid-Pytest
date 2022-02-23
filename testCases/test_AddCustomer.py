import os
import time
from utilities import XLUtils

import pytest
from selenium import webdriver
#from pageObjects.LoginPage import Login
from pageObjects.LoginPage import Login
from pageObjects.AddCustomer import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
import string
import random


@pytest.mark.sanity
class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()#"https://admin-demo.nopcommerce.com/"
#    path = ".//TestData//LoginData.xlsx"
    path = "C:\\Users\\User\\PycharmProjects\\Hybrid-Pytest\\TestData\\LoginData.xlsx"
    username = ReadConfig.getUseremail()#"admin@yourstore.com"
    password = ReadConfig.getPassword()#"admin"

    logger = logGen.loggen()
    print(os.getcwd())
    #@pytest.mark.skip
    def test_addCustomer(self,setup):

        self.logger.info("**********test_003_AddCustomer*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        print("ddddd",os.getcwd())
        print("username", self.username)
        print("Pa", self.password)
        self.lp.clicklogin()

        self.logger.info("**********Login Successful*****************")

        self.logger.info("**********Starting Add Customer Test*****************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        time.sleep(1)
        self.addcust.clickOnCustomersMenuItem()

     #   self.addcust.clickOnAddNew()
      #  self.email = random_generator() + "@gmail.com"
       # self.logger.info("**********Providing Customer Information*****************")

       # self.rows = XLUtils .getRowCount(self.path,'Sheet2')
       # print("number of rows in Excel",self.rows)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet2')
        print("number of rows in Excel", self.rows)
        lst_status =[]

        for r in range(2,self.  rows+1):
            self.addcust.clickOnAddNew()
            self.email = random_generator() + "@gmail.com"
            self.logger.info("**********Providing Customer Information*****************")



            self.password = XLUtils.readData(self.path, 'Sheet2', r, 2)
            self.CustomerRoles = XLUtils.readData(self.path, 'Sheet2', r, 3)
            self.ManagerOfVendor = XLUtils.readData(self.path, 'Sheet2', r, 4)
            self.setGender = XLUtils.readData(self.path, 'Sheet2', r, 5)
            self.setFirstName = XLUtils.readData(self.path, 'Sheet2', r, 6)
            self.setLastName = XLUtils.readData(self.path, 'Sheet2', r, 7)
            self.setDOB = XLUtils.readData(self.path, 'Sheet2', r, 8)
            self.setCompanyName = XLUtils.readData(self.path, 'Sheet2', r, 9)
            self.setAdmincontent = XLUtils.readData(self.path, 'Sheet2', r, 10)


            print(self.setDOB)
            self.addcust.setEmail(self.email)
            self.addcust.setPassword(self.password)
            self.addcust.setCustomerRoles(self.CustomerRoles)
            self.addcust.setManagerofVendor(self.ManagerOfVendor)
            self.addcust.setGender(self.setGender)
            self.addcust.setFirstName(self.setFirstName)
            self.addcust.setLastName(self.setLastName)
            self.addcust.setDob(self.setDOB)
            self.addcust.setCompanyName(self.setCompanyName)
            self.addcust.setAdminContent(self.setAdmincontent)
            self.addcust.clickOnSave()

            self.logger.info("**********Saving customer info*****************")
            self.logger.info("**********Add customer validation started*****************")

            self.msg = self.driver.find_element_by_tag_name("body").text

            print(self.msg)
            if 'customer has been added successfully.' in self.msg:
                assert True == True
                self.logger.info("**********Add customer passed*****************")
            else:
                self.driver.save_screenshot("..\\Screenshots\\" + "test_addcustomer_scr.png")
                self.logger.info("**********Add customer Test Failed*****************")
                assert True == False


            self.logger.info("**********Ending Home Page Title Test*****************")

        self.driver.close()
def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))