import os
from celery import Celery
from celery.schedules import crontab

####################################################
# ЗАПУСКАТЬ В РАЗНЫХ КОНСОЛЯХ - СМОТРИ ВНИЗУ !!!!!!#
####################################################


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


app.conf.beat_schedule = {
        'notify_every_weekly':
        {
            'task': 'newapp.tasks.notify_to_subscribers_weekly',
            'schedule': crontab(hour=20, minute=15, day_of_week='monday'),
            # 'schedule': crontab(),                                          # ежеминутно
            # 'schedule': crontab(minute='*/2')         # каждые 2 минуты
            #'args': ('тут_аргумент')  # аргумент передается в функцию в таске
            }
}








# 'print_every_5_seconds':
    #     {
    #         'task': 'newapp.tasks.printer',
    #         'schedule': 5,  #  5 раз
    #         'args': (5,),   # передается в printer
    #         },


# ЗАПУСК В НОВОЙ КОНСОЛИ
############   ВОТ   ТАК   ################
#    pip install eventlet
#    консоль №1    celery -A NewsPortal worker -l info -P eventlet
#    консоль №2    celery -A NewsPortal beat -l info --- при работе по расписанию
#    консоль №3     redis-cli
##########################################

# celery -A NewsPortal django_celery_beat.schedulers:DatabaseScheduler  ---   из админки задачи
# redis-server    ---  стартует при запуске системы
# celery -A NewsPortal worker -l INFO  --concurrency=3
# celery -A NewsPortal worker --pool=solo -l info --concurrency=2
# celery -A NewsPortal worker -P gevent --loglevel=INFO