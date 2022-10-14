import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/testdatasheet.xlsx"
    logger = LogGen.loggen()  # Variable for Log

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("***** START ********")
        self.logger.info("*****[Test_Case_Id]____Test_Login_DDT____********")
        self.logger.info("*********** Verifying Login page title ***********")

        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        # Fetching Data from Excel
        self.rows = XLUtils.getRowCount(self.path, 'datasheet')
        print("Number of rows in Excel", self.rows)

        lst_status = []  # Empty List variable

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'datasheet', r, 1)
            self.password = XLUtils.readData(self.path, 'datasheet', r, 2)
            self.exp = XLUtils.readData(self.path, 'datasheet', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            # time.sleep(3)
            # Validation
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***** TC Pass")
                    self.lp.clickLogout()
                    lst_status.append('Pass')
                elif self.exp == "Fail":
                    self.logger.info("***** TC Fail")
                    self.lp.clickLogout()
                    lst_status.append('Fail')
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("***** TC Fail")
                    self.lp.clickLogout()
                    lst_status.append('Fail')
                elif self.exp == "Fail":
                    self.logger.info("***** TC Pass")
                    self.lp.clickLogout()
                    lst_status.append('Pass')
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger("***** Login Test DDT is Passed")
            self.driver.close()
            assert True
        else:
            self.logger("***** Login Test DDT is Failed")
            self.driver.close()
            assert False
