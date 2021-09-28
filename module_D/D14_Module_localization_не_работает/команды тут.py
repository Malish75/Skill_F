#from django.test import TestCase

from newapp.models import *

# Создать двух пользователей (с помощью метода User.objects.create_user).
user1 = User.objects.create_user(username="ivanko",first_name="Иван",last_name="Иванов",)
user2 = User.objects.create_user(username="petrushko",first_name="Петр",last_name="Петров",)

# Создать два объекта модели Author, связанные с пользователями.
author1 = Author.objects.create(author=user1)
author2 = Author.objects.create(author=user2)

# Добавить 4 категории в модель Category.
category_cinema = Category.objects.create(category_name="кино")
category_sport = Category.objects.create(category_name="спорт")
category_auto = Category.objects.create(category_name="авто")
category_chields = Category.objects.create(category_name="дети")

# Добавить 2 статьи и 1 новость.
post1 = Post.objects.create(new_post="PO",title="Заголовок 1", content_new_post=" статья 1 статья 1 статья 1", author= author1)
post2 = Post.objects.create(new_post="PO",title="Заголовок 2", content_new_post=" статья 2 статья 2 статья 2", author= author2)
post3 = Post.objects.create(new_post="NE",title="Заголовок 3", content_new_post=" новость 3 новость 3 новость 3", author= author2)

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
post1.category.add(category_cinema)
post2.category.add(category_sport)
post3.category.add(category_auto, category_chields)

# Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
comm1 = Comment.objects.create(content_comments="коммент 1",post=post1, user=user1)
comm2 = Comment.objects.create(content_comments="коммент 2",post=post2, user=user2)
comm3 = Comment.objects.create(content_comments="коммент 3",post=post3, user=user2)
comm4 = Comment.objects.create(content_comments="коммент 4",post=post1, user=user2)

# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
post1.like()
post1.like()
post2.dislike()
post3.like()
post3.like()
post3.like()
comm1.like()
comm2.like()
comm3.like()
comm4.dislike()

# Обновить рейтинги пользователей.
author1.update_rating()
author2.update_rating()

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
r = Author.objects.all().order_by("-author_rating").values('author', 'author_rating')[0] # {'author': 4, 'author_rating': 0.0}
full_name = User.objects.filter(id = r["author"]).values("username")[0]["username"] # <QuerySet [{'username': 'ivanko'}]>
best_user = full_name + ", " + str(r['author_rating'])
print(best_user)

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи,
# основываясь на лайках/дислайках к этой статье.
best_post = Post.objects.all().order_by("-rating_new_post").values()[0]
print(best_post['time_in_new_post'].strftime("%d.%m.%Y"))
print(User.objects.get(id=best_post['author_id']).username)
print(Author.objects.get(id=best_post['author_id']).author_rating)
print(best_post["title"])
prev = Post.objects.all().order_by("-rating_new_post").values()[0]["content_new_post"][:125] + "..."
print(prev)  # не знаю как применить def preview к лучшему посту

# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
all_comm_best_post = Comment.objects.filter(post__id=9).values()
for _ in all_comm_best_post:
    print(
        _['time_in_comment'].strftime("%d.%m.%Y"),
        User.objects.get(id=_['user_id']).username,
        _['rating_comment'],
        _['content_comments'],
        sep="\n"
        )
    print()