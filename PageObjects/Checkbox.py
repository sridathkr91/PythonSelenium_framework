from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Test_CheckBox:
    checkbox_menu_Xpath="//span[text()='Check Box']"
    expandAll_button_xpath="//button[@title='Expand all']"
    collapseAll_button_xpath="//button[@title='Collapse all']"
    Notes_Checkbox_xpath="//span[text()='Notes']//preceding::span[2]"
    testSuccess_mesage_xpath="//span[@class='text-success']"

    def __init__(self,driver):
        self.driver=driver

    def clickCheckboxMenu(self):
        self.driver.find_element(By.XPATH,self.checkbox_menu_Xpath).click()

    def checkNotes(self):
        ele=self.driver.find_element(By.XPATH,self.Notes_Checkbox_xpath)
        ele.click()

    def testSelection(self):
        text=self.driver.find_element(By.XPATH,self.testSuccess_mesage_xpath).text
        if 'notes' in text:
            print("selected ")
        else:
            print("not seletced")

    def expandALl(self):
        self.driver.find_element(By.XPATH,self.expandAll_button_xpath).click()
    def collapseALl(self):
        self.driver.find_element(By.XPATH,self.collapseAll_button_xpath).click()

