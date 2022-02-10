from selenium.webdriver.common.by import By
import time

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_user_name(self, username):
        self.driver.find_element(By.ID, 'username').clear()
        self.driver.find_element(By.ID, 'username').send_keys(username)

    def click_next_button(self):
        self.driver.find_element(By.ID, 'next').click()

    def enter_password(self, password):
        self.driver.find_element(By.ID, 'password').clear()
        self.driver.find_element(By.ID, 'password').send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(By.ID, 'signIn').click()

