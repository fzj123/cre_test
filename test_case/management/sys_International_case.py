import time
from model.screenshots import insert_img
from model import myunit
from page_object.sys_International_page import SysInternationalPage
from model.logs import log

class SysInternationalCase(myunit.MyTest):
    # 在国际化配置页面，点击工具栏“新增语言词条”按钮，弹出新增语言词条的对话框
    def test_inter_new_button_click(self):
        inter = SysInternationalPage(self.driver)
        self.url = '/managecenter/language/dictionary'
        inter.open(self.url)
        inter.login_action('admin', 'admin')
        time.sleep(3)
        inter.button_new_click()
        try:
            self.assertEqual(inter.pop_alter_title_error(), '新增语言词条')
            log().info('Judge success, and the result is' + inter.pop_alter_title_error())
        except Exception as e:
            log().exception('Failing judgment, the result is')
            log().exception(e)
        insert_img(self.driver, 'inter_new_button_click.jpg')

    #未输入词条key和中文简体/中文繁体/英文时，点击“确定”，有提示“字典KEY不能为空！…..”四个字典项均为必填项
    def test_inter_new_button_click_null(self):
        inter = SysInternationalPage(self.driver)
        self.url = '/managecenter/language/dictionary'
        inter.open(self.url)
        inter.login_action('admin', 'admin')
        time.sleep(3)
        inter.page_new_language_input('', '', '', '')
        time.sleep(5)
        try:
            self.assertEqual(inter.input_dictionary_key_error(), '此处为必填项，不能为空!')
            log().info('Judge success, and the result is:' + inter.input_dictionary_key_error())
            self.assertEqual(inter.input_dictionary_en_us_error(), '此处为必填项，不能为空!')
            log().info('Judge success, and the result is:' + inter.input_dictionary_en_us_error())
            self.assertEqual(inter.input_dictionary_zh_cn_error(), '此处为必填项，不能为空!')
            log().info('Judge success, and the result is:' + inter.input_dictionary_zh_cn_error())
            self.assertEqual(inter.input_dictionary_zh_tw_error(), '此处为必填项，不能为空!')
            log().info('Judge success, and the result is:' + inter.input_dictionary_zh_tw_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'inter_new_button_click.jpg')

    #各字典项输入完整后点击“确定”,可看到新增加的字典
    def test_inter_save_show(self):
        inter = SysInternationalPage(self.driver)
        self.url = '/managecenter/language/dictionary'
        inter.open(self.url)
        inter.login_action('admin', 'admin')
        inter.page_new_language_input('test.svae.successful', 'TestSvaeSuccessful', '保存测试成功', '保存測試成功')
        time.sleep(5)
        inter.input_language_key('test.svae.successful')
        inter.button_query_click()
        time.sleep(5)
        try:
            self.assertEqual(inter.list_page_one_data_error(), 'test.svae.successful')
            log().info('Judge success, and the result is:' + inter.list_page_one_data_error())
        except Exception as e:
            log().exception('Failing judgment, the result is:')
            log().exception(e)
        insert_img(self.driver, 'inter_save_show.jpg')