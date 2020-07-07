from common.util.env_conf import EnvConfBase


class Mysql(EnvConfBase):
    NAME = 'test'
    USER = 'root'
    PASSWORD = '123'
    PORT = 3306
    HOST = '127.0.0.1'
    ENGINE = 'django.db.backends.mysql'

# class Celery(EnvConfBase):
#     BROKER_URL = 'redis://:jic@2020@39.97.182.186:6380/0'
#     RESULT_BACKEND = 'redis://:jic@2020@39.97.182.186:6380/1'
