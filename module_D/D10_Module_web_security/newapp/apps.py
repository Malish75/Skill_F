from django.apps import AppConfig
import redis


class NewConfig(AppConfig):
    name = 'newapp'
    verbose_name = "Новости"  #  изменяет в админке newapp на новости

    # поскольку файл signals у нас отдельный и нигде в приложении не встречается, декораторы receive сработать не смогут,
    # а значит функции-обработчики не будут привязаны к сигналам. Давайте это исправим с помощью небольших изменений в файле:
    # нам надо переопределить метод ready, чтобы при готовности нашего
    # приложения импортировался модуль со всеми функциями обработчиками

    def ready(self):
        import newapp.signals






# red = redis.Redis(
#     host='localhost', #:10773
#     port=6379,
#     # host='redis-10773.c274.us-east-1-3.ec2.cloud.redislabs.com', #:10773
#     # port=10773,
#     # password='CHtEAiUtn3EMO5IGQfpAEwbJ07OGyURz'
# )


