import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager

from common.models import BaseModel


class BaseUserManage(UserManager):
    pass


class User(BaseModel, AbstractBaseUser):
    no = models.CharField(help_text='编号', max_length=32, unique=True, default=uuid.uuid4,
                          error_messages={'unique': "该用户编号已存在"})
    username = models.CharField(help_text='用户名', max_length=32, unique=True, default=uuid.uuid4,
                                error_messages={'unique': "该用户名已存在"})
    password = models.CharField(help_text='密码', max_length=128, default='', blank=True)
    email = models.EmailField(help_text="邮箱", default=uuid.uuid4, unique=True,
                              error_messages={'unique': '该邮箱已存在'})

    objects = BaseUserManage()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = verbose_name_plural = '用户'
        db_table = 'user'

    def __str__(self):
        return f'User: <{self.username}[{self.pk}]>'
