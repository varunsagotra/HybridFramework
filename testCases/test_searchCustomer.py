import time

import pytest

from pageObjects.AddcustomerPageNew import AddCustomerNew
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Variable for Log

    @pytest.mark.regression
    def test_SearchCustomerByEmail(self, setup):
        self.logger.info("***** START ********")
        self.logger.info("*****[Test_Case_Id]____Test_004_Search____********")
        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.addcust = AddCustomerNew(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("********** Search Test Started ********")

        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("ZVWzM@gmail.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("ZVWzM@gmail.com")
        assert True == status
        self.driver.close()
        self.logger.info("******** TC Completed *************")
