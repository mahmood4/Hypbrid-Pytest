import os
import time

import pytest
from selenium import webdriver
#from pageObjects.LoginPage import Login
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()#"https://admin-demo.nopcommerce.com/"
    username = ReadConfig.getUseremail()#"admin@yourstore.com"
    password = ReadConfig.getPassword()#"admin"

    logger = logGen.loggen()


    #@pytest.mark.regression
    def test_homePageTitle(self,setup):
        #self.driver = webdriver.Chrome()
        self.logger.info("**********test_001_login*****************")
        self.logger.info("**********Verifying Home Page Title*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(2)
        act_title=self.driver.title

        #print("act_title", act_title)
        if act_title =="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********Passed  Home Page Title*****************")
        else:
            self.driver.save_screenshot("..\\Screenshots\\" + "test_homePageTitle1.png")
            #self.driver.save_screenshot("C:\\Users\\s5114509\\PycharmProjects\\Hybrid-Pytest\\Screenshots\\" + "test_homePageTitle.png")
            #print(os.getcwd())
            #self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), '\\Screenshots\\','PutFileNameHere'))
            self.driver.close()
            assert False

    #@pytest.mark.skip
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        print("username",self.username)
        print("Password",self.password)
        self.lp.clicklogin()
        time.sleep(2)
        act_title=self.driver.title
        print("act_title",act_title)
        self.driver.close()
        if act_title =="Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
