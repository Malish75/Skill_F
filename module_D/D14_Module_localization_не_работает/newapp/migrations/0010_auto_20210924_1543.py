# Generated by Django 3.1.7 on 2021-09-24 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0009_auto_20210910_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_name_en_us',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_name_ru',
        ),
    ]
