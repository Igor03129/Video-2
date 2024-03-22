from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestInput:
    def test_send_keys(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/issues")
        driver.find_element(By.XPATH, '//*[@id="js-issues-search"]').send_keys('buge' + Keys.ENTER)
        pass
