import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PageObjects.test_Elements_Textbox import Test_Elements
from Utilities.readConfigIni import Utility_readConfigIni
from Utilities import readExcel
from PageObjects.Checkbox import Test_CheckBox

class Test_checkbox_002:
        URL=Utility_readConfigIni.readURL()

        def test_chbx001(self,setUp):
            self.driver=setUp
            self.driver.get(self.URL)
            obj=Test_CheckBox(self.driver)
            obj.clickCheckboxMenu()
            obj.expandALl()
            obj.checkNotes()
            obj.testSelection()
            obj.collapseALl()
            status=self.driver.find_element(By.XPATH,"//li[contains(@class,'rct-node rct-node-parent rct-node')]")
            assert status.get_attribute('class') =="rct-node rct-node-parent rct-node-collapsed"
            print("user has performed collapse all action")
            obj.expandALl()
            assert status.get_attribute('class') == "rct-node rct-node-parent rct-node-expanded"
            print("user has performed expand all action")


