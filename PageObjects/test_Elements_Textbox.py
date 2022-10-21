from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Test_Elements:
    header_elements_xpath="//div[@class='category-cards']/div[1]"
    heading_textbox_xpath="//span[text()='Text Box']"

    inputbox_fullName_id="userName"
    inputbox_email_id="userEmail"
    textarea_currentAddress_id="currentAddress"
    textarea_permanenetaddress_id = "permanentAddress"

    button_submit_xpath="//button[@class='btn btn-primary']"

    input_elements_xpath="//div[@class='col-md-3 col-sm-12']"
    output_elements_xpath="//p[@class='mb-1']"


    def __init__(self,driver):
        self.driver=driver

    def clickHeaderElement(self):
        self.driver.find_element(By.XPATH,self.header_elements_xpath).click()
    def clickHeadingTextbox(self):
        self.driver.find_element(By.XPATH,self.heading_textbox_xpath).click()

    def setFullname(self,fullname):
        self.driver.find_element(By.ID,self.inputbox_fullName_id).send_keys(fullname)
    def setEmail(self,email):
        self.driver.find_element(By.ID,self.inputbox_email_id).send_keys(email)
    def setCurrentAddress(self,currentAddress):
        self.driver.find_element(By.ID,self.textarea_currentAddress_id).send_keys(currentAddress)
    def setPermanentAddress(self,PermanentAddress):
        self.driver.find_element(By.ID,self.textarea_permanenetaddress_id).send_keys(PermanentAddress)

    def clearPermanentAddress(self):
        self.driver.find_element(By.ID,self.textarea_permanenetaddress_id).clear()
    def clearCurrentAddress(self):
        self.driver.find_element(By.ID,self.textarea_currentAddress_id).clear()
    def clearFullname(self):
        self.driver.find_element(By.ID,self.inputbox_fullName_id).clear()
    def clearEmail(self):
        self.driver.find_element(By.ID,self.inputbox_email_id).clear()

    def clickSubmit(self):
        self.driver.find_element(By.XPATH,self.button_submit_xpath).click()

    def outputElement(self):
        ListOfOutput=self.driver.find_elements(By.XPATH,self.output_elements_xpath)
        return ListOfOutput

    def inputElement(self):
        ListOfInput=self.driver.find_elements(By.XPATH,self.input_elements_xpath)
        return ListOfInput
