import time
from model.path import dir_path
from page_object.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.logs import log
from page_object.login_page import LoginPage

class SysEnvironmentPage(Base, LoginPage):
    #新增，编辑，删除，导入，导出按钮
    button_new_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[1]/div/label[1]')
    button_editor_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[1]/div/label[2]')
    button_delect_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[1]/div/label[3]')
    button_import_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[1]/div/label[4]')
    button_exprot_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[1]/div/label[5]')
    #应用名，变量名，描述，
    select_appname_loc = (By.ID, 'app-name-select')
    input_variablename_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[2]/ul/li[2]/div/input')
    input_describe_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[2]/ul/li[3]/div/input')
    #检索按钮
    button_query_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[1]/div[2]/ul/li[4]/div/button')
    #新增,编辑按钮-变量名
    input_new_variablename_loc = (By.ID, 'variable-name')
    #新增，编辑按钮-应用名
    input_new_app_loc = (By.ID, 'env-app-name')
    #新增，编辑按钮-变量值
    input_new_variablevalue_loc = (By.ID, 'variable-value')
    #新增，编辑按钮-取值范围
    input_new_value_range_loc = (By.ID, 'value-range')
    #新增，编辑按钮-描述
    input_new_description_loc = (By.ID, 'variable-description')
    #新增，编辑按钮-确定
    input_new_surecreate_loc = (By.ID, 'sure-create-btn')
    #新增，编辑按钮-取消
    input_new_cancle_loc = (By.XPATH, '//*[@id="create-environment-dialog"]/div/div/div[3]/button[2]')

    #定位button_checkbox
    button_checkbox_loc = (By.XPATH, "//input[@type='checkbox']")
    #新增环境变量页面iframeid
    switch_new_env_page_iframeid = 'urlFrame'
    #表单复选框全选
    checkbox_value_loc =(By.XPATH, '//*[@id="tab-list-content"]/div/div[2]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/span/input')
    checkbox_one_loc = (By.XPATH, "//input[@type='checkbox']")
    #导入页面
    import_file_loc = (By.XPATH, '//*[@id="import-file"]')
    import_button_loc = (By.ID, 'sure-create-btn')
    #导入页面上传按钮
    test_import_upload_button_loc = (By.XPATH, '//*[@id="import-file"]')


    #断言-新增环境变量页面
    new_env_page_loc = (By.XPATH, '//*[@id="environment-dialog-title"]')
    #断言-新增环境变量页面，变量名为空
    new_env_variable_loc = (By.XPATH, '//*[@id="variable-name"]')
    #断言，保存成功，查询列表第一条数据变量名称
    env_new_page_save_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/div/span')
    #断言,获取弹出框（点击编辑按钮，提示“请选择一条记录”,确定要删除吗?）
    env_new_page_editor_click__loc = (By.CSS_SELECTOR, '.bootbox-body')
    #断言，显示编辑页面
    env_editor_page_successful_loc = (By.XPATH, '//*[@id="environment-dialog-title"]')
    # 断言-修改编辑页面后点击“保存”按钮，保存成功（应用名）
    test_newpage_editor_save_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/div/span')
    #断言-点击“删除”按钮,有提示“请选择一条记录”
    test_delete_button_loc = (By.CSS_SELECTOR, '.bootbox-body')
    #断言-表单显示暂无内容
    show_no_content_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[2]/div/div[2]/div[1]/table/tbody/div')
    #断言-导入，导出按钮弹出框-显示文本
    test_export_button_all_loc = (By.CSS_SELECTOR, '.bootbox-body')
    test_import_buttot_sure_loc = (By.CSS_SELECTOR, '.bootbox-body')
    #断言-导入按钮弹出框-显示文本
    test_import_button_loc = (By.XPATH, '//*[@id="common-import-dialog"]/div/div/div[1]/h4')
    #断言-导入覆盖记录按钮
    test_import_buttot_chooseno_loc = (By.XPATH, '//*[@id="form-horizontal import-xml-form"]/div/div[1]/div[2]/div/label[2]')
    test_import_buttot_chooseyes_loc = (By.XPATH, '//*[@id="form-horizontal import-xml-form"]/div/div[1]/div[2]/div/label[1]')
    #断言-应用名检索
    test_appname_query_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/div/span')
    #断言-描述检索
    test_describe_query_loc = (By.XPATH, '//*[@id="tab-list-content"]/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[6]/div/span')

    #点击新增按钮
    def button_new_click(self):
        self.find_element(*self.button_new_loc).click()
    #点击编辑按钮
    def button_editor_click(self):
        self.find_element(*self.button_editor_loc).click()
    #点击删除按钮
    def butto_delect_click(self):
        self.find_element(*self.button_delect_loc).click()
    #点击导入按钮
    def button_import_click(self):
        self.find_element(*self.button_import_loc).click()
    #点击导出按钮
    def button_export_click(self):
        self.find_element(*self.button_exprot_loc).click()
    #应用名下拉列表框选择
    def select_appname(self):
        return Select(self.find_element(*self.select_appname_loc))

    #输入变量名
    def imput_variablename(self, text):
        self.find_element(*self.input_variablename_loc).send_keys(text)
    #清空变量名
    def clear_variablename(self):
        self.find_element(*self.input_variablename_loc).clear()
    #输入描述
    def input_describe(self,text):
        self.find_element(*self.input_describe_loc).send_keys(text)
    #清空描述
    def clear_describe(self):
        self.find_element(*self.input_describe_loc).clear()
    #点击检索按钮
    def button_query_click(self):
        self.find_element(*self.button_query_loc).click()

    #新增环境变量，变量名，应用名，变量值，取值范围，描述，确认，取消
    def input_new_variablename(self, text):
        self.find_element(*self.input_new_variablename_loc).send_keys(text)
    def input_new_app(self, text):
        self.find_element(*self.input_new_app_loc).send_keys(text)
    def input_new_variablevalue(self, text):
        self.find_element(*self.input_new_variablevalue_loc).send_keys(text)
    def input_new_value_range(self, text):
        self.find_element(*self.input_new_value_range_loc).send_keys(text)
    def input_new_description(self, text):
        self.find_element(*self.input_new_description_loc).send_keys(text)
    def input_new_surecreate(self):
        self.find_element(*self.input_new_surecreate_loc).click()
    def input_new_cancle(self):
        self.find_element(*self.input_new_cancle_loc).click()

    #编辑环境变量页面，清空应用名，变量值，取值范围，描述
    def clear_new_app(self):
        self.find_element(*self.input_new_app_loc).clear()
    def clear_new_variablevalue(self):
        self.find_element(*self.input_new_variablevalue_loc).clear()
    def clear_new_value_range(self):
        self.find_element(*self.input_new_value_range_loc).clear()
    def clear_new_description(self):
        self.find_element(*self.input_new_description_loc).clear()

    #删除环境变量，点击确定按钮
    def delete_sure_button(self):
        js = 'document.getElementsByClassName("btn btn-info")[1].click();'
        self.js_script(js)

    #表单复选框全选
    def checkbox_value(self):
        return self.find_element(*self.checkbox_value_loc).click()

    #表单中的复选框，某一行
    def checkbox_one(self):
        return self.find_elements(*self.checkbox_one_loc)[1].click()

    #返回表单中所有的复选框
    def button_checkbox(self):
        checkboxs = self.find_elements(*self.checkbox_one_loc)
        return checkboxs

    #导入-确定按钮点击
    def import_button(self):
        self.find_element(*self.import_button_loc).click()
    #导入-定位上传按钮，添加本地文件
    def test_import_upload_button(self):
        path = dir_path() + '/file/Environment.xml'
        log().info(path)
        self.find_element(*self.test_import_upload_button_loc).send_keys(path)

    #获取提示框
    def prompt_box(self):
        text = self.switch_alert().text
        return text

    #新增环境变量页面——确定
    def new_environment(self, varname, appname, variablevalue, value_range, description):
        self.button_new_click()
        time.sleep(3)
        self.input_new_variablename(varname)
        time.sleep(3)
        self.input_new_app(appname)
        self.input_new_variablevalue(variablevalue)
        self.input_new_value_range(value_range)
        self.input_new_description(description)
        self.input_new_surecreate()
    #编辑环境变量——确定
    def editor_environment(self, appname, variablevalue, value_range, description):
        #清空
        self.clear_new_app()
        self.clear_new_variablevalue()
        self.clear_new_value_range()
        self.clear_new_description()
        time.sleep(5)
        #输入
        self.input_new_app(appname)
        self.input_new_variablevalue(variablevalue)
        self.input_new_value_range(value_range)
        self.input_new_description(description)
        self.input_new_surecreate()

    #导入
    def import_environment(self):
        self.button_import_click()
        self.test_import_upload_button()
        self.import_button()


    #选择应用名检索
    def query_appname(self):
        self.select_appname().select_by_index(1)
        self.button_query_click()
    #变量名检索
    def input_variable_name(self, value):
        self.clear_variablename()
        self.imput_variablename(value)
        self.button_query_click()
    #描述检索
    def input_describe_query(self, value):
        self.input_describe(value)
        self.button_query_click()

    #断言-新增环境变量页面
    def env_new_page_error(self):
        text = self.find_element(*self.new_env_page_loc).text
        return text
    #断言-变量名为空
    def env_new_page_variable_error(self):
        text = self.find_element(*self.new_env_variable_loc).get_attribute('data-original-title')
        return text
    #断言-新增保存成功
    def env_new_page_save_error(self):
        text = self.find_element(*self.env_new_page_save_loc).text
        return text
    #断言-获取弹出框（点击编辑按钮，提示“请选择一条记录”）
    def env_new_page_editor_click_error(self):
        text = self.find_element(*self.env_new_page_editor_click__loc).text
        return text
    #断言-显示编辑页面
    def env_editor_page_successful_error(self):
        text = self.find_element(*self.env_editor_page_successful_loc).text
        return text
    #断言-修改编辑页面后点击“保存”按钮，保存成功
    def test_newpage_editor_save_error(self):
        text = self.find_element(*self.test_newpage_editor_save_loc).text
        return text
    #点击“删除”按钮,有提示“请选择一条记录”
    def test_delete_button_error(self):
        text = self.find_element(*self.test_delete_button_loc).text
        return text
    # 断言,获取弹出框（确定要删除吗?）
    def test_delete_button_more_error(self):
        text = self.find_element(*self.env_new_page_editor_click__loc).text
        return text
    # 断言-表单显示暂无内容
    def show_no_content_error(self):
        text = self.find_element(*self.show_no_content_loc).text
        return text
    # 断言-导出按钮弹出框-显示文本
    def test_export_button_all_error(self):
        text = self.find_element(*self.test_export_button_all_loc).text
        return text
    # 断言-导入按钮弹出框-显示文本
    def test_import_button_error(self):
        text = self.find_element(*self.test_import_button_loc).text
        return text
    #断言-导入页面，提示“请选择文件”,“上传成功”
    def test_import_buttot_sure_error(self):
        text = self.find_element(*self.test_import_buttot_sure_loc).text
        return text
    # 断言-导入覆盖记录按钮
    def test_import_buttot_chooseyes_error(self):
        text = self.find_element(*self.test_import_buttot_chooseyes_loc).text
        return text
    def test_import_buttot_chooseno_error(self):
        text = self.find_element(*self.test_import_buttot_chooseno_loc).text
        return text
    # 断言-应用名检索
    def test_appname_query_error(self):
        text = self.find_element(*self.test_appname_query_loc).text
        return text
    # 断言-描述检索
    def test_describe_query_error(self):
        text = self.find_element(*self.test_describe_query_loc).text
        return text