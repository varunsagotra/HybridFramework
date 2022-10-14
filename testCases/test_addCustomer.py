import json
import random
import string

from pageObjects.AddcustomerPage import AddCustomer
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Variable for Log

    def test_addCustomer(self, setup):
        self.logger.info("***** START ********")
        self.logger.info("*****[Test_Case_Id]____Test_003_AddCustomer____********")
        self.logger.info("*********** Verifying Customer page title ***********")
        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("*** Starting Add Customer Process ***")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("**** Providing customer details ******")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        # self.addcust.setEmail = json.dumps(self.addcust.setEmail.toJson(), indent=4)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Varun")
        self.addcust.setGender("Male")
        self.addcust.setDob("7/05/1985")
        self.addcust.setCompanyName("busyQA")
        # self.addcust.selectTaxExempt()
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setMngOfVendor("Vendor 2")
        # self.addcust.selectActive()
        self.addcust.setAdminComment("This is for testing.....")
        self.addcust.clickOnSave()

        self.logger.info("****** Add Customer TC Completed ******")

        # Customer Validation
        self.logger.info("******Customer Validation Process Started ******")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("**** Add Customer TC Passed ****")
        else:
            self.driver.save_screenshot(".//Screenshots/test_addCustomer_scr.png")
            self.logger.info("**** Add Customer TC Failed ****")
            assert True == False

            self.driver.close()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
