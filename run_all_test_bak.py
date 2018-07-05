import unittest
import time
from model.HTMLTestRunner_PY3 import HTMLTestRunner
from model.path import dir_path
from model.screenshots import img_dir

#指定测试用例为当前文件夹下的test_case目录

path = dir_path()
img_path = img_dir()
#test_dir = './test_case/'
test_dir = './test_case/test'
test_report = path +'/report'
discover_test = unittest.defaultTestLoader.discover(test_dir, pattern = '*_case.py')


if __name__ == "__main__":

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description="运行环境：windows 7, Chrome")
    runner.run(discover_test)

    fp.close()
