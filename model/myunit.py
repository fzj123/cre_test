import unittest
from selenium import webdriver

class MyTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)


    def tearDown(self):
        self.driver.quit()