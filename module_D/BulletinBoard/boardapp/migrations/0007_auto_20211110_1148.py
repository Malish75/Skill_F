# Generated by Django 3.1.7 on 2021-11-10 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boardapp', '0006_auto_20211109_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='message',
            new_name='text_message',
        ),
        migrations.AlterField(
            model_name='messages',
            name='post',
            field=models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages_posts', to='boardapp.posts', verbose_name='Отклик'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор объявления'),
        ),
    ]