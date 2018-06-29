import os

#获取项目根目录D:/PycharmProjects/cre_test
def dir_path():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('test_case')[0]

    return base


