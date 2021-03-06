# Generated by Django 3.2.5 on 2021-07-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_post_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_new_post',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
    ]
