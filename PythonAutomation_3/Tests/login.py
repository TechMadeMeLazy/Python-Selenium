from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
import HtmlTestRunner

from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from Config.config import *


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        self.driver.get(BASE_URL)
        login_page = LoginPage(self.driver)

        login_page.enter_user_name(USER_NAME)
        login_page.click_next_button()
        login_page.enter_password(PASSWORD)
        login_page.click_sign_in_button()

    def test_my_contracts_page(self):
        self.driver.get(BASE_URL)
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        login_page.enter_user_name(USER_NAME)
        login_page.click_next_button()
        login_page.enter_password(PASSWORD)
        login_page.click_sign_in_button()

        home_page.navigate_my_contracts_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))

# How to run from command prompt
# Run Tests parallel
# C:\Users\sdad\Downloads\Projects\Office_2022\PythonAutomation_3>pytest Tests/login.py -v -n 2 --html=./reports/Results_ParallelExecution.html

# When you have multiple packages structure(This is recommended procedure)
# C:\Users\sdad\Downloads\Projects\Office_2022\PythonAutomation_3>python -m Tests.login

# with __name__
# python login.py

# without __name__
# cd C:\Users\sdad\Downloads\Projects\Office_2022\PythonAutomation_3\Tests
# python -m unittest login.py
