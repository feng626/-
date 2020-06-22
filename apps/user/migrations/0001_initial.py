# Generated by Django 2.2 on 2020-06-21 15:50

from django.db import migrations, models
import user.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('create_by', models.CharField(default='jic', max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_by', models.CharField(default='jic', max_length=255)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('no', models.CharField(default=uuid.uuid4, error_messages={'unique': '该用户编号已存在'}, help_text='编号', max_length=32, unique=True)),
                ('username', models.CharField(default=uuid.uuid4, error_messages={'unique': '该用户名已存在'}, help_text='用户名', max_length=32, unique=True)),
                ('password', models.CharField(blank=True, default='', help_text='密码', max_length=32)),
                ('email', models.EmailField(default=uuid.uuid4, error_messages={'unique': '该邮箱已存在'}, help_text='邮箱', max_length=254, unique=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
            },
            managers=[
                ('objects', user.models.BaseUserManage()),
            ],
        ),
    ]