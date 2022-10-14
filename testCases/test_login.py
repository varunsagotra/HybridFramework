import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()   # Variable for Log


    def test_homePageTitle(self, setup):
        self.logger.info("***** START ********")
        self.logger.info("*****[Test_Case_Id]____Test_001_Login____********")
        self.logger.info("*********** Verifying home page title ***********")
        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***********INFO: Home Page Title Test is Passed ***********")
            self.logger.info("***** END - Passed ********")
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("***********Error: Home Page Title Test is Failed ***********")
            self.logger.warn("***********Warn: Home Page Title Test is Failed ***********")
            self.logger.warning("***********Warning: Home Page Title Test is Failed ***********")
            self.logger.info("***** END - Failed ********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***** START ********")
        self.logger.info("*****[Test_Case_Id]____Test_Login____********")
        self.logger.info("*********** Verifying Login page title ***********")

        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("***********INFO: Login Page Title Test is Passed ***********")
            self.logger.info("***** END - Passed ********")
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_login.png")
            self.driver.close()
            self.logger.info("***********INFO: Login Page Title Test is Passed ***********")
            self.logger.info("***** END - Failed ********")
            assert False


