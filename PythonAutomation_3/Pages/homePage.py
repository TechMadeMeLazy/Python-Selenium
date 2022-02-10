from selenium.webdriver.common.by import By
import time


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_my_contracts_page(self):
        time.sleep(30)
        self.driver.find_element(By.XPATH, "//span[@class='hpe-nav-icon icon-services']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[text()='My Contracts']").click()
        time.sleep(30)
