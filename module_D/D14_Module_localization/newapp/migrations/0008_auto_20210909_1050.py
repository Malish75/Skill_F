# Generated by Django 3.1.7 on 2021-09-09 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(help_text='category name', max_length=30, unique=True),
        ),
    ]
