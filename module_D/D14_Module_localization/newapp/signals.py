from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver  # импортируем нужный декоратор
import time
import datetime
from django.core.mail import EmailMessage
from newapp.models import Category, PostCategory, Post
import pytz  #  устранение проблем с UTC



'''РАССЫЛКА ПОДПИСЧИКАМ КАТЕГОРИИ ПРИ ДОБАВЛЕНИИ НОВОСТИ'''
@receiver(m2m_changed, sender=Post.category.through)
def notify_to_subscribers(sender, instance,**kwargs):
    ''' '''
    ''' ПОЛУЧЕНИЕ СПИСКА РАССЫЛКИ '''
    subscriber_list = []
    instance_category = instance.category.all().values('id')                # <QuerySet [{'id': 4}]>
    i_need_id_of_category = list(d["id"] for d in instance_category)        # [1]  - id категории новой новости
    for val in i_need_id_of_category:
        username_email = Category.objects.get(id=val).subscriber.values('username', 'email')
        subscriber_list = [{i['username']:i['email']} for i in username_email]
                                                                            # [{'admin': 'admin@example.com'}, {'asmal75': 'asmal75@bk.ru'}]
    ''' РАССЫЛКА '''
    content = f'{instance.content_new_post[50]}...' if len(instance.content_new_post) > 50 else instance.content_new_post
    title = instance.title.encode('utf-8')  # у меня на одном из проектов ругался на кодировку
    for subscrier in subscriber_list:
        for name, email in subscrier.items():
            to_email = email
            subject = 'Новая статья в Вашем любимом разделе!'
            html_content = f'Здравствуйте, уважаемый(-ая) {name}!'
            html_content += '<p>Приглашаем ознакомиться: <a href="http://127.0.0.1:8000/news/%s/">%s</a></p>' % (instance.id, title)
            html_content += '<p>%s</p>' % (content)
            from_email = 'andstamal@yandex.ru'
            msg = EmailMessage(subject, html_content, from_email, [to_email])
            msg.content_subtype = "html"
            msg.send()



'''ЕЖЕНЕДЕЛЬНАЯ РАССЫЛКА ПОДПИСЧИКАМ через Celery и tasks'''
def start_of_the_weekly_newsletter():
    all_categories = Category.objects.filter().values('id')  # <QuerySet [{'id': 1}, {'id': 2}, ...}]>
    for val in all_categories.values():

        ''' ПОЛУЧЕНИЕ СПИСКА РАССЫЛКИ по всем категогриям'''
        username_email = Category.objects.get(id=val['id']).subscriber.values('username', 'email')
        subscriber_list = [{i['username']: i['email']} for i in username_email]
        # print(username_email, subscriber_list)

        ''' ПОДГОТОВКА СПИСКА НОВОСТЕЙ ПО КАТЕГОРИЯМ ЗА НЕДЕЛЮ'''
        week_period = datetime.datetime.now() - datetime.timedelta(days=7)
        week_period = pytz.utc.localize(week_period)
        posts_list_weekly = []
        posts_category = PostCategory.objects.filter(category_id=val[
            'id']).values()  # <QuerySet [{'id': 216, 'post_id': 434, 'category_id': 8}, {'id': 217, ....},
        for item in posts_category:
            time_post = Post.objects.filter(id=item['post_id']).values("time_in_new_post")[0]['time_in_new_post']
            if time_post > week_period:
                posts_list_weekly.append(Post.objects.filter(id=item['post_id']).values('title', 'id'))

        if posts_list_weekly:  # список новостей непустой
            # print(posts_list_weekly)                                        #  [<QuerySet [{'title': '4fa', 'id': 454}]>, <QuerySet [{'title': '5епыуасяывас', 'id': 455}]>]

            '''ОТПРАВКА ПИСЕМ'''
            for subs in subscriber_list:
                for name, email in subs.items():
                    to_email = email
                    subject = 'Поступила Ваша подписка новостей за неделю.'
                    html_content = f'Здравствуйте, уважаемый(-ая) {name}!'
                    html_content += '<p> Приглашаем к прочтению: </p>'

                    for que in posts_list_weekly[0]:
                        title, id = que['title'], que['id']
                        title = title.encode('utf-8')  # у кого-то на одном из проектов ругался на кодировку
                        html_content += '\n'
                        html_content += '<p><a href="http://127.0.0.1:8000/news/%s/"> %s </a></p>' % (id, title)

                    from_email = 'andstamal@yandex.ru'
                    msg = EmailMessage(subject, html_content, from_email, [to_email])
                    msg.content_subtype = "html"
                    msg.send()






# def notify_to_subscribers(sender, instance, **kwargs):
#     pass
# m2m_changed.connect(notify_to_subscribers, sender=Post.category.through)


# @receiver(post_save, sender=Post)
# def notify_to_subscribers(sender, instance, created, **kwargs):
#     pass


