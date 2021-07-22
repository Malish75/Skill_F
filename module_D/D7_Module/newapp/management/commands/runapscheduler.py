'''ЗАПУСКАТЬ ОТДЕЛЬННО PY MANAGE.PY RUNAPSCHEDULER'''

import logging
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from newapp.models import Category, Post, PostCategory
from django.core.mail import EmailMessage
import datetime
logger = logging.getLogger(__name__)

# наша задача по выводу текста на экран
def weekly_newsletter_to_subscribers():
    #  Your job processing logic here...
    # print('Тут старт еженедельной рассылки типа')
    all_categories = Category.objects.filter().values('id')  # <QuerySet [{'id': 1}, {'id': 2}, ...}]>
    for val in all_categories.values():

        ''' ПОЛУЧЕНИЕ СПИСКА РАССЫЛКИ по всем категогриям'''
        username_email = Category.objects.get(id=val).subscriber.values('username', 'email')
        subscriber_list = [{i['username']: i['email']} for i in username_email]

        ''' ПОЛУЧЕНИЕ СПИСКА НОВОСТЕЙ ПО КАТЕГОРЯИМ ЗА НЕДЕЛЮ'''
        #   ТУТ НЕПРАВИЛЬНО ПОЛОВИНА, ВЗЯТЬ КОД ИЗ РАСССЫЛКИ ПО ТАСКАМ
        posts_list_weekly = []
        posts_category = PostCategory.objects.filter(
            category_id=val).values()  # <QuerySet [{'id': 216, 'post_id': 434, 'category_id': 8}, {'id': 217, 'post_id': 435, 'category_id': 8},
        week_period = datetime.datetime.now() - datetime.timedelta(days=7)
        for item in posts_category.keys():
            if item['time_in_new_post'] > week_period:
                posts_list_weekly.append(
                    (Post.objects.filter(id=item['post_id']).values('title'),
                     Post.objects.filter(id=item['post_id']).values('id'))  # <QuerySet [{'id': 434}
                )  # <QuerySet ['Необычный дуалбут: ноутбук с «двойным дном»', '434'

        # print(posts_list_weekly)

        '''ОТПРАВКА ПИСЕМ'''
        # title = instance.title.encode('utf-8')  # у меня на одном из проектов ругался на кодировку
        for subs in subscriber_list:
            for name, email in subs.items():
                to_email = email
                subject = 'Поступила Ваша подписка новостей за неделю.'
                html_content = f'Здравствуйте, уважаемый(-ая) {name}!'
                html_content += '<p> Приглашаем к прочтению: </p>'
                for val in posts_list_weekly:
                    html_content += '\n'
                    html_content += '<p><a href="http://127.0.0.1:8000/news/%s/"> %s </a></p>' % (val[1], val[0])

                from_email = 'andstamal@yandex.ru'
                msg = EmailMessage(subject, html_content, from_email, [to_email])
                msg.content_subtype = "html"
                msg.send()



# функция, которая будет удалять неактуальные задачи
def delete_old_weekly_newsletter_to_subscribers(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.weekly_newsletter_to_subscribers(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # добавляем работу нашему задачнику
        scheduler.add_job(
            weekly_newsletter_to_subscribers,
            trigger=CronTrigger(day_of_week='mon', hour="08", minute="30"),
            id="weekly_newsletter_to_subscribers",  # уникальный айди
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'weekly_newsletter_to_subscribers'.")

        scheduler.add_job(
            delete_old_weekly_newsletter_to_subscribers(),
            trigger=CronTrigger(
                day_of_week="tue", hour="00", minute="00"
            ),
            # Каждую неделю будут удаляться старые задачи, которые либо не удалось выполнить, либо уже выполнять не надо.
            id="delete_old_weekly_newsletter_to_subscribers(",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_weekly_newsletter_to_subscribers'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")