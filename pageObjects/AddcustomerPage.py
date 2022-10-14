import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


# Add Customer Page - Locators
class AddCustomer:
    linkCustomer_Menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkCustomer_MenuItem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddNew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFemaleGender_xpath = "//input[@id='Gender_Female']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    textCompanyName = "//input[@id='Company']"
    cbox_TaxExempt_xpath = "//input[@id='IsTaxExempt']"
    lstitemNewsletter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    lstitemNewsletter_Yourstorename_xpath = "//span[normalize-space()='Your store name']"
    lstitemNewsletter_Teststore2_xpath = "//span[normalize-space()='Test store 2']"
    lst_CustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lst_CustomerRoles_Administrators_xpath = "//li[contains(text(), 'Administrators')]"
    lst_CustomerRoles_ForumModerators_xpath = "//li[contains(text(), 'Forum Moderators')]"
    lst_CustomerRoles_Guests_xpath = "//li[contains(text(), 'Guests')]"
    lst_CustomerRoles_Registered_xpath = "//li[contains(text(), 'Registered')]"
    lst_CustomerRoles_Vendors_xpath = "//li[contains(text(), 'Vendors')]"
    drmngofvendor_xpath = "//select[@id='VendorId']"
    cbox_Active_xpath = "//input[@id='Active']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

# Action Items
    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_Menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.clickOnCustomerMenuItem).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.textCompanyName).send_keys(comname)

    def selectTaxExempt(self):
        self.driver.find_element(By.XPATH, self.cbox_TaxExempt_xpath).click()

    # def setNewsletter(self):

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.lst_CustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_CustomerRoles_Registered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_CustomerRoles_Administrators_xpath)
        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_CustomerRoles_ForumModerators_xpath)
        elif role == 'Guests':
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li[4]/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lst_CustomerRoles_Guests_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_CustomerRoles_Vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lst_CustomerRoles_Guests_xpath)
            time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setMngOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drmngofvendor_xpath))
        drp.select_by_visible_text(value)

    def selectActive(self):
        self.driver.find_element(By.XPATH, self.cbox_Active_xpath).click()

    def setAdminComment(self, commenttxt):
        self.driver.find_element(By.XPATH, self.setAdminComment).send_keys(commenttxt)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()



