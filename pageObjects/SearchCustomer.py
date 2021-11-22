import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException


class SearchCustomer:
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"

    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"


    #to initialize test case we need to intialtize driver

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.txtFirstName_id).clear()
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.txtLastName_id).clear()
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNoOfRows(self):
        #print("rows",len(self.driver.find_element_by_xpath(self.tableRows_xpath)))
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        print(self.getNoOfRows()+1)
        for r in range(1,self.getNoOfRows()+1):

            table = self.driver.find_element_by_xpath(self.table_xpath)
            try:
                table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
                emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            except NoSuchElementException:
                   emailid =""
                   pass
            print("email::::",emailid)
            if emailid == email:
                flag = True
                break
            else:
                allure.attach(self.driver.get_screenshot_as_png(),name="Not Found",attachment_type=AttachmentType.PNG)
                #print("email::::", emailid1)
                flag = False
        return flag


    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag