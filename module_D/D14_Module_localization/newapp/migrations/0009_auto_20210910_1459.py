# Generated by Django 3.1.7 on 2021-09-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0008_auto_20210909_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name_en_us',
            field=models.CharField(help_text='name_of_category', max_length=30, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_ru',
            field=models.CharField(help_text='name_of_category', max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(help_text='name_of_category', max_length=30, unique=True),
        ),
    ]
