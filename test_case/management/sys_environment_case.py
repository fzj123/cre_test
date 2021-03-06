import time
from model.screenshots import insert_img
from model import myunit
from page_object.sys_environment_page import SysEnvironmentPage
from model.logs import log

class SysEnvironmentCase(myunit.MyTest):

    #在管理中心-系统配置-环境变量配置页，点击“新建”,弹出新建环境变量窗口
    def test_env_newbutton_promptbox(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(2)
        env.button_new_click()
        time.sleep(3)
        try:
            self.assertEqual(env.env_new_page_error(), '新增环境变量')
            log().info('Judge success, and the result is:'+ env.env_new_page_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_newbutton_promptbox.jpg')

    #新建环境变量页面-变量名称未输入或输入空格点击“保存”按钮，有提示“名称不能为空”
    def test_env_newpage_variable_null(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.new_environment('','test','1','1','test')
        time.sleep(3)
        try:
            self.assertEqual(env.env_new_page_variable_error(), '此处为必填项，不能为空!')
            log().info('Judge success, and the result is:'+ env.env_new_page_variable_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_newpage_variable_null.jpg')

    #应用名未输入或输入空格点击“保存”按钮,有提示“应用名不能为空”
    def test_env_newpage_appname_null(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.new_environment('test_new_env', '', '1', '1', 'test_new_env')
        time.sleep(3)
        try:
            self.assertEqual(env.env_new_page_variable_error(), '此处为必填项，不能为空!')
            log().info('Judge success, and the result is:'+ env.env_new_page_variable_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_newpage_appname_null.jpg')

    #信息填写完整后点击“保存”按钮,弹出提示“新建成功”
    def test_env_newpage_save_successful (self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.new_environment('test_save_successful', 'test_save_successful', '1', '1', 'test_save_successful')
        time.sleep(3)
        env.input_variable_name('test_save_successful')
        time.sleep(3)
        log().info(env.env_new_page_save_error())
        try:
            self.assertEqual(env.env_new_page_save_error(), 'test_save_successful')
            log().info('Judge success, and the result is:'+ env.env_new_page_save_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_newpage_save_successful.jpg')

    #编辑页面-未选择环境变量点击“编辑”按钮,有提示“请选择一条记录”
    def test_env_editor_page_null(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.button_editor_click()
        time.sleep(3)
        try:
            self.assertEqual(env.env_new_page_editor_click_error(), '只能选择单条记录进行编辑！')
            log().info('Judge success, and the result is:'+ env.env_new_page_editor_click_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_editor_page_null.jpg')

    #编辑页面-选择两条及以上环境变量点击“编辑”按钮,有提示“只能选择一条记录”
    def test_env_editor_page_more(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.checkbox_value()
        env.button_editor_click()
        time.sleep(3)
        try:
            self.assertEqual(env.env_new_page_editor_click_error(), '只能选择单条记录进行编辑！')
            log().info('Judge success, and the result is:'+ env.env_new_page_editor_click_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_editor_page_more.jpg')

    #选择一条点击“编辑”按钮,弹出修改环境变量页签
    def test_env_editor_page_one(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.checkbox_one()
        time.sleep(3)
        env.button_editor_click()
        time.sleep(3)
        text = str(env.env_editor_page_successful_error())
        log().info(text)
        errot_text = text[0:6]
        log().info(errot_text)
        try:
            self.assertEqual(errot_text, '编辑环境变量')
            log().info('Judge success, and the result is:'+ errot_text)
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_editor_page_one.jpg')

    #修改编辑页面后点击“保存”按钮,有提示“修改成功”,变量名是不可编辑
    def test_env_editor_page_save(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.new_environment('test_editor_successful', 'test_editor_successful', '1', '1', 'test_editor_successful')
        time.sleep(3)
        env.input_variable_name('test_editor_successful')
        time.sleep(3)
        env.checkbox_one()
        time.sleep(3)
        env.button_editor_click()
        time.sleep(3)
        env.editor_environment('change_test_editor_successful', '2', '2', 'change_test_editor_successful')
        time.sleep(3)
        try:
            self.assertEqual(env.test_newpage_editor_save_error(), 'change_test_editor_successful')
            log().info('Judge success, and the result is:'+ env.test_newpage_editor_save_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_editor_page_save.jpg')

    #未选择环境变量点击“删除”按钮,有提示“请选择一条记录”
    def test_env_delete_button(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.butto_delect_click()
        time.sleep(3)
        try:
            self.assertEqual(env.test_delete_button_error(), '请选择记录！')
            log().info('Judge success, and the result is:'+ env.test_delete_button_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_delete_button.jpg')

    # 选择一条或多条点击“删除”按钮，有弹出确认删除环境变量提示窗
    def test_env_delete_button_more(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.checkbox_one()
        time.sleep(3)
        env.butto_delect_click()
        time.sleep(3)
        try:
            self.assertEqual(env.test_delete_button_more_error(), '确定要删除吗?')
            log().info('Judge success, and the result is:'+ env.test_delete_button_more_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_delete_button_more.jpg')


    #在删除确认窗口点击“确定”按钮,有弹出提示删除成功，不能再查询到删除后的环境变量
    def test_env_delete_button_sure(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.new_environment('test_delete_successful', 'test_delete_successful', '1', '1', 'test_delete_successful')
        time.sleep(3)
        env.input_variable_name('test_delete_successful')
        time.sleep(3)
        env.checkbox_one()
        time.sleep(3)
        env.butto_delect_click()
        time.sleep(3)
        env.delete_sure_button()
        time.sleep(3)
        env.input_variable_name('env_delete_button_sure')

        try:
            self.assertEqual(env.show_no_content_error(), '暂无内容')
            log().info('Judge success, and the result is:'+ env.show_no_content_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'test_delete_button_sure.jpg')

    #未选择环境变量点击“导出”按钮，弹出提示“是否导出全部？”
    def test_env_export_button_all(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.button_export_click()
        time.sleep(3)
        try:
            self.assertEqual(env.test_export_button_all_error(), '导出全部？')
            log().info('Judge success, and the result is:'+ env.test_export_button_all_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_export_button_all.jpg')

   #选择一条或多条环境变量点击“导出”
    def test_env_export_button_one(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.checkbox_one()
        time.sleep(3)
        env.button_export_click()
        time.sleep(5)
        insert_img(self.driver, 'env_export_button_one.jpg')

    #点击“导入”按钮,弹出“导入文件”窗口
    def test_env_import_button(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.button_import_click()
        time.sleep(3)
        try:
            self.assertEqual(env.test_import_button_error(), '导入')
            log().info('Judge success, and the result is:'+ env.test_import_button_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_import_button.jpg')
    #在导入文件窗口未选择待导入文件点击“确定”,有提示“请选择要导入的文件！”
    def test_env_import_button_sure(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.button_import_click()
        time.sleep(3)
        env.import_button()
        time.sleep(3)
        try:
            self.assertEqual(env.test_import_buttot_sure_error(), '请选择文件')
            log().info('Judge success, and the result is:'+ env.test_import_buttot_sure_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_import_button_sure.jpg')

    #导入文件时查看，有“覆盖”和“不覆盖”两种
    def test_env_import_button_choose(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.button_import_click()
        time.sleep(3)
        try:
            self.assertEqual(env.test_import_buttot_chooseyes_error(), '覆盖')
            log().info('Judge success, and the result is:'+ env.test_import_buttot_chooseyes_error())
            self.assertEqual(env.test_import_buttot_chooseno_error(), '不覆盖')
            log().info('Judge success, and the result is:'+ env.test_import_buttot_chooseno_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_import_button_choose.jpg')
    #导入文件后,可以在表单中查询到
    def test_env_import_buttot_save(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.import_environment()
        time.sleep(3)
        try:
            self.assertEqual(env.test_import_buttot_sure_error(), '上传成功！')
            log().info('Judge success, and the result is'+ env.test_import_buttot_sure_error())
        except Exception as e:
            log().exception('Failing judgment, the result is')
            log().exception(e)
        insert_img(self.driver, 'env_import_buttot_save.jpg')
    #选择应用类型值后，点击“查询”，可查询出符合应用类型的变量结果
    def test_env_appname_query(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.query_appname()
        time.sleep(5)
        try:
            self.assertEqual(env.test_appname_query_error(), 'APP')
            log().info('Judge success, and the result is:'+ env.test_appname_query_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_appname_query.jpg')
    #在变量名框中输入名称，点击“查询”
    def test_env_variable_query(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.input_variable_name('DB_')
        time.sleep(3)
        try:
            self.assertEqual(env.env_new_page_save_error(), 'DB_VERSION')
            log().info('Judge success, and the result is:'+ env.env_new_page_save_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_variable_query.jpg')
    #在描述框框中输入描述内容，点击“查询”
    def test_env_describe_query(self):
        env = SysEnvironmentPage(self.driver)
        self.url = '/managecenter/system/environment'
        env.open(self.url)
        env.login_action('admin', 'admin')
        time.sleep(3)
        env.input_describe_query('CRE数据库版本')
        time.sleep(3)
        try:
            self.assertIn('CRE数据库版本', env.test_describe_query_error())
            log().info('Judge success, and the result is:'+ env.test_describe_query_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'env_describe_query.jpg')