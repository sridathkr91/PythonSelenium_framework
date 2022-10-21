from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture()
def setUp(browser):
    if browser=="chrome":
        # obj = Service()
        driver = webdriver.Chrome(executable_path=r"C:\Users\Dell\Desktop\NewTestEnv\Scripts\chromedriver.exe")
        yield driver
        driver.close()
    elif browser=='edge':
        # obj=Service()
        driver=webdriver.Edge(executable_path=r"C:\Users\Dell\Desktop\NewTestEnv\Scripts\msedgedriver.exe")
        yield driver
        driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

