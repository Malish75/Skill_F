# Generated by Django 3.2.5 on 2021-07-10 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_author_daily_posts_add_counter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='daily_posts_add_counter',
        ),
    ]
