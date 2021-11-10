from django.db import models
from django.contrib.auth.models import User




class Posts(models.Model):
    title_post = models.CharField('Заголовок', max_length=60, null=False)
    text_post = models.TextField('Объявление', null=False)
    CP = [('Танки', "Танки"), ('Хилы', 'Хилы'), ('ДД', 'ДД'), ('Торговцы', 'Торговцы'), \
            ('Гилдмастеры', 'Гилдмастеры'), ('Квестгиверы', 'Квестгиверы'), ('Кузнецы', 'Кузнецы'), \
                     ('Кожевники', 'Кожевники'), ('Зельевары', 'Зельевары'), ('Мастера заклинаний', 'Мастера заклинаний'),]
    category_post = models.CharField('Категория', choices=CP, max_length=50, null=False)
    dt_post = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Автор объявления", blank=True, null=True)

    def __str__(self):
        return self.title_post

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"



class Messages(models.Model):
    dt_message = models.DateTimeField('Дата сообщения', auto_now_add=True)
    text_message = models.TextField("Текст отклика")

    post = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='Отклик', blank=True, null=True,
                             max_length=200, related_name='messages_posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор отклика", blank=True, null=True)
    status = models.BooleanField(verbose_name='Видимость отклика', default=False)


