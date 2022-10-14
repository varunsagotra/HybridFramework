from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_Login_xpath = "//button[normalize-space()='Log in']"
    Logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):  # initialize the driver - automatically invokes at the time of object creation
        self.driver = driver


    # Action Methods
    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.Logout_xpath).click()


