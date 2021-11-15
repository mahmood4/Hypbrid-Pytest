import os
import time

from pageObjects.SearchCustomer import SearchCustomer
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


class Test_004_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()#"https://admin-demo.nopcommerce.com/"
    path = ".//TestData/LoginData.xlsx"
    username = ReadConfig.getUseremail()#"admin@yourstore.com"
    password = ReadConfig.getPassword()#"admin"

    logger = logGen.loggen()
    print(os.getcwd())
    #@pytest.mark.skip
    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):

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

        self.logger.info("**********Starting Search Customer By Email*****************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        time.sleep(1)
        self.addcust.clickOnCustomersMenuItem()

     #   self.addcust.clickOnAddNew()
      #  self.email = random_generator() + "@gmail.com"
        self.logger.info("**********Searching Customer by EmailID *****************")

        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        print("status::::",status)
        assert True == status
        self.logger.info("**********TC_Searching_Customer_by_EmailID Completed *****************")
       # self.rows = XLUtils .getRowCount(self.path,'Sheet2')
