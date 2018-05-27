import os,redis
class Config(object):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI='mysql://root:liujunjie@localhost:3306/xjzx'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    # session
    SECRET_KEY = "itheima"
    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 14  # session 的有效期，单位是秒
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class DevelopConfig(Config):
    DEBUG = True
