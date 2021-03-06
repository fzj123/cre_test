from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from model.logs import log


class Base(object):

    def __init__(self, driver, base_url="http://100.0.10.209"):
        self.driver = driver
        self.base_url = base_url
    #打开浏览器
    def open(self, url):
        url_new = self.base_url +url
        self.driver.maximize_window()
        self.driver.get(url_new)
        sleep(3)

    # #定位元素
    # def find_element(self, *loc):
    #     return self.driver.find_element(*loc)
    # #d多个页面
    # def find_elements(self, *loc):
    #     return self.driver.find_elements(*loc)


    #显性等待-获取页面单个元素
    def find_element(self, loc):
        try:
            element = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(loc))
            return element
        except Exception as e:
            log().exception('Timeout waiting for')
            log().exception(e)
    #显性等待-获取页面多个元素
    def find_elements(self, loc):
        element = WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_all_elements_located(loc))
        return element


    #多表单切换,切换到iframe
    def iframe(self, iframeid):
        return self.driver.switch_to.frame(iframeid)

    #调用js
    def js_script(self, js):
        return self.driver.execute_script(js)

    #获取弹出框
    def switch_alert(self):
        alert = self.driver.switch_to_alert()
        return alert

    #鼠标-悬停
    def mouse_hover(self, *loc):
        # 定位到要悬停的元素
        above = self.driver.find_element(*loc)
        # 对定位到的元素执行悬停操作
        ActionChains(self.driver).move_to_element(above).perform()

    #获取当前窗口句柄
    def now_window_handle(self):
        return self.driver.current_window_handle
    #获取所有窗口句柄
    def all_window_handle(self):
        return self.driver.window_handles

