from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver  # импортируем нужный декоратор
from .models import *
from django.core.mail import EmailMessage


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


# ''' СЧЕТЧИК ПО ДОБАВЛЕНИЮ НОВОСТИ ИЗЗА ОГРАНИЧЕНИЯ 3 ПОСТА'''
# @receiver(post_save, sender=Post)
# def daily_counter(sender, instance, created, **kwargs):
#     if created:  #  не забываем добавить, иначе уйдем в бесконечную рекурсия из-за .save()
#         if Post.objects.all().order_by('-time_in_new_post') == 1:
#             last_post_date = Post.objects.all().order_by('-time_in_new_post')[1].time_in_new_post.date()  #  получаем дату предпоследней новости
#         else:
#             last_post_date = Post.objects.all().order_by('-time_in_new_post')[0].time_in_new_post.date()  # нужно если новость одна
#         if last_post_date == instance.time_in_new_post.date():
#             instance.author.daily_posts_add_counter += 1
#         else:
#             instance.author.daily_posts_add_counter = 1
#         instance.author.save()
#     else:
#         pass


# def notify_to_subscribers(sender, instance, **kwargs):
#     pass
# m2m_changed.connect(notify_to_subscribers, sender=Post.category.through)


# @receiver(post_save, sender=Post)
# def notify_to_subscribers(sender, instance, created, **kwargs):
#     pass


