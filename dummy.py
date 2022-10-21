from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj=Service()
driver=webdriver.Chrome(service=obj)
driver.get("https://demoqa.com/text-box")
driver.find_element(By.ID,"userName").send_keys("datta")
driver.find_element(By.ID,"userEmail").send_keys("asdfa@af.com")
driver.find_element(By.ID,"currentAddress").send_keys("wesasf")
driver.find_element(By.ID,"permanentAddress").send_keys("sadasfasf")
driver.find_element(By.ID,"submit").click()
output=driver.find_elements(By.XPATH,"//p[@class='mb-1']")
for i in output:
    text=i.text
    print(text)