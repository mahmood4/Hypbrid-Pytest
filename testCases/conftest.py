import pytest
import selenium

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


gecko_path = "c:\\Test\\geckodriver.exe"
path = "C:\\Users\\s5114509\\AppData\\Local\\Mozilla Firefox\\firefox.exe"
binary = FirefoxBinary(path)

@pytest.fixture()
def setup(browser):
    # logger = logGen.loggen()
     #global ddd = browser
     if browser =='chrome':
      driver = webdriver.Chrome(r"C:\Test\chromedriver.exe")  # driver path should start with r

 #     logger.info("**********Chrome Browser*****************")
      print("Launching chrome beowser")
     elif browser =='firefox':
        driver = selenium.webdriver.Firefox(executable_path=gecko_path,firefox_binary=binary)
     #   logger.info("**********Firefox Browser*****************")
        print("Launching Firefox browser")
     else:
         driver = webdriver.Chrome(r"C:\Test\chromedriver.exe")  # driver path should start with r
         #driver = webdriver.Ie(r"C:\Syed\Test11\IEDriverServer.exe")
     return driver



def pytest_addoption(parser):
   parser.addoption("--browser")

@pytest.fixture()
def browser(request):
   return request.config.getoption("--browser")


####################### Pytest HTML Report ***********************
def pytest_configure(config):
    config._metadata['Project name'] = 'nop commerce'
    config._metadata['Module name'] = 'Login'
    config._metadata['Tester'] = 'XYZ'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
    #config.metadata['Tester'] = 'XYZ'

