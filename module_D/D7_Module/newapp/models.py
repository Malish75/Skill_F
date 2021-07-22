# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django import forms


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.FloatField(default=0.0)
    # daily_posts_add_counter = models.SmallIntegerField(default=0)

    def update_rating(self):
        # каждой статьи автора
        posts_author = Post.objects.filter(author=self.id)
        author_rating_new = 0
        for _ in posts_author.all().values('rating_new_post'):
            author_rating_new += _['rating_new_post']
        author_rating_new = author_rating_new*3

        # всех комментариев автора
        comm_auth = Comment.objects.filter(author=self.id)
        comm_auth_new = 0
        for _ in comm_auth.all().values('rating_comment'):
            comm_auth_new += _['rating_comment']

        # всех комментариев к статьям автора
        comm_post_auth = Post.objects.filter(author = self).values('rating_new_post')
        comm_post_auth_new = 0
        for _ in comm_post_auth:
            comm_post_auth_new += _['rating_new_post']

        # print("рейтинг обновлен, ", self.author_rating)
        self.author_rating = self.author_rating + author_rating_new \
                             + comm_auth_new + comm_post_auth_new
        self.save()

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        # return f'{self.title}: {self.content_new_post[:125]}...'
        return f'{self.author}'


class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True, null=False,)
    subscriber = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    post = "PO"
    new = "NE"
    POST_NEW = [(post, "статья"), (new,"новость")]
    new_post = models.CharField(max_length = 2, choices = POST_NEW, default = post, verbose_name="Тип")
    time_in_new_post = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    title = models.CharField(max_length=150, verbose_name="Заголовок", null=False)
    content_new_post = models.TextField(null=False, verbose_name="Текст",
                                        )
    rating_new_post = models.FloatField(default=0.0, verbose_name="Рейтинг")
    # photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name="Фото", blank=True)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="Обновлено")
    category = models.ManyToManyField(Category, through='PostCategory')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def like(self):
        self.rating_new_post += 1
        self.save()

    def dislike(self):
        self.rating_new_post += 1
        self.save()

    def preview(self):
        return f'{self.content_new_post[:125]}...'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)


class Comment(models.Model):
    content_comments = models.CharField(max_length=255)
    time_in_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.FloatField(default=0.0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # text = models.TextField(max_length=300, null=False)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    # def __str__(self):
    #     return self.content_comments


class UserCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
