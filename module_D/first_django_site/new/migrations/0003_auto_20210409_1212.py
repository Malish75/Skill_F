# Generated by Django 3.1.7 on 2021-04-09 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_auto_20210408_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='new_post',
            field=models.CharField(choices=[('PO', 'статья'), ('NE', 'новость')], default='PO', max_length=2),
        ),
    ]
