import os
import time
from utilities import XLUtils

import pytest
from selenium import webdriver
#from pageObjects.LoginPage import Login
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
class Test_002_Login:
    baseURL = ReadConfig.getApplicationURL()#"https://admin-demo.nopcommerce.com/"
    #path = ".//testData/LoginData.xlsx"
    path = "C://Users//s5114509//PycharmProjects//Hybrid-Pytest//TestData//LoginData.xlsx"
  #  username = ReadConfig.getUseremail()#"admin@yourstore.com"
  #  password = ReadConfig.getPassword()#"admin"

    logger = logGen.loggen()


    #@pytest.mark.skip
    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("**********test_002_login*****************")
        self.logger.info("**********Verifying Login DDT itle*****************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("number of rows in Excel",self.rows)
        lst_status =[]

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            print("username",self.user)
            print("Pa",self.password)
            print("exp", self.exp)
            self.lp.clicklogin()
            time.sleep(2)
            exp_title = "Dashboard / nopCommerce administration"
            act_title=self.driver.title
            #print("act_title",act_title)
            #self.driver.close()
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("Passed")
                    self.lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("Failed")
                    self.lp.clicklogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("Failed")
                    #self.lp.clicklogout()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("Passed")
                    #self.lp.clicklogout()
                    lst_status.append("Pass")


        if "Fail" not in lst_status:
              self.logger.info("Login DDT test passed")
              self.driver.close()
              assert True
        else:
              self.logger.info("Login DDT test Failed")
              self.driver.close()
              assert False


