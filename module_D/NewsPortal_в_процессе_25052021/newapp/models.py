# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.category_name


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.FloatField(default=0.0)

    def __str__(self):
        #return f'{self.title}: {self.content_new_post[:125]}...'
        return f'{self.author}'

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

        print("рейтинг обновлен, ", self.author_rating)
        self.author_rating = self.author_rating + author_rating_new \
                             + comm_auth_new + comm_post_auth_new

        self.save()
        # NameError: name 'comments_author' is not defined ??????? откуда????
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы (чтоб переопр. название - см. класс Meta в модели)"



class Post(models.Model):
    post = "PO"
    new = "NE"
    POST_NEW = [(post, "статья"), (new,"новость")]
    new_post = models.CharField(max_length = 2, choices = POST_NEW, default = post)
    time_in_new_post = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150, null=False)
    content_new_post = models.TextField(null=False)
    rating_new_post = models.FloatField(default=0.0)

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

    # Например, получить     дату    добавления    лучшей    статьи
    # p = Post.objects.get(id=int(_['id']))
    # И     потом     превью
    # p.preview()

    def __str__(self):
        #return f'{self.title}: {self.content_new_post[:125]}...'
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'


class Comment(models.Model):
    content_comments = models.CharField(max_length=255)
    time_in_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.FloatField(default=0.0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()

    def __str__(self):
        return self.content_comments


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
