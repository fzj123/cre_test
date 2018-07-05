import time

from page_object.base import Base
from selenium.webdriver.common.by import By
from page_object.login_page import LoginPage
from model.logs import log

class SysInternationalPage(Base, LoginPage):
    # 新增，编辑，删除，导入，导出按钮
    button_new_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[1]/div/label[1]')
    button_editor_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[1]/div/label[2]')
    button_delect_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[1]/div/label[3]')
    button_import_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[1]/div/label[4]')
    button_exprot_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[1]/div/label[5]')
    # 语言词条key，区域语言，语言词条值，
    input_language_key_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[2]/ul/li[1]/div/input')
    input_language_area_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[2]/ul/li[2]/div/input')
    input_language_value_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[2]/ul/li[3]/div/input')
    # 检索按钮
    button_query_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[2]/ul/li[4]/div/button')
    #页面表单第一条数据
    list_page_one_data_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/span')
    # 新增语言词条页面元素定位
    page_dictionary_key_loc = (By.ID, 'dictionary-key') #语言词条Key
    page_dictionary_en_us_loc = (By.ID, 'dictionary-en-us') #英文
    page_dictionary_zh_cn_loc = (By.ID, 'dictionary-zh-cn') #中文简体
    page_dictionary_zh_tw_loc = (By.ID, 'dictionary-zh-tw') #中文繁体
    page_button_new_sure_loc = (By.ID, 'sure-create-btn') #确定按钮
    pop_alter_title_loc = (By.ID, 'language-dialog-title') #新增语言词条页面元素定位-页面标题


    #test
    def button_tests_click(self):
        self.find_element(self.button_new_loc).click()

    # 点击新增按钮,点击编辑按钮,点击删除按钮,点击导入按钮,点击导出按钮,
    def button_new_click(self):
        self.find_element(self.button_new_loc).click()
    def button_editor_click(self):
        self.find_element(self.button_editor_loc).click()
    def butto_delect_click(self):
        self.find_element(self.button_delect_loc).click()

    def button_import_click(self):
        self.find_element(self.button_import_loc).click()

    def button_export_click(self):
        self.find_element(self.button_exprot_loc).click()


    # 输入-语言词条key，区域语言，语言词条值
    def input_language_key(self, key):
        self.find_element(self.input_language_key_loc).send_keys(key)

    def input_language_area(self, area):
        self.find_element(self.input_language_area_loc).send_keys(area)

    def input_language_value(self, value):
        self.find_element(self.input_language_value_loc).send_keys(value)

    #点击检索按钮
    def button_query_click(self):
        self.find_element(self.button_query_loc).click()


    # 新增语言词条页面-语言词条Key，英文，中文简体，中文繁体（输入value），点击确定按钮
    def input_dictionary_key_value(self, key):
        self.find_element(self.page_dictionary_key_loc).send_keys(key)

    def input_dictionary_en_us_value(self, us):
        self.find_element(self.page_dictionary_en_us_loc).send_keys(us)

    def input_dictionary_zh_cn_value(self, cn):
        self.find_element(self.page_dictionary_zh_cn_loc).send_keys(cn)

    def input_dictionary_zh_tw_value(self, tw):
        self.find_element(self.page_dictionary_zh_tw_loc).send_keys(tw)

    def button_new_sure_click(self):
        self.find_element(self.page_button_new_sure_loc).click()


    #新增语言词条页面-输入语言词条Key，英文，中文简体，中文繁体
    def page_new_language_input(self, key, us, cn, tw):
        self.button_new_click()
        time.sleep(5)
        self.input_dictionary_key_value(key)
        self.input_dictionary_en_us_value(us)
        self.input_dictionary_zh_cn_value(cn)
        self.input_dictionary_zh_tw_value(tw)
        self.button_new_sure_click()


    # 断言-新增语言词条页面标题（点击新增按钮）
    def pop_alter_title_error(self):
        text = self.find_element(self.pop_alter_title_loc).text
        return text

    # 断言-新增语言词条页面,语言词条Key，英文，中文简体，中文繁体,获取文本信息
    def input_dictionary_key_error(self):
        text = self.find_element(self.page_dictionary_key_loc).get_attribute('data-original-title')
        return text
    def input_dictionary_en_us_error(self):
        text = self.find_element(self.page_dictionary_en_us_loc).get_attribute('data-original-title')
        log().info(text)
        return text
    def input_dictionary_zh_cn_error(self):
        text = self.find_element(self.page_dictionary_zh_cn_loc).get_attribute('data-original-title')
        log().info(text)
        return text
    def input_dictionary_zh_tw_error(self):
        text = self.find_element(self.page_dictionary_zh_tw_loc).get_attribute('data-original-title')
        log().info(text)
        return text
    #断言-#页面表单第一条数据文本内容
    def list_page_one_data_error(self):
        text = self.find_element(self.list_page_one_data_loc).text
        return text