from flask import Flask
from views_admin import admin
from views_news import news
from views_user import user
from flask_wtf.csrf import CSRFProtect
import logging
from logging.handlers import RotatingFileHandler
def create_app(config):

    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(user)
    app.register_blueprint(news)
    app.register_blueprint(admin)
    # 防御csrf跨域攻击
    CSRFProtect(app)
    logging.basicConfig(level=logging.DEBUG)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler(config.BASE_DIR + "/logs/xjzx.log", maxBytes=1024 * 1024 * 100,
                                           backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
    app.logger_xjzx = logging


    return app
