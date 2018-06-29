import os
import datetime
import logging
import logging.config
from model.path import dir_path

#日志
def log_out():
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # base_dir = str(base_dir)
    # base_dir = base_dir.replace('\\', '/')
    # base = base_dir.split('test_case')[0]
    base = dir_path()
    LOG_DIR = os.path.join(base, 'logs')
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)  # 创建路径

    LOG_FILE = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                'format': '%(asctime)s [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
            },
            'standard': {
                'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
            },
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },

            "default": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "simple",
                "filename": os.path.join(LOG_DIR, LOG_FILE),
                'mode': 'w+',
                "maxBytes": 1024*1024*5,  # 5 MB
                "backupCount": 20,
                "encoding": "utf8"
            },
        },
        "loggers": {
            "app_name": {
                "level": "INFO",
                "handlers": ["console"],
                "propagate": "no"
            }
        },

        "root": {
            'handlers': ['default',"console"],
            'level': "INFO",
            'propagate': False
        }
    }

    logging.config.dictConfig(LOGGING)


def log():
    log_out()
    return logging.getLogger(__file__)



#
# if __name__ == '__main__':
#     try:
#         b = 1 +'1'
#     except TypeError as e:
#         log().error(e)

