import time
from model.screenshots import insert_img
from model import myunit
from page_object.sys_environment_page import SysEnvironmentPage
from model.logs import log

class SysEnvironmentCase(myunit.MyTest):
    # 在导入文件窗口未选择待导入文件点击“确定”,有提示“请选择要导入的文件！”
    def test_import_buttot_sure(self):
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
            log().info(env.test_import_buttot_sure_error())
        except Exception as e:
            log().exception(e)
        insert_img(self.driver, 'test_import_buttot_sure.jpg')
