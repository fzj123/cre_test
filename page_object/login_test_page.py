from page_object.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class LoginTestPage(Base):
    login_username_text_loc = (By.ID, 'username')
    login_password_text_loc = (By.ID, 'j_password')
    login_button_loc = (By.ID, 'submit')
    login_erro_hint_loc = (By.CLASS_NAME, 'ferrorhead')
    login_slider_loc = (By.XPATH, '//*[@id="slider2"]/div/div[2]')
    login_slider_text_loc = (By.XPATH, '//*[@id="slider2"]/div/div[1]')

    def login_username(self,text):
        self.find_element(*self.login_username_text_loc).send_keys(text)

    def clear_username(self):
        self.find_element(*self.login_username_text_loc).clear()

    def login_password(self,text):
        self.find_element(*self.login_password_text_loc).send_keys(text)

    def clear_password(self):
        self.find_element(*self.login_password_text_loc).clear()

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def login_slider(self):
        for index in range(5):
            try:
                source = self.find_element(*self.login_slider_loc)
                ActionChains(self.driver).drag_and_drop_by_offset(source, 300, 0).perform()
                texts = self.find_element(*self.login_slider_text_loc).text

                if texts.startswith('通过验证'):
                    print('成功滑动')
                    break
                else:
                    texts.startswith('请按住滑块')
                    continue
            except Exception as e:
                print(e)

    def login_action(self, username, password):
        self.clear_username()
        self.login_username(username)
        self.clear_password()
        self.login_password(password)
        self.login_slider()
        self.login_button()

