from rest_framework import status
from common.base.exceptions import Exception


class UserNameError(Exception):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = '该用户名不存在'


class PasswordError(Exception):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = '输入的密码错误'
