import os
from celery import Celery


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mcdonalds.settings')
# связываем настройки Django с настройками Celery через переменную окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')


# создаем экземпляр приложения Celery и устанавливаем для него файл конфигурации. Мы также указываем пространство имен,
# чтобы Celery сам находил все необходимые настройки в общем конфигурационном файле settings.py.
# Он их будет искать по шаблону «CELERY_***».
app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')


# указываем Celery автоматически искать задания в файлах tasks.py каждого приложения проекта
app.autodiscover_tasks()