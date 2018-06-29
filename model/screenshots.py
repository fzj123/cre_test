import datetime
import os
from selenium import webdriver
from model.logs import log
from model.path import dir_path

#截图
def insert_img(driver, file_name):
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # base_dir = str(base_dir)
    # base_dir = base_dir.replace('\\', '/')
    # base = base_dir.split('test_case')[0]
    # print(base)
    base = dir_path()
    img_dirs = datetime.datetime.now().strftime("%Y-%m-%d")
    file_path = base + '/report/image/' + img_dirs +'/' + file_name
    log().info(file_path)
    log().info('Screenshots to')
    driver.get_screenshot_as_file(file_path)
    log().info('End of the screenshots')

#创建截图保存目录
def img_dir():
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # base_dir = str(base_dir)
    # base_dir = base_dir.replace('\\', '/')
    # base = base_dir.split('test_case')[0]
    base = dir_path()

    img_dirs = datetime.datetime.now().strftime("%Y-%m-%d")
    file_path = base + '/report/image/'
    LOG_DIR = os.path.join(file_path, img_dirs)
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)  # 创建路径




# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get('http://www.baidu.com')
#     img_dir()
#     insert_img(driver, 'baidu.jpg')
#     driver.quit()
#


