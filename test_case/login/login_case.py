import time
from model.screenshots import insert_img
from model import myunit
from page_object.login_test_page import LoginTestPage

class LoginCase(myunit.MyTest):

    def  test_login_success(self):
       po = LoginTestPage(self.driver)
       self.url = '/managecenter'
       po.open(self.url)
       po.login_action('admin', 'admin')
       time.sleep(2)
       insert_img(self.driver, 'login_success.jpg')
