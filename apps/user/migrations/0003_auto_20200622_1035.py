# Generated by Django 2.2 on 2020-06-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200622_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, default='', help_text='密码', max_length=128),
        ),
    ]
