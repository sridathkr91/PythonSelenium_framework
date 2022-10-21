import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PageObjects.test_Elements_Textbox import Test_Elements
from Utilities.readConfigIni import Utility_readConfigIni
from Utilities import readExcel
class Test_TextBox_001:
    URL=Utility_readConfigIni.readURL()
    path=Utility_readConfigIni.returnExcelPath()

    def testTextBox1_001(self,setUp):
        self.driver=setUp
        self.driver.get(self.URL)
        obj001=Test_Elements(self.driver)
        self.driver.maximize_window()
        # obj001.clickHeaderElement()
        obj001.clickHeadingTextbox()
        obj001.setFullname(Utility_readConfigIni.readFullName())
        obj001.setEmail(Utility_readConfigIni.readEmail())
        obj001.setCurrentAddress(Utility_readConfigIni.readCurrAddress())
        obj001.setPermanentAddress(Utility_readConfigIni.readPermAddress())
        self.driver.execute_script('window.scrollBy(0,700)')
        obj001.clickSubmit()

        ListOfOutputElements=obj001.outputElement()
        ListOfInputElements=obj001.inputElement()
        if len(ListOfOutputElements)==len(ListOfInputElements):
            self.driver.save_screenshot(".\\Screenshots\\tc001.png")
            print("All the data from input area are entered and matching in the output area")
            assert True
        else:
            self.driver.execute_script('window.scrollBy(0,700)')
            self.driver.save_screenshot(".\\Screenshots\\tc001.png")
            assert False , "Not Passed  , Failed"

    def testTextBox1_002(self,setUp):
        self.driver=setUp
        self.driver.get(self.URL)

        obj001=Test_Elements(self.driver)
        self.driver.maximize_window()
        obj001.clickHeadingTextbox()

        rows=readExcel.getRowCount(self.path,'Sheet1')
        cols=readExcel.getColumnCount(self.path,'Sheet1')
        print("there are {} rows and {} columns".format(rows,cols))
        for i in range(2,rows+1):
            self.Name=readExcel.read(self.path,'Sheet1',i,1)
            self.Email = readExcel.read(self.path, 'Sheet1', i, 2)
            self.CurrentAddr = readExcel.read(self.path, 'Sheet1', i, 3)
            self.PermAddrName = readExcel.read(self.path, 'Sheet1', i, 4)
            
            obj001.setFullname(self.Name)
            obj001.setEmail(self.Email)
            obj001.setCurrentAddress(self.CurrentAddr)
            obj001.setPermanentAddress(self.PermAddrName)
            
            self.driver.execute_script('window.scrollBy(0,500)')
            obj001.clickSubmit()

            ListOfOutputElements = obj001.outputElement()
            ListOfInputElements = obj001.inputElement()
            if len(ListOfOutputElements) == len(ListOfInputElements):
                self.driver.save_screenshot(".\\Screenshots\\tc001.png")
                print("All the data from input area are entered and matching in the output area")
                assert True
            else:
                self.driver.execute_script('window.scrollBy(0,700)')
                self.driver.save_screenshot(".\\Screenshots\\tc001.png")
                assert False, "Not Passed  , Failed"

            self.driver.execute_script('window.scrollBy(-500,0)')
            obj001.clearFullname()
            obj001.clearEmail()
            obj001.clearPermanentAddress()
            obj001.clearCurrentAddress()


        