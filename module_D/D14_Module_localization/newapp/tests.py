import datetime


import django.db.models
# from django.contrib.auth.models import User
# from .filters import PostFilter
# from .forms import PostForm, ContactForm, CommentForm
from django.core.mail import EmailMessage
from newapp.models import Category, PostCategory, Post


def my_test():

    all_categories = Category.objects.filter().values('id')  # <QuerySet [{'id': 1}, {'id': 2}, ...}]>
    for val in all_categories.values():

        ''' ПОЛУЧЕНИЕ СПИСКА РАССЫЛКИ по всем категогриям'''
        username_email = Category.objects.get(id=val).subscriber.values('username', 'email')
        subscriber_list = [{i['username']: i['email']} for i in username_email]

        ''' ПОЛУЧЕНИЕ СПИСКА НОВОСТЕЙ ПО КАТЕГОРЯИМ ЗА НЕДЕЛЮ'''
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

#
# if __name__ == '__main__':
#
#
#     my_test()
#
# # my_test()