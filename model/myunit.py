import unittest
from selenium import webdriver

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)


    def tearDown(self):
        self.driver.quit()