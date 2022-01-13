# Generated by Django 3.2.9 on 2022-01-12 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0002_auto_20220112_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boardapp.author', verbose_name='Автор объявления'),
        ),
    ]
