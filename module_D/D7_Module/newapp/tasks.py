from celery import shared_task
from .signals import start_of_the_weekly_newsletter


'''ЕЖЕНЕДЕЛЬНАЯ РАССЫЛКА ПОДПИСЧИКАМ через Celery и tasks (код в signals)'''
@shared_task
def notify_to_subscribers_weekly():
    print("Старт еженедельной рассылки новостей.")
    start_of_the_weekly_newsletter()
    print("Рассылка успешно завершена.")









# app_task()
# @shared_task()
# def hello():
#     time.sleep(10)
#     print("Hello, world! из newapp")
#
#
# @shared_task
# def printer(N):
#     for i in range(N):
#         time.sleep(1)
#         print(i+1)